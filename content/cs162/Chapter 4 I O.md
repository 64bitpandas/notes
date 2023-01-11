---
title: "Chapter 4: I/O"
---

# UNIX Abstraction: Everything is a File

A **file** is a named collection of data in a file system. In the POSIX (Portable Operating System Interface for UNIX) standard, every file includes data (a sequence of bytes) and metadata (such as size, modification time, owner, security, and access control).

Files are organized into directories, which are folders containing files and other directories. Directories employ hierarchical naming (`/path/to/file.txt`) to ensure that ever file has a unique identifier.

Every process has a **current working directory (CWD),** which can be set using `int chdir(const char *path)`.

UNIX I/O has several key ideas:

- **Uniformity:** all IO operations use the same syscalls (open, close, read, write).
- **Open before use:** A device or channel must be opened and checked for permissions before any IO can commence.
- **Byte Oriented:** Everything can be represented as a series of bytes in an array.
- **Kernel-buffered reads and writes:** All data, whether incoming or outgoing, is stored in a kernel buffer and returned on request or when devices become available. This frees the processor to perform other tasks while IO is occurring but not ready.
    - Kernel buffering is typically done in blocks to enable efficient caching; as a consequence, `int fflush(FILE *stream)` must be called to push all buffered contents out of the file and complete the file operation.
- **Explicit Close:** Applications which are done accessing a file or device must call `close` to signal to the OS that the file is available.

# High level IO: Streams

High-level C libraries operate on **streams** (unformatted sequences of bytes with a position). When using high-level IO operations, the libraries automatically provide caching and write buffering to improve performance.

### Reading and Writing

To read or write using the high-level file API, we must first call `FILE* fopen(const char *filename, const char *mode)` to open the file.

The `mode` can be set to read (r), write(w), append(a), readwrite existing (r+), readwrite existing or create non-existing (w+), readwrite as append (a+), or binary versions of all stated (such as rb or ab+).

After opening the file, `size_t fread(void *restrict ptr, size_t size, size_t nmemb, FILE *restrict stream)` can be called to read contents from the file into the buffer at `*ptr`. This function reads `nmemb` items of data, each `size` bytes long, from `stream`.

The `fwrite` function can also be used (it has the same signature as `fread`) to write items from the buffer at `ptr` into `stream`.

Here's an example function that copies the file contents from the path `*src` into the file at path `*dest`:

```c
void copy(const char *src, const char *dest) {
	char buffer [100];
	FILE* read_file = fopen(src, "r");
	int buf_size = fread(buffer, 1, sizeof(buffer), read_file);
	fclose(read_file);
	FILE* write_file = fopen(dest, "w");
	fwrite(buffer, 1, buf_size, write_file);
	fclose(write_file);
}
```

### Stream Operations

Streams can be accessed in the same manner as files. Some API Standard Streams include `stdin` (input stream), `stdout` (output stream), and `stderr` (error stream).

The C libraries include several operations to work with streams:

- `int fputc(int c, FILE *stream)` puts a character `c` at the current position in `*stream`.
- `fputs` writes a string at the current position.
- `fgetc` and `fgets` reads the next character/string at the current position.

# Low Level IO: File Descriptors

Rather than working with streams, low level IO functions interface with the syscalls directly, and handle file identification using **file descriptors.** Every opened file is assigned an integer index in the kernel's file descriptor table, which can then be used to read and write to and from that file.

Unlike high level IO, where everything will be written at once from a buffer, operations on low-level file descriptors are visible immediately. As such, **mixing high and low level IO can be problematic** because it's very difficult to predict which sections of the file will be accessed at any particular point in time.

By default, every program starts with the three standard streams `stdin`, `stdout`, and `stderr`, which are assigned the file descriptors `0`, `1`, and `2` respectively. Every future file opened will be assigned some number greater than `2`. These numbers can be accessed with the constants `STDIN_FILENO`, `STDOUT_FILENO`, and `STDERR_FILENO` which require an `#include <unistd.h>`.

To open a file, use `int open(const char* filename, int flags, mode_t mode)`.

- Flags handle access modes (Rd, Wr, etc), as well as operating modes (Create, append, etc.).
- The mode is a bit vector of permission bits, bitwise OR'd (`|`) together.
- For a full list of flags and modes, see the man page ([https://man7.org/linux/man-pages/man2/openat.2.html](https://man7.org/linux/man-pages/man2/openat.2.html)).
- There is also the `int creat(const char* filename, mode_t mode)` function, which is equivalent to calling `open` with the flags `O_CREAT|O_WRONLY|O_TRUNC` (create the file, write only, replace existing file completely).

To read and write, use `ssize_t read(int filedes, void *buffer, size_t size)` and `int write(int filedes, void *buffer, size_t size)` respectively. These functions return the number of bytes that were read or written.

To change the current location within a file, use `lseek(int filedes, off_t offset, int whence)`.

- Several options for `whence` include:
    - `SEEK_SET`, which interprets the offset from the beginning of the file (position 0),
    - `SEEK_END`, which subtracts the offset from the end of the file, and
    - `SEEK_CUR`, which adds the offset to the current position in the file.

To duplicate descriptors (so that multiple processes can operate on the same file), there are two options:

1. Use `int dup(int oldfd)`, which creates and returns a new file descriptor which acts as an alias for `oldfd`.
2. Use  `dup2(int old, int new)`, using `new` instead of assigning a new file descriptor. This is useful for redirecting output (for example, specifying `new == STDOUT_FILENO` would print the file to standard output).

An implementation of the `copy` example from the high-level IO section using low-level IO might look something like this:

```c
void copy(const char *src, const char *dest) {
	char buffer [100];
	int read_fd = open(src, O_RDONLY);
	int bytes_read = 0;
	int buf_size = 0;
	while ((bytes_read = read(read_fd, &buffer[buf_size], sizeof(buffer) - buf_size)) > 0) {
		buf_size += bytes_read;
	}
	close(read_fd);
	int bytes_written = 0;
	int write_fd = open(dest, O_WRONLY);
	while (bytes_written < buf_size) {
		bytes_written += write(write_fd, &buffer[bytes_written], buf_size - bytes_written);
	}
	close(write_fd);
}
```

For an example of using `dup2` in the context of forks and pipes to execute processes, see [http://www.cs.loyola.edu/~jglenn/702/S2005/Examples/dup2.html](http://www.cs.loyola.edu/~jglenn/702/S2005/Examples/dup2.html).

### High vs Low Level IO

**High level streams are buffered in user memory:**

## Be careful when mixing high and low level IO

High level IO operations interface with the user-level buffer in chunks. However, low-level IO operations interface with the file directly. It is very hard to predict which portions of the file will be edited by which at what time.

# Pipes

UNIX pipes provide a way to communicate information both within and between processes. Using pipes is very similar to reading and writing from a file, with some additional checks involved.

To create a pipe, use `int pipe(int fileds[2])`, where `fileds[2]` is a two-integer array. When `pipe` is called, it automatically assigns two new file descriptors to the array.

To read and write to and from a pipe, the `write` and `read` low-level calls can be made on `fileds[1]` and `fileds[0]`, respectively.

![Untitled](Chapter%204%20I%20O/Untitled.png)

In the kernel, pipes are implemented as a fix-sized queue. This causes some issues when the allocated size is overflowed:

- If the buffer is full and Process A tries to write, then the pipe blocks (process gets put to sleep).
- If the buffer is empty and Process B tries to read, then the pipe also blocks.

### Closing Pipes

Just like files, pipes should be closed after use with `close(fileds[0])` for the read stream and `close(fileds[1])` for the write stream.

If a pipe is accessed after it is closed, several things could happen:

- If the write descriptor is closed, then the pipe will continually return EOF's if read from.
- If the read descriptor is closed, then attempting to write to the pipe will generate a SIGPIPE signal.

Here's an example of how to use pipes to transfer a string:

```c
int main() {
	int fds[2];
	pipe(fds);
	char *str = "hello world";
	size_t bytes_written = 0;
	size_t total = 0;
	while (bytes_written = write(fds[1], &str[total], strlen(&str[total]) + 1)) {
		total += bytes_written;
		if (str[total - 1] == ’\0’) break;
	}
	close(fds[1]);
	char *read_str = malloc(strlen(str) + 1);
	total = 0;
	size_t bytes_read;
	while (bytes_read = read(fds[0], &read_str[total], 50)) {
		total += bytes_read;
	}
	printf("%s", read_str);
	return 0;
}
```

# Signals

A **signal** is a software interrupt which provides a method of communicating state information about processes, the OS, or hardware. Different signals can have different handlers, or be ignored entirely, depending on the program.

Here is a list of standard Linux signals:

![Untitled](Chapter%204%20I%20O/Untitled%201.png)

Custom signal handlers can be specified using the `int signal(int signum, void (*handler)(int))` function. For example, `signal(SIGINT, printMsg)` will call the `printMsg()` function when the user quits out of the program using Ctrl+C.

Instead of specifying a custom handler, you also have the option of passing in `SIG_IGN`, which ignores the signal, or `SIG_DFL`, which runs the default behavior for that signal.

# Sockets

```c
#include <sys/socket.h>

/* Creates an endpoint for communication and returns a
	 file descriptor corresponding to that endpoint. */
int socket(int domain, int type, int protocol);

```

[https://man7.org/linux/man-pages/man2/socket.2.html](https://man7.org/linux/man-pages/man2/socket.2.html)

```c
#include <netdb.h>

struct addrinfo {
    int ai_flags;
    int ai_family;
    int ai_socktype;
    int ai_protocol;
    size_t ai_addrlen;
    char * ai_canonname;
    struct sockaddr * ai_addr;
    struct addrinfo * ai_next
};
```

```c
#define BUF_SIZE 1024
struct addrinfo *setup_address(char *port) {
	struct addrinfo *server;
	// Provides the preferred connection properties. 
	//If this is NULL, any connection is acceptible
	struct addrinfo hints; 
	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;
	hints.ai_flags = AI_PASSIVE;
	int rv = getaddrinfo(NULL, port, &hints, &server); // Connects to loopback (node is NULL)
	if (rv != 0) {
		printf("getaddrinfo failed: %s\n", gai_strerror(rv));
		return NULL;
	}
	return server;
}
void *serve_client(void *client_socket_arg) {
	int client_socket = (int)client_socket_arg;
	char buf[BUF_SIZE];
	ssize_t n;
	while ((n = read(client_socket, buf, BUF_SIZE)) > 0) {
		buf[n] = ’\0’;
		printf("Client Sent: %s\n", buf);
		if (write(client_socket, buf, n) == -1) {
			close(client_socket);
			pthread_exit(NULL);
		}
	}
	close(client_socket);
	pthread_exit(NULL);
}

int main(int argc, char **argv) {
	if (argc < 2) {
		printf("Usage: %s <port>\n", argv[0]);
		return 1;
	}

	struct addrinfo *server = setup_address(argv[1]);
	if (server == NULL) return 1;
	int server_socket = socket(server->ai_family, server->ai_socktype, server->ai_protocol);
	if (server_socket == -1) return 1;
	if (bind(server_socket, server->ai_addr, server->ai_addrlen) == -1) return 1;
	if (listen(server_socket, 1) == -1) return 1;
while (1) {
int connection_socket = accept(server_socket, NULL, NULL);
if (connection_socket == -1) {
perror("accept");
pthread_exit(NULL);
}
pthread_t handler_thread;
int err = pthread_create(&handler_thread, NULL,
serve_client, (void *)connection_socket);
if (err != 0) {
printf("pthread_create: %s\n", strerror(err));
pthread_exit(NULL);
}
pthread_detach(handler_thread);
}
pthread_exit(NULL);
}
```
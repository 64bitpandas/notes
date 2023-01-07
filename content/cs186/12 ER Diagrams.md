# ER Diagrams

Production databases have a lot of tables with complicated relationships. **Entity Relationship (ER) Diagrams** help us organize databases in a visual manner.

### Steps in Database Design

- Requirement Analysis: what do users need the database to do?
- Conceptual Design (ER Model): highly level description of DB schemas
- Logical Design: translate ER model into DBMS data model
- Schema Refinement: consistency, normalization
- Physical Design: indices, disk layout
- Security Design: who accesses what, and how

## Data Models

A data model is a collection of concepts for describing data.

A schema is a description of a particular collection of data using a given data model. 

Abstraction:

- Users see views (eg app on smartphone)
- Logical structure defined by conceptual schema
- Physical structure stores conceptual schema using files and indices

**Logical Data Independence:** maintain views when logical structure changes

**Physical data independence:** maintain logical structure when physical structure changes

## Entities

Entities are real-world objects that are described with attributes.

An entity set is a collection of the same type of entities (same attributes).

- Entity sets are described by a key (rectangle) and attributes (ellipses):
    
    ![Untitled](ER%20Diagrams/Untitled.png)
    
- Primary keys are underlined.

## Constraints

A relationship is an association between multiple entities or entity sets.

A relationship set is a collection of the same type of relationships (diamond).

![Untitled](ER%20Diagrams/Untitled%201.png)

![Untitled](ER%20Diagrams/Untitled%202.png)

![Untitled](ER%20Diagrams/Untitled%203.png)

## Weak Entities

Weak entities can be defined uniquely only with the key of another entity.

- The partial key (dashed underline) is the key in the other entity that must be combined with the owner entity’s key.
- Must exist in a many-to-one relationship (1 owner entity, many weak entities) with total participation
- Weak entities and their relationship set are bolded
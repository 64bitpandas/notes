---
title: "E-R Diagrams"
weight: 120
---

## Introduction

Production databases have a lot of tables with complicated relationships. **Entity Relationship (ER) Diagrams** help us organize databases in a visual manner.

### Steps in Database Design

Database design is a bit different from the rest of the content we've covered so far. In previous sections, we mostly learned how to use databases and write the algorithms that make it work efficiently-- but now, we need to ensure that the data itself is structured in a meaningful manner to take advantage of all those optimizations!

Here are some parts of database design:
- Requirement Analysis: what do users need the database to do?
- Conceptual Design: highly level description of DB schemas
- Logical Design: translate conceptual model into DBMS data model
- Schema Refinement: consistency, normalization
- Physical Design: indices, disk layout
- Security Design: who accesses what, and how

ER Diagrams help us with *conceptual design.*

## Relevant Materials 
 - [Note 13](https://notes.bencuan.me/cs186/coursenotes/n13-DBDesign.pdf)
 - [Discussion 10](https://docs.google.com/presentation/d/1qRrHbZ2zTLDUjrUJ5cn3jaAU1On0apKizWqfTKVGMwg/edit#slide=id.g5202e50430_0_0)

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

## Weak Entities

Weak entities can be defined uniquely only with the key of another entity.
- The partial key (dashed underline) is the key in the other entity that must be combined with the owner entity’s key.
- Must exist in a many-to-one relationship (1 owner entity, many weak entities) with total participation
- Weak entities and their relationship set are bolded
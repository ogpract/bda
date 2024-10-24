## CRUD Commands in MongoDB

### 1. Switch Database

- **Command:** `use <database_name>`
- **Description:** Switches the current session to the specified database. If the database does not already exist, MongoDB will create it when you insert data.

### 2. Select and Display

- **Command:** `db.collection.find(query)`
- **Description:** Retrieves documents from the specified collection that match the provided query criteria. This command can return multiple documents, and you can use additional parameters to limit, sort, or project specific fields from the result set.

### 3. Insert One

- **Command:** `db.collection.insertOne(document)`
- **Description:** Inserts a single document into the specified collection. If the collection does not exist, it will be created automatically. This operation is used for adding individual records to your MongoDB database.

### 4. Insert Many

- **Command:** `db.collection.insertMany([document1, document2, ...])`
- **Description:** Inserts multiple documents into the specified collection in a single operation. This command is efficient for adding a batch of records at once and is generally faster than inserting documents individually.

### 5. Update One

- **Command:** `db.collection.updateOne(filter, update, options)`
- **Description:** Updates the first document that matches the filter criteria in the specified collection. You can use this command to modify specific fields of a document or to completely replace the document based on the update operation.

### 6. Update Many

- **Command:** `db.collection.updateMany(filter, update, options)`
- **Description:** Updates all documents in the collection that match the filter criteria. This command is useful when you need to apply the same update to multiple documents at once, such as changing a common field across many records.

### 7. Delete One

- **Command:** `db.collection.deleteOne(filter)`
- **Description:** Deletes the first document that matches the filter criteria from the specified collection. This operation is typically used when you need to remove a single record from the database.

### 8. Delete Many

- **Command:** `db.collection.deleteMany(filter)`
- **Description:** Deletes all documents that match the filter criteria from the specified collection. This command is useful for bulk deletion operations, such as clearing out records that meet certain conditions.

### 9. Drop Collection

- **Command:** `db.collection.drop()`
- **Description:** Deletes the entire collection along with all its documents and indexes from the database. This operation is irreversible, so it should be used with caution, typically when you no longer need the collection or want to reset its data completely.


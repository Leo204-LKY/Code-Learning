## Lecture 12.2: MongoDB 操作  

### MongoDB 中的操作  
- MongoDB 提供多种不同的操作，用于搜索和修改 MongoDB 数据库中的数据  
    - 搜索操作  
    - 插入操作  
    - 删除操作  
    - 更新和替换操作  
- 本讲中，将介绍最重要的操作  

#### 查找操作：查找单个文档  
- 可以使用 `collection.findOne()` 方法查询集合中的单个文档  
- 这种方法使用查询文档，只查找集合中与查询匹配的文档子集  
- 该操作只返回第一个匹配的文档  
- 如果没有提供查询文档，或者提供的是空文档，查询将匹配到集合中的所有文档  

#### 查找操作例 1  
```js
// 创建 MongoDB 客户端并连接到群集
import { MongoClient } from mongodb;

// URI 可从你的 MongoDB Atlas 账户中获取
const uri = "mongodb+srv://user:<password>@cluster0.lqnvfse.mongodb.net/";
const client = new MongoClient(uri);

// 注意，数据库操作是异步的
async function run() {
    // MongoDB 操作需要在 try...catch 块内调用
    try {
        // 定义要访问的数据库和集合
        const database = client.db("sample_mflix");
        const movies = database.collection("movies");
        // 指定要查找字段 "title" 与值 "The Room" 匹配的文档
        const query = { title: "The Room" };
        const options = {
            // 如果有多个匹配项，按 "imdb-rating" 字段降序排序
            sort: {"imdb-rating": -1},
            // 我们只想在返回的文件中看到 "title" 和 "imdb" 字段
            projection: { _id: 0, title: 1, imdb: 1 }
        };

        // 最后，使用 findOne 方法运行查询，然后输出返回的影片
        const movie = await movies.findOne(query, options);
        console.log(movie);
    }
    finally {
        await client.close();
    }
}

run().catch(console.dir);
```
```
$ node mongoexample1.js
( { title: 'The Room', imdb: { rating: 3.5, votes: 25673, id: 368226 } }
$ 
```

#### 查找操作：查找多个文档  
- 可以使用 `collection.find()` 方法查询集合中的多个文档  
- 可以在选项参数中定义更多的查询选项，如排序：排序可按首选顺序组织返回的文档  
- 可以遍历返回的匹配文档  

#### 查找操作例 2  
```js
// 第一行和最后一行不再显示，因为它们在所有示例中都是一样的
...
async function run() {
    try {
        const database = client.db("sample_mflix");
        const movies = database.collection("movies");
        // 查找时长少于 5 分钟的电影
        const query = { runtime: { $lt: 5 } };
        // 按照片名的字母顺序对电影进行排序，并且只显示片名
        const options = {
            sort: {"title": 1},
            projection: { _id: 0, title: 1 }
        };
        // 最后，使用查找方法运行查询，然后打印返回的影片
        const cursor = movies.find(query, options);
        // 如果没有找到电影，用户将收到通知
        if ((await movies.countDocuments(query)) === 0) {
            console.log("No movies found!");
        }
        for await (const doc of cursor) {
            console.dir(doc);
        }
    }
}
...
```
```
$ node mongoexample2.js
{ title: 'Andrè and Wally B.' }
{ title: "Don't Hug Me I'm Scared" }
{ title: "Don't Hug Me I'm Scared 2: Time" }
{ title: 'Dots' }
{ title: 'For the Birds' }
{ title: 'Fresh Guacamole' }
{ title: 'Gagarin' }
{ title: 'Game Over' }
{ title: "Geri's Game" }
{ title: 'Jinxy Jenkins, Lucky Lou' }
{ title: 'Knick Knack' }
{ title: 'Lights Out' }
{ title: 'Luxo Jr.' }
{ title: 'Neko no shukai' }
{ title: 'Oktapodi' }
{ title: 'Passeio com Johnny Guitar' }
{ title: 'Pixels' }
{ title: "Season's Greetings" }
{ title: "Sebastian's Voodoo" }
{ title: 'Sisyphus' }
{ title: 'The Fly' }
{ title: 'The Kiss' }
{ title: 'The Kiss' }
{ title: 'Wind’ }
$ 
```

#### 插入操作：插入一个文档  
- 可以使用 `collection.insertOne()` 将文档插入到集合中  
- 要插入文档，需要定义一个对象，其中包含我们希望存储在集合中的字段和值  
- 如果我们指定的集合还不存在，该方法将创建它  
- 如果文档成功插入，则会添加一个 `insertedID` 字段，并将其值分配给 `_id` 字段  

#### 插入操作例 1  
```js
...
async function run() {
    try {
        // 指定要插入数据的数据库和集合
        const database = client.db("insertDB");
        const haiku = database.collection("haiku");
        // 指定我们要插入的文件
        const doc = {
            title: "Record of a Shriveled Datum",
            content: "No bytes, no problem. Just insert a document, in MongoDB."
        };

        // 运行插入操作并打印分配的 _id
        const result = await haiku.insertOne(doc);
        console.log(`A document was inserted with _id: ${result.insertedId}`);
    }
}
...
```
```
$ node mongoexample3.js
A document was inserted with _id: 6603f922370d2844268977ab
$
```

#### 插入操作：插入多个文档  
- 可以使用 `collection.insertMany()` 将多个文档插入到一个集合中  
- 该方法的输入是一个文档数组  
- 也可以将其他选项作为参数传递  
    - 例如，可以指定顺序，以防止在数组中前一个文档插入失败的情况下插入其余文档  
- 需要小心，因为指定不正确的参数可能会导致问题  

#### 插入操作例 2  
```js
...
async function run() {
    try {
        const databse = client.db("insertDB");
        const foods = database.collection("foods");
        // 在本例中，指定了一个要插入的文档数组
        const docs = [
            { name: "cake", healthy: false },
            { name: "lettuce", healthy: true},
            { name: "donut", healthy: false }
        ];
        const options = { ordered: true };

        // 使用指定的选项运行 insertMany() 操作，最后打印插入的文档数
        const result = await foods.insertMany(docs, options);
        console.log(`${result.insertedCount} documents were inserted`);
    }
}
...
```
```
$ node mongoexample4.js
3 documents were inserted
$ 
```

#### 删除文档：删除一个文档  
- 使用 `collection.deleteOne()` 删除单个文档  
    - 该方法使用查询文档来匹配查询中与查询相匹配的文档子集  
    - 如果没有提供查询文档（或查询文档为空），它将匹配集合中的**所有文档**，并**删除第一个匹配文档！**  
- 如果需要删除后的已删除文档，可以使用 `findOneAndDelete()`  

#### 删除文档例 1  
```js
...
async function run() {
    try {
        const database = client.db("sample_mflix");
        const movies = database.collection("movies");
        // 删除集合 "movies" 中标题为 "Annie Hall" 的文档
        const query = { title: "Annie Hall" };

        // 运行操作并打印结果
        const result = await moves.deleteOne(query);
        if (resule.deletedCount === 1) {
            console.log("Successfully deleted one document.");
        } else {
            console.log("No document matched the query. Deleted 0 documents.");
        }
    }
}
...
```
```
$ node mongoexample5.js
Successfully deleted one document.
$ 
```

#### 删除文档：删除多个文档  
- 可以使用 `collection.deleteMany()` 从集合中删除多个文档  
- **警告**：如果我们没有提供查询文档（或文档为空），MongoDB 将匹配集合中的所有文档并全部删除！  
    - 如果要删除集合中的所有文档，建议使用 `drop()` 方法，这样性能更好，代码也更清晰  

#### 删除文档例 2  
```js
...
async function run() {
    try {
        const database = client.db("sample_mflix");
        const movies = database.collection("movies");
        // 快到夏天了，我们想删除所有标题中包含 "Santa" 的圣诞电影
        const query = { title: { $regex: "Santa" } };

        // 运行操作并打印删除文件的数量
        const result = await movies.deleteMany(query);
        console.log("Deleted " + result.deletedCount + " documents.");
    }
}
...
```
```
$ node mongoexample6.js
Deleted 18 documents.
$ node mongoexample6.js
Deleted 0 documents.
$ 
```
注意，如果再次运行程序，将不会删除任何文件：所有匹配的文件都已删除！

#### 更新操作：更新一个文档  
- 可以使用 `collection.updateOne()` 从集合中更新文档  
- 该方法接受一个过滤文件（filter document）和一个更新文件（update document）作为输入参数  
- 如果查询与集合中的文档匹配，该方法会对相应字段和值应用更新  

#### 更新操作例 1  
```js
...
async function run() {
    try {
        const database = client.db("sample_mflix");
        const movies = database.collection("movies");
        // 要更新的文件标题应为 "Random Harvest"
        const filter = { title: "Random Harvest" };
        // 如果找不到匹配的文档，则创建它
        const options = { upsert: true };
        // 指定更新文档的方式
        const updateDoc = {
            $set: {
                plot: `A harvest of random numbers, such as ${Math.random()}`
            }
        };

        // 运行操作并打印结果
        const result = await movies.updateOne(filter, updateDoc, options);
        console.log(
            `${result.matchedCount} docs matched, updated ${result.modifiedCount} docs.`
        );
    }
}
...
```
```
$ node mongoexample7.js
1 docs matched, updated 1 docs.
$ 
```

#### 更新文档：更新多个文档  
- 可以使用 `collection.updateMany()` 更新集合中的多个文档  
- 更新将应用于所有匹配文件  
- 可指定其他选项  

#### 更新文档例 2  
```js
...
async function run() {
    try {
        const database = client.db("sample_mxflix");
        const movies = database.collection("movies");
        // 我们希望更新所有被评为 G 级的电影
        const filter = { rated: "G" };
        // 指定文档的更新方式
        const updateDoc = {
            $set: {
                random_review: `I am ${100 * Math.random()}% satisfied.`
            }
        };

        // 运行操作并打印结果
        const result = await movies.updateMany(filter, updateDoc);
        console.log(`Updated ${result.modifiedCount} docs.`);
    }
}
...
```
```
$ node mongoexample8.js
Updated 469 docs.
$ 
```

#### 更新文档：替换文档  
- 可以使用 `collection.replaceOne()` 从集合中替换单个文档  
    - 该方法接受一个查询文档和一个替换文档  
    - 如果查询与文档集中的文档相匹配，它将替换第一个匹配的文档，并删除原始文档中的字段  
    - 除非明确指定新值，否则 `_id` 字段的值保持不变  
- 使用 `findOneAndReplace()` 还可以替换文档  
    - 可配置为退回原文档或替换文档  

#### 更新文档例 3  
```js
...
async function run() {
    try {
        const database = client.db("sample_mflix");
        const movies = database.collections("movies");
        // 被替换文档的标题应包含 "The Cat from"
        const query = { title: { $regex: "The Cat from" } };
        // 指定替换文档
        const replacement = {
            title: `The Cat with ${Math.floor(Math.random() * 10)} Lives`
        };

        // 运行操作并打印结果
        const result = await movies.replaceOne(query, replacement);
        console.log(`Replaced ${result.modifiedCount} docs.`);
    }
}
...
```
```
$ node mongoexample9.js
Replaced 1 docs.
$ 
```

### 小结  
- 我们的应用程序需要数据库来帮助我们管理大量数据和处理多用户问题  
- 关系数据库和非关系数据库是两种主要数据库类型  
    - 关系数据库或非关系数据库的最佳选择取决于各种因素，如数据类型和用户负载  
- MongoDB 是一种流行的 NoSQL 数据库  
    - 通过各种 MongoDB 操作，我们可以查找、插入、删除、更新或替换数据，从而管理我们的数据集  
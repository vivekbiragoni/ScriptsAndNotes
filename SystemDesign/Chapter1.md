### Chapter 1: Scale from Zero to Millions of Users

#### Single Server Setup
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/8f58f570-aec3-4945-b71f-53158be96302)

- **Initial Setup**: Everything runs on a single server (web app, database, cache).
- **Request Flow**:
  1. Users access websites via domain names (e.g., api.mysite.com), with DNS usually provided by third-party services.
  2. IP address is returned to the browser or mobile app (e.g., 15.125.23.214).
  3. HTTP requests are sent to the web server using the obtained IP address.
  4. Web server returns HTML pages or JSON responses for rendering.
- **Traffic Sources**:
  - **Web Application**: Uses server-side languages (Java, Python) for business logic and storage, and client-side languages (HTML, JavaScript) for presentation.
  - **Mobile Application**: Communicates with the web server via HTTP protocol. Uses JSON format for API responses (e.g., GET /users/12 to retrieve user object with id = 12).

#### Database Scaling
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/90e79ae6-ba9c-4b68-b6a8-e5ccf90be93c)

- **Separation of Concerns**: With user base growth, separate servers for web/mobile traffic (web tier) and database (data tier) allow independent scaling.
- **Database Options**:
  - **Relational Databases (RDBMS/SQL)**: 
    - Examples: MySQL, Oracle, PostgreSQL.
    - Structure: Data stored in tables and rows, with join operations across tables using SQL.
  - **Non-Relational Databases (NoSQL)**:
    - Examples: CouchDB, Neo4j, Cassandra, HBase, Amazon DynamoDB.
    - Types: Key-value stores, graph stores, column stores, document stores.
    - Characteristics: Generally do not support join operations.

#### Choosing the Right Database
- **Relational Databases**: Preferred for most developers due to their reliability and long history of successful use.
- **Non-Relational Databases**: Suitable when:
  - Super-low latency is required.
  - Data is unstructured or non-relational.
  - Serialization and deserialization of data (JSON, XML, YAML) are needed.
  - Massive data storage is necessary.

#### Load Balancer
- **Function**: Distributes incoming traffic among web servers.
- ![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/a75fe107-a501-462c-a355-49e0bffe719b)

- **Setup**:
  - Users connect to the load balancer's public IP.
  - Web servers communicate via private IPs.
  - Enhances security and server communication efficiency.
- **Benefits**:
  - **Failover**: Traffic is rerouted to a healthy server if one goes offline.
  - **Scalability**: Additional servers can be added to handle increased traffic.

#### Database Replication
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/ac1318d2-170d-413b-b3c1-2edcbe9abd1c)

- **Master-Slave Model**:
  - **Master Database**: Handles write operations.
  - **Slave Databases**: Handle read operations and replicate data from the master.
- **Advantages**:
  - **Performance**: Write operations centralized on the master, read operations distributed among slaves.
  - **Reliability**: Data preserved across multiple locations.
  - **High Availability**: System remains operational even if one database is offline.

#### Handling Database Failures
- **Slave Database Failure**:
  - Read operations temporarily directed to the master.
  - New slave database replaces the failed one.
- **Master Database Failure**:
  - Slave promoted to master.
  - New slave replaces the old one for data replication.
  - Data recovery scripts may be needed to update slave data.
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/ff0b5e10-4e3c-4536-adbe-33fb592e065f)

#### Improved System Design with Load Balancer and Database Replication
- **Request Flow**:
  1. User gets the IP address of the load balancer from DNS.
  2. User connects to the load balancer.
  3. HTTP request routed to a web server.
  4. Web server reads data from a slave database.
  5. Web server routes write/update/delete operations to the master database.

### Next Steps: Enhancing Load/Response Time
- **Cache Layer**: Improve response time by caching frequently accessed data.
- **Content Delivery Network (CDN)**: Distribute static content (JavaScript, CSS, images, videos) to servers closer to users for faster delivery.


#### Cache
- **Function**: Temporarily stores the result of expensive responses or frequently accessed data in memory for faster subsequent requests.
- **Benefits**:
  - Improves application performance by reducing repeated database calls.
  - Reduces database workload.
  - Scales independently from other system components.
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/0a4503d5-8d1a-4e64-a3f4-8d10dc268ce0)

#### Cache Tier
- **Setup**: A separate data store layer faster than the database (Figure 1-7).
- **Read-through Cache Strategy**:
  - Web server checks the cache first for the requested data.
  - If data is available in cache, it is sent to the client.
  - If not, data is fetched from the database, stored in cache, and sent to the client.

#### Considerations for Using Cache
- **Usage**:
  - Use cache for data that is read frequently but modified infrequently.
  - Important data should be saved in persistent data stores as cache is volatile.
- **Expiration Policy**:
  - Implement an expiration policy to remove outdated data from cache.
  - Avoid making the expiration date too short or too long.
- **Consistency**:
  - Ensure data store and cache are in sync, especially challenging across multiple regions.
  - Refer to "Scaling Memcache at Facebook" for further details on maintaining consistency.
- **Mitigating Failures**:
  - Use multiple cache servers across different data centers to avoid a single point of failure (SPOF).
  - Overprovision memory to provide a buffer for increasing usage.
- **Eviction Policy**:
  - Popular policy: Least Recently Used (LRU).
  - Other policies: Least Frequently Used (LFU), First In First Out (FIFO).

#### Content Delivery Network (CDN)
- **Function**: A network of geographically dispersed servers delivering static content like images, videos, CSS, JavaScript files.
- **High-Level Workflow**:
  1. User requests a static asset (e.g., image.png) via a URL provided by the CDN provider.
  2. If not cached, the CDN server requests the asset from the origin server.
  3. The origin server returns the asset to the CDN server with an optional Time-to-Live (TTL) header.
  4. The CDN caches the asset and returns it to the user.
  5. Subsequent requests for the same asset are served from the CDN cache until the TTL expires.
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/93443267-733d-4456-b18b-2c092c1e0f72)
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/2cf51e97-3314-4a41-9379-1ee0d6f9d339)

#### Considerations for Using CDN
- **Cost**: Charged for data transfers; move infrequently used assets out of the CDN.
- **Cache Expiry**: Set appropriate cache expiry times to balance freshness and reload frequency.
- **CDN Fallback**: Ensure clients can request resources from the origin if the CDN fails.
- **Invalidating Files**:
  - Use APIs to invalidate CDN objects.
  - Implement object versioning (e.g., image.png?v=2).

#### Enhanced System Design with CDN and Cache
- **Static Assets**: Served by CDN for better performance (Figure 1-11).
- **Database Load**: Lightened by caching frequently accessed data.
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/a319706f-fe9b-47e3-b455-c92b76a2234b)


### Stateless Web Tier

#### Scaling the Web Tier Horizontally

To achieve horizontal scalability in the web tier, it is crucial to move state information (such as user session data) out of the web servers. This setup allows any web server to handle any client request, improving flexibility and robustness.

#### Stateless vs. Stateful Architecture

**Stateful Architecture:**
- **Description**: A stateful server remembers client data (state) from one request to the next. 
- **Example**: As shown in Figure 1-12, user session data and profile images are stored on specific servers. For instance, User A's session data is on Server 1, User B's on Server 2, and so forth.
- **Challenges**: 
  - HTTP requests must be routed to the same server that holds the user’s session data.
  - Adding or removing servers is complex.
  - Difficult to handle server failures.
    

  ![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/be82fa2b-5658-42ce-956b-8ff50b8f1c37)


**Stateless Architecture:**
- **Description**: A stateless server does not store any client data between requests. Each HTTP request is independent.
- **Example**: Illustrated in Figure 1-13, all HTTP requests from users are sent to a pool of web servers, which then fetch state data from a shared data store.
- **Advantages**:
  - Simplifies system design.
  - Enhances scalability and robustness.
  - Easy to add or remove servers dynamically based on traffic.
  
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/bfa1e5d9-683e-4860-85fe-8a3267af6b6c)


#### Implementation Steps for a Stateless Web Tier

1. **Move Session Data to Persistent Storage**: Store session data in databases or NoSQL stores, which are shared across all web servers.
2. **Use a Shared Data Store**: Web servers fetch necessary state data from a shared storage solution, which could be a relational database, Memcached/Redis, or NoSQL database.
3. **Enable Auto-scaling**: Automatically add or remove web servers based on traffic load, since web servers are stateless and do not hold any user-specific data.

![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/fe5ed703-e3ce-4cec-a912-5029202130a4)

#### Design Considerations

1. **Persistent Storage Options**: Choose between relational databases, NoSQL databases, or in-memory data stores like Memcached or Redis based on the scalability requirements and data access patterns.
2. **Load Balancer Configuration**: Ensure the load balancer can route requests to any web server, as each can handle requests independently by accessing shared session data.
3. **Data Consistency**: Ensure consistency between the shared data store and web servers. Data synchronization and handling data updates efficiently is crucial.
4. **Global Availability**: For websites with international users, deploying multiple data centers improves availability and reduces latency by serving users from geographically closer servers.



### Adding Message Queues and Tools


![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/69021db8-d336-44f4-82a1-80d051eb14ac)


To improve the system further, we can integrate a message queue and other essential tools. Here’s a simplified version of the updated design:

1. **Message Queue**: Adds flexibility and resilience by decoupling producers and consumers.
2. **Logging, Monitoring, Metrics, and Automation Tools**: Enhances system reliability and developer productivity by providing better visibility into system performance and automating repetitive tasks.

**Updated Design Example**:
- Imagine a single data center with:
  - Web servers sending tasks to a message queue.
  - Consumers processing tasks from the message queue.
  - Centralized logging and monitoring to keep track of system health.
  - Automation tools to streamline development and deployment processes.


![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/491ede3e-4d48-414e-96df-e84a8e7515ea)



### Database Scaling

As your data grows, your database can become overloaded. To handle this, you need to scale your database. There are two main approaches: **vertical scaling** and **horizontal scaling**.

#### Vertical Scaling (Scaling Up)
- **Definition**: Adding more power (CPU, RAM, disk space, etc.) to an existing machine.
- **Example**: Upgrading a database server to one with 24 TB of RAM to handle more data.
- **Drawbacks**:
  - **Hardware Limits**: There's a maximum limit to how much you can upgrade a single machine.
  - **Single Point of Failure**: If the powerful server fails, your entire database goes down.
  - **High Cost**: Powerful servers are very expensive.

#### Horizontal Scaling (Sharding)
- **Definition**: Adding more servers to distribute the load.
- **Sharding**: Splitting a large database into smaller pieces called shards. Each shard has the same schema but different data.
- **Example**: Distributing user data across multiple database servers based on user IDs using a hash function (e.g., user_id % 4).
- **Sharding Key**: A key (e.g., user_id) that determines how data is distributed across shards.
  
![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/785bb155-2c5a-4578-87f3-54d236931669)

**Benefits**:
- **Scalability**: Easily add more servers as needed.
- **Reduced Risk**: Failure of one server doesn’t bring down the entire database.

**Challenges**:
- **Resharding Data**: If a shard becomes too full or unevenly distributed, you may need to redistribute data.
- **Celebrity Problem**: High traffic to specific data (e.g., celebrity profiles) can overwhelm a shard.
- **Join Operations**: Joining data across shards is difficult, often requiring denormalization.

### Summary of Scaling for Millions of Users

To support millions of users, apply the following strategies:
1. **Keep Web Tier Stateless**: Store session data in a shared data store.
2. **Build Redundancy**: Ensure every tier has backup options to avoid single points of failure.
3. **Cache Data**: Use caching to reduce load on your database.
4. **Support Multiple Data Centers**: Distribute data centers geographically to improve availability and user experience.
5. **Host Static Assets in CDN**: Use Content Delivery Networks to serve static files quickly.
6. **Scale Data Tier by Sharding**: Distribute database load by sharding.
7. **Split Tiers into Individual Services**: Decouple services to manage and scale them independently.
8. **Monitor Your System**: Use logging and metrics to track system performance.
9. **Use Automation Tools**: Implement tools for continuous integration, testing, and deployment to improve efficiency.

![image](https://github.com/vivekbiragoni/ScriptsAndNotes/assets/104636857/92a7220c-7328-4823-8883-3f42e39a741d)

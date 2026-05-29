# Universal Code Documentation Standard

## Your Task

Document code following this universal schema. Works for Python, Terraform, SQL, TypeScript, YAML, and all other languages.

---

## Documentation Principles

**CRITICAL: Minimal but Sufficient**

When documenting code, you MUST:
- ✅ Use **minimal words** to convey complete meaning
- ✅ Use **simple language** (avoid jargon unless domain-specific)
- ✅ Use **clear vocabulary** (precise, unambiguous terms)
- ✅ Use **patterns** (consistent phrasing across codebase)
- ❌ Avoid **verbosity** (no redundant explanations)
- ❌ Avoid **ambiguity** (no vague descriptions)
- ❌ Avoid **obvious statements** (don't repeat what code shows)

**Examples:**

❌ Too verbose:
```
"This function is responsible for the retrieval of the complete skill definition
from the provider by searching through all available providers and then loading
the skill instructions from the SKILL.md file and combining them with metadata"
```

✅ Minimal but sufficient:
```
"Retrieve complete skill definition from provider"
```

❌ Too brief (ambiguous):
```
"Get skill"
```

✅ Clear and precise:
```
"Retrieve complete skill definition from provider"
```

---

## Required Sections

### Purpose (REQUIRED)
**What:** What this code does and why it exists
**Format:** 1-2 sentences starting with action verb
**Example:** `Purpose: Calculate customer risk score from policy data`

### Structure (REQUIRED)
**What:** Elements (inputs, outputs, attributes, keys) with types and roles
**Format:** `name (type): role - description`
**Example:**
```
Structure:
    customer_id (str): input - Unique customer identifier
    risk_score (float): output - Risk score 0.0-1.0
```

### Relationships (REQUIRED if code interacts with other assets)
**What:** What this consumes (reads/calls/imports) and produces (writes/returns/creates)
**Format:** `Consumes: asset.element, asset.element` / `Produces: asset.element`
**Example:**
```
Relationships:
    Consumes: customers.customer_id, policies.policy_count
    Produces: customer_360.risk_score
```

---

## Optional Sections

### Semantics (for business logic)
**What:** Business domain, entity, and logic rules
**Format:** `Domain: name` / `Entity: name` / `Logic: [rule1, rule2]`
**Example:**
```
Semantics:
    Domain: underwriting
    Entity: Customer
    Logic: [Higher policy count = lower risk, Recent claims = higher risk]
```

### Flow (if 3+ steps)
**What:** High-level algorithm steps
**Format:** Numbered list
**Example:**
```
Flow:
    1. Validate input
    2. Query database
    3. Calculate score
    4. Return result
```

### Parameters (if function has parameters)
**What:** Each parameter's purpose
**Format:** `name (type): description`
**Example:** `skill_name (str): Name of skill to retrieve. Must match directory name.`

### Returns (if function returns)
**What:** Return value and structure
**Format:** `type: description`
**Example:** `dict: Skill definition with 'instructions' and 'metadata' keys. None if not found.`

### Raises (if function throws exceptions)
**What:** Exceptions and conditions
**Format:** `ExceptionType: condition`
**Example:** `ValueError: If skill_name is empty or contains invalid characters`

### Important (for critical requirements)
**What:** Critical information that must not be ignored
**When:** Required for correct operation, breaking changes, mandatory constraints
**Example:** `stateless_http=True is REQUIRED for cloud deployments. Do not change to False.`

### Example (for non-trivial code)
**What:** Concrete usage
**Format:** Code showing call and result
**Example:** `>>> get_skill('post-implementation-review')`

### Note (for caveats)
**What:** Important limitations or considerations
**Example:** `This function blocks until server stops. Use in separate thread.`

---

## Language-Specific Syntax

### Python
Use docstrings: `"""..."""` or `'''...'''`

```python
def calculate_risk_score(customer_id: str, policy_data: dict) -> float:
    """
    Purpose: Calculate customer risk score from policy data

    Structure:
        customer_id (str): input - Customer identifier
        policy_data (dict): input - Policy details
        risk_score (float): output - Risk score 0.0-1.0

    Relationships:
        Consumes: customers.customer_id, policies.policy_count
        Produces: customer_360.risk_score

    Semantics:
        Domain: underwriting
        Entity: Customer
        Logic: [Higher policy count = lower risk]

    Flow:
        1. Validate customer_id
        2. Extract policy metrics
        3. Calculate score
        4. Return normalized score

    Args:
        customer_id: Customer identifier
        policy_data: Policy details

    Returns:
        Risk score 0.0-1.0

    Raises:
        ValueError: If customer_id is empty

    Important:
        policy_data MUST contain 'policy_count' and 'claim_count' keys.

    Example:
        >>> calculate_risk_score("C123", {"policy_count": 3, "claim_count": 0})
        0.75
    """
    # Implementation
```

**Minimal format:**
```python
def calculate_risk_score(customer_id: str, policy_data: dict) -> float:
    """
    Purpose: Calculate customer risk score from policy data

    Structure:
        customer_id (str): input
        policy_data (dict): input
        risk_score (float): output

    Relationships:
        Consumes: customers, policies
        Produces: customer_360.risk_score
    """
    # Implementation
```

### Terraform
Use block comments: `/* ... */`

```hcl
/*
Purpose: Create S3 bucket for customer data storage

Structure:
    bucket_name (var): input - Unique bucket name
    environment (var): input - Environment tag
    bucket_id (output): output - Created bucket ID

Relationships:
    Produces: aws_s3_bucket.customer_data
    Consumes: var.bucket_name, var.environment

Semantics:
    Domain: storage
    Entity: CustomerDataBucket
    Logic: [Versioning enabled, Encryption required]

Important:
    versioning MUST be enabled for compliance.
    encryption MUST use aws:kms for production.
*/
resource "aws_s3_bucket" "customer_data" {
  bucket = var.bucket_name

  versioning {
    enabled = true
  }
}
```

**Minimal format:**
```hcl
/*
Purpose: Create S3 bucket for customer data

Structure:
    bucket_name (var): input
    bucket_id (output): output

Relationships:
    Produces: aws_s3_bucket.customer_data
*/
resource "aws_s3_bucket" "customer_data" {
  bucket = var.bucket_name
}
```

### SQL
Use line comments `--` or block comments `/* ... */`

```sql
/*
Purpose: Create customer 360 view by joining customer and demographic data

Structure:
    customer_id (column): key - Customer identifier
    email (column): attribute - Customer email
    lifetime_value (column): output - Calculated value

Relationships:
    Consumes: customers.customer_id, customers.email, demographics.location
    Produces: customer_360 (all columns)

Semantics:
    Domain: customer
    Entity: Customer360
    Logic: [Lifetime value = policy_count × 1000, Filter test accounts]

Flow:
    1. Join customers with demographics
    2. Calculate lifetime_value
    3. Filter test accounts
    4. Insert into customer_360
*/
INSERT INTO customer_360
SELECT
    c.customer_id,
    c.email,
    (c.policy_count * 1000) AS lifetime_value
FROM customers c
JOIN demographics d ON c.customer_id = d.customer_id
WHERE c.email NOT LIKE '%test%';
```

**Minimal format:**
```sql
-- Purpose: Create customer 360 view
-- Structure: customer_id (key), email (attr), lifetime_value (output)
-- Relationships: Consumes customers, demographics; Produces customer_360
CREATE TABLE customer_360 AS
SELECT c.customer_id, c.email, (c.policy_count * 1000) AS lifetime_value
FROM customers c
JOIN demographics d ON c.customer_id = d.customer_id;
```

### TypeScript
Use JSDoc comments: `/** ... */`

```typescript
/**
 * Purpose: Fetch customer data from API with retry logic
 *
 * Structure:
 *     customerId (string): input - Customer identifier
 *     options (FetchOptions): input - Request options
 *     customerData (Customer): output - Customer object
 *
 * Relationships:
 *     Consumes: /api/customers/{id} (REST endpoint)
 *     Produces: Customer object
 *
 * Semantics:
 *     Domain: customer
 *     Entity: Customer
 *
 * Flow:
 *     1. Validate customerId
 *     2. Attempt API call
 *     3. Retry on failure (max 3)
 *     4. Parse response
 *     5. Return data
 *
 * @param customerId - Customer identifier
 * @param options - Request options
 * @returns Customer data object
 * @throws NetworkError if API unreachable after retries
 *
 * Important:
 *     Retry logic MUST use exponential backoff.
 *     Maximum 3 retry attempts to prevent rate limiting.
 *
 * @example
 * const customer = await fetchCustomer("C123", { timeout: 5000 });
 */
async function fetchCustomer(
  customerId: string,
  options: FetchOptions
): Promise<Customer> {
  // Implementation
}
```

### YAML
Use line comments: `#`

```yaml
# Purpose: Configure underwriting agent with customer data access
#
# Structure:
#     name (string): config - Agent identifier
#     model (string): config - LLM model name
#     resources (array): input - Data resources
#     tools (array): input - Functions
#
# Relationships:
#     Consumes: customer_data, policy_rules, calculate_risk_score
#     Produces: underwriting_decisions
#
# Semantics:
#     Domain: underwriting
#     Entity: UnderwritingAgent
#
# Important:
#     temperature MUST be 0.7 for consistent decisions.
#     resources MUST include customer_data for compliance.

agent:
  name: underwriting-agent
  model: claude-sonnet-4
  temperature: 0.7

  resources:
    - customer_data
    - policy_rules

  tools:
    - calculate_risk_score
    - validate_policy
```

---

## Constraints

**You MUST:**
- Include Purpose for all code elements
- Include Structure for all code elements with inputs/outputs/attributes
- Include Relationships if code interacts with other assets
- Use minimal words (see Documentation Principles)
- Use language-specific comment syntax
- Skip test files by default (notify user if skipping)

**You SHOULD:**
- Include Semantics for business logic
- Include Flow if 3+ steps
- Include Important for critical requirements
- Include Example for non-trivial code

**You MUST NOT:**
- Document implementation details (code shows this)
- Document obvious information (adds no value)
- Document future plans (document current state only)
- Repeat type information already in signatures
- Use vague terms like "handles", "processes", "manages"
- Document test files unless explicitly requested

**Test Files:**
Skip documentation for test files by default. Notify user when skipping.
Test file patterns: `*_test.py`, `test_*.py`, `*.test.ts`, `*.spec.ts`, `*_spec.rb`, files in `tests/`, `test/`, `__tests__/`, `spec/` directories.
Only document tests if user explicitly requests: "document test files" or "include tests".

---

## Before You Start

**Ask user:**
"Are there additional sources I should review for Important information? (design docs, ADRs, migration guides, security policies, deployment requirements)"

**Default source:** Current conversation history and code changes

# 0x00. Personal Data

This repository contains the materials and exercises for the "0x00. Personal Data" class in the ALX program. This class focuses on understanding and protecting Personally Identifiable Information (PII).

## Objectives
- Understand what constitutes Personally Identifiable Information (PII).
- Learn how to protect PII through obfuscation and encryption.
- Implement secure password handling.
- Securely authenticate to a database using environment variables.

## Table of Contents
1. [Examples of Personally Identifiable Information (PII)](#examples-of-personally-identifiable-information-pii)
2. [How to Implement a Log Filter that will Obfuscate PII Fields](#how-to-implement-a-log-filter-that-will-obfuscate-pii-fields)
3. [How to Encrypt a Password and Check the Validity of an Input Password](#how-to-encrypt-a-password-and-check-the-validity-of-an-input-password)
4. [How to Authenticate to a Database Using Environment Variables](#how-to-authenticate-to-a-database-using-environment-variables)

## Examples of Personally Identifiable Information (PII)
PII is information that can be used on its own or with other information to identify, contact, or locate a single person. Common examples include:
- Full Name
- Social Security Number (SSN)
- Driver's License Number
- Passport Number
- Email Address
- Phone Number
- Home Address
- Date of Birth
- Credit Card Information
- Health Records

## How to Implement a Log Filter that will Obfuscate PII Fields
### Importance of Log Filtering
Logs can contain sensitive information; it is crucial to obfuscate PII to protect privacy.

### Techniques
- **Regex Matching**: Identify PII patterns using regular expressions.
- **Obfuscation Methods**:
  - Masking: Replace parts of the data with asterisks or other characters.
  - Redaction: Completely remove sensitive data from the logs.

### Implementation Example (Python)
```python
import re

def obfuscate_pii(log: str) -> str:
    patterns = {
        'email': r'[\w\.-]+@[\w\.-]+',
        'phone': r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    }
    for key, pattern in patterns.items():
        log = re.sub(pattern, '[REDACTED]', log)
    return log

log_entry = "User email: user@example.com, phone: 123-456-7890"
obfuscated_log = obfuscate_pii(log_entry)
print(obfuscated_log)


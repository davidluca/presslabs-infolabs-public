# Project API

# Group overview
## Propose
Simple REST API for creating checks for domains and get detailed report about that check.
## HTTP methods
 * `GET` - **Retrieve** a representation of the report status
 * `POST` - **Create** a new check for the domain.

## Possible responses
Depending on the request being made, you can get:
 * `200` - The request has been successfully performed
 * `201` - The resource has been successfully created
 * `400` - The request body contains attributes that does not know how to be handled
 * `401` - The request requires authentication
 * `404` - Can not find the requested resource

## Resources/Entities
The entities that can be observed through the API endpoints are the following:
 * **Report** - The representation of the report model, that contains all the features that are analyzed.G
 * **Feature** - The representation of the analyzed feature of the domain.

# Group Report/DomainCheck
From this endpoint you can create a domain check(report) which is initially in `pending` state, or you can
get the state and results of a report. Also listing will be available.

## Report List [/check/]
## Create a new check [POST]
+ Request (application/json)
   + Attributes (CheckPost)
+ Response 201 (application/json)
   + Headers
           Location: /check/1
+ Response 400 (application/json)
   + Body
      {"domain": "This field is required."}

## Retrieve report [/check/{id}]
+ Parameters
  + id - The report id

## List all reports [GET]
+ Request (application/json) 
+ Response 200 (application/json)
   + Attributes (array[ReportObj])
+ Response 401 (application/json)
   + Attributes (AuthenticationRequired)
    

# Group Features
From this endpoint you can get the features values.

## Retrieve feature [/feature/{id}/]
+ Parameters
  + id - The feature id

### Retrieve a feature [GET]
+ Request (application/json)
+ Response 200 (application/json)
   + Attributes (FeatureObj)
+ Response 404 (application/json)
   + Attributes (ResourceNotFound)

# Data Structures
## CheckPost (object)
 - domain: `www.example.com` (string, required) - Domain which will be analyzed.

## ReportObj (object)
 - domain: `www.example.com ` (string) The domain for which the report is made.
 - state: `pending` (string) The report state. This can be `pending` or `finished`
 - created_at: `2017-04-19T22:44:50.985576` (string) The date-time when the check was created.
 - features: `http://api.info.com/feature/1`, `http://api.info.com/feature/2` (array[string]) List of features URL.
 
## FeatureObj (object)
 - name: `response_time` (string) The feature name
 - value: `234ms` (string) The value for this features. This can be a json object.
 - compare_value: `210ms` (string) What we can offer for this feature.
 - report: `http://api.info.com/check/1` (string) The check URL.

## ResourceNotFound (object)
- message: `Requested resource not found` (string)

## AuthenticationRequired (object)
- message: `Authentication is required for this operation` (string)

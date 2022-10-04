/*
Models corresponding to https://languagetool.org/http-api/swagger-ui/#!/default/post_check
Used for deserializing JSON responses from the Language tool API.
*/

#[derive(Debug, Deserialize)]
struct check_response {
    software: Option<software>,
    warnings: Option<warnings>,
    language: Option<language>,
    matches: Option<Vec<matches>>,
    sentenceRanges: Option<Vec<Vec<i32>>>,
}

// Inline model 1
#[derive(Debug, Deserialize)]
struct software {
    name: String,
    version: String,
    buildDate: String,
    apiVersion: i32,
    status: Option<String>,
    premium: Option<bool>,
}

// Inline model 2
#[derive(Debug, Deserialize)]
struct language {
    name: String,
    code: String,
    detectedLanguage: detectedLanguage,
}

// Inline model 3
#[derive(Debug, Deserialize)]
struct matches {
    message: String,
    shortMessage: Option<String>,
    offset: i32,
    length: i32,
    replacements: Vec<replacements>,
    context: context,
    sentence: String,
    rule: Option<rule>,
}

// Inline model 4
#[derive(Debug, Deserialize)]
struct detectedLanguage {
    name: String,
    code: String,
}

// Inline model 5
#[derive(Debug, Deserialize)]
struct replacements {
    value: Option<String>,
}

// Inline model 6
#[derive(Debug, Deserialize)]
struct context {
    text: String,
    offset: i32,
    length: i32,
}

// Inline model 7
#[derive(Debug, Deserialize)]
struct rule {
    id: String,
    subId: Option<String>,
    description: String,
    urls: Option<Vec<urls>>,
    issueType: Option<String>,
    category: category,
}

// Inline model 8
#[derive(Debug, Deserialize)]
struct urls {
    value: Option<String>,
}

// Inline model 9
#[derive(Debug, Deserialize)]
struct category {
    id: Option<String>,
    name: Option<String>,
}


// N.B. does not exist in the docs
#[derive(Debug, Deserialize)]
struct warnings {
    incompleteResults: Option<bool>,
}

// N.B. does not exist in the docs
#[derive(Debug, Deserialize)]
struct sentenceRanges {
    sentenceRanges: Option<Vec<Vec<i32>>>,
}
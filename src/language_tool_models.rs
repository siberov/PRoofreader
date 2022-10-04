#![allow(non_snake_case)]
#![allow(non_camel_case_types)]
use serde::Deserialize;
/*
Models corresponding to https://languagetool.org/http-api/swagger-ui/#!/default/post_check
Used for deserializing JSON responses from the Language tool API.
*/

#[derive(Debug, Deserialize)]
pub struct check_response {
    pub software: Option<software>,
    pub warnings: Option<warnings>,
    pub language: Option<language>,
    pub matches: Option<Vec<matches>>,
    pub sentenceRanges: Option<Vec<Vec<i32>>>,
}

// Inline model 1
#[derive(Debug, Deserialize)]
pub struct software {
    pub name: String,
    pub version: String,
    pub buildDate: String,
    pub apiVersion: i32,
    pub status: Option<String>,
    pub premium: Option<bool>,
}

// Inline model 2
#[derive(Debug, Deserialize)]
pub struct language {
    pub name: String,
    pub code: String,
    pub detectedLanguage: detectedLanguage,
}

// Inline model 3
#[derive(Debug, Deserialize)]
pub struct matches {
    pub message: String,
    pub shortMessage: Option<String>,
    pub offset: i32,
    pub length: i32,
    pub replacements: Vec<replacements>,
    pub context: context,
    pub sentence: String,
    pub rule: Option<rule>,
}

// Inline model 4
#[derive(Debug, Deserialize)]
pub struct detectedLanguage {
    pub name: String,
    pub code: String,
}

// Inline model 5
#[derive(Debug, Deserialize)]
pub struct replacements {
    pub value: Option<String>,
    pub shortDescription: Option<String>,
}

// Inline model 6
#[derive(Debug, Deserialize)]
pub struct context {
    pub text: String,
    pub offset: i32,
    pub length: i32,
}

// Inline model 7
#[derive(Debug, Deserialize)]
pub struct rule {
    pub id: String,
    pub subId: Option<String>,
    pub description: String,
    pub urls: Option<Vec<urls>>,
    pub issueType: Option<String>,
    pub category: category,
}

// Inline model 8
#[derive(Debug, Deserialize)]
pub struct urls {
    pub value: Option<String>,
}

// Inline model 9
#[derive(Debug, Deserialize)]
pub struct category {
    pub id: Option<String>,
    pub name: Option<String>,
}


// N.B. does not exist in the docs
#[derive(Debug, Deserialize)]
pub struct warnings {
    pub incompleteResults: Option<bool>,
}

// N.B. does not exist in the docs
#[derive(Debug, Deserialize)]
pub struct sentenceRanges {
    pub sentenceRanges: Option<Vec<Vec<i32>>>,
}

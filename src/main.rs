use reqwest;

mod language_tool_models;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let language = "en";
    let text = "Hello world and Arvid Siberov and Vetenskapsmannen Linus!";
    let input = "language=".to_owned() + language + "&text=" + text;
    let client = reqwest::Client::new();
    let result = client
        .post("http://localhost:8010/v2/check")
        .body(input)
        .send()
        .await;
    let json: language_tool_models::check_response = result?.json().await?;

    println!("{:?}", json.software.ok_or("error"));
    Ok(())
}
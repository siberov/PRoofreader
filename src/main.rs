use reqwest;

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

    println!("{:?}", result?.text().await?);
    Ok(())
}
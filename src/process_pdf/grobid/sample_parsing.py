from pathlib import Path
from grobid_client.grobid_client import GrobidClient


def process_pdf_directory(
    input_dir: str = "samples/pdf",
    output_dir: str = "samples/parsed_result",
    server: str = "http://localhost:8070",
    n: int = 10,
) -> None:
    client = GrobidClient(grobid_server=server)
    client.process(
        service="processFulltextDocument",
        input_path=input_dir,
        output_path=output_dir,
        n=n,
    )


if __name__ == "__main__":
    process_pdf_directory()
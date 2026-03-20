from pathlib import Path
from typing import Sequence

from grobid_client.grobid_client import GrobidClient


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def _resolve_project_path(relative_path: str) -> Path:
    return (PROJECT_ROOT / relative_path).resolve()

def parse_fulltext(
    input_dir: str = "samples/pdf",
    output_dir: str = "samples/parsed_result",
    server: str = "http://localhost:8070",
    n: int = 10,
    coordinate_elements: Sequence[str] = ("ref", "biblStruct"),
    segment_sentences: bool = False,
) -> None:
    input_path = _resolve_project_path(input_dir)
    output_path = _resolve_project_path(output_dir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input directory not found: {input_path}")

    output_path.mkdir(parents=True, exist_ok=True)

    client = GrobidClient(
        grobid_server=server,
        coordinates=list(coordinate_elements),
    )
    client.process(
        service="processFulltextDocument",
        input_path=str(input_path),
        output=str(output_path),
        n=n,
        tei_coordinates=True,
        segment_sentences=segment_sentences,
    )



def parse_references(
    input_dir: str = "samples/pdf",
    output_dir: str = "samples/parsed_references",
    server: str = "http://localhost:8070",
    n: int = 10,
    consolidate_citations: bool = False,
    include_raw_citations: bool = True,
) -> None:
    input_path = _resolve_project_path(input_dir)
    output_path = _resolve_project_path(output_dir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input directory not found: {input_path}")

    output_path.mkdir(parents=True, exist_ok=True)

    client = GrobidClient(grobid_server=server)
    client.process(
        service="processReferences",
        input_path=str(input_path),
        output=str(output_path),
        n=n,
        consolidate_citations=consolidate_citations,
        include_raw_citations=include_raw_citations,
    )

def parse_header(
    input_dir: str = "samples/pdf",
    output_dir: str = "samples/parsed_header",
    server: str = "http://localhost:8070",
    n: int = 10,
    consolidate_header: bool = True,
) -> None:
    input_path = _resolve_project_path(input_dir)
    output_path = _resolve_project_path(output_dir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input directory not found: {input_path}")

    output_path.mkdir(parents=True, exist_ok=True)

    client = GrobidClient(grobid_server=server)
    client.process(
        service="processHeaderDocument",
        input_path=str(input_path),
        output=str(output_path),
        n=n,
        consolidate_header=consolidate_header,
    )

def parse_citation_list(
    input_dir: str = "samples/citations",
    output_dir: str = "samples/parsed_citations",
    server: str = "http://localhost:8070",
    n: int = 10,
    consolidate_citations: bool = False,
    include_raw_citations: bool = True,
) -> None:
    input_path = _resolve_project_path(input_dir)
    output_path = _resolve_project_path(output_dir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input directory not found: {input_path}")

    output_path.mkdir(parents=True, exist_ok=True)

    client = GrobidClient(grobid_server=server)
    client.process(
        service="processCitationList",
        input_path=str(input_path),
        output=str(output_path),
        n=n,
        consolidate_citations=consolidate_citations,
        include_raw_citations=include_raw_citations,
    )


def parse_all(
    input_dir: str = "samples/pdf",
    fulltext_output_dir: str = "samples/parsed_result",
    header_output_dir: str = "samples/parsed_header",
    citation_input_dir: str = "samples/citations",
    references_output_dir: str = "samples/parsed_references",
    citation_output_dir: str = "samples/parsed_citations",
    server: str = "http://localhost:8070",
    n: int = 10,
    coordinate_elements: Sequence[str] = ("ref", "biblStruct"),
    segment_sentences: bool = False,
    consolidate_header: bool = True,
    consolidate_citations: bool = False,
) -> None:

    parse_fulltext(
        input_dir=input_dir,
        output_dir=fulltext_output_dir,
        server=server,
        n=n,
        coordinate_elements=coordinate_elements,
        segment_sentences=segment_sentences,
    )

    parse_header(
        input_dir=input_dir,
        output_dir=header_output_dir,
        server=server,
        n=n,
        consolidate_header=consolidate_header,
    )

    parse_references(
        input_dir=input_dir,
        output_dir=references_output_dir,
        server=server,
        n=n,
        consolidate_citations=consolidate_citations,
    )
    citation_input_path = _resolve_project_path(citation_input_dir)
    if citation_input_path.exists():
        parse_citation_list(
            input_dir=citation_input_dir,
            output_dir=citation_output_dir,
            server=server,
            n=n,
            consolidate_citations=consolidate_citations,
        )


if __name__ == "__main__":
    parse_all()
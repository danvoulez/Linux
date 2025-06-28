import subprocess

def test_sbom_generator(tmp_path):
    result = subprocess.check_output(['./compliance/sbom_generator.py'])
    assert b"SBOM" in result

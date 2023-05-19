$files_to_check_matera = @(
    "mat_Cadoc.csv",
    "mat_CC.csv",
    "mat_CC_acumulativo.csv",
    "mat_CC_ANUAL.csv",
    "mat_CC_atual.csv",
    "mat_Vers_Matera.csv"
)

foreach ($file in $files_to_check_matera) {
    Write-Output "Header1,Header2,Header3" > $file
}
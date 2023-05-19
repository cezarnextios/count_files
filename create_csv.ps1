$files_to_check_matera = @(
    "cart_baseiof.csv",
    "cart_plan_camp.csv",
    "cart_rot_combinado.csv",
    "cart_saldodevmin.csv",
    "CartoesPAGTOMIN.csv",
    "CartoesREGRACAMPANHA.csv",
    "Cartoestxcamp.csv"
)

foreach ($file in $files_to_check_matera) {
    Write-Output "Header1,Header2,Header3" > $file
}
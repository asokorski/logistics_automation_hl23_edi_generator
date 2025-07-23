dynamic_items_query = """
SELECT DISTINCT
    hlartip.arcart                               AS "Item_code",
    hlcdfap.a2cfar                               AS "Brand"
FROM
    DE_NL_PRD.hlartip
    LEFT JOIN DE_NL_PRD.hlcdfap ON hlartip.arcart = hlcdfap.a2cart
    LEFT JOIN DE_NL_PRD.hlafpdp ON hlafpdp.aycart = hlartip.arcart
WHERE
    hlafpdp.aycfpd IS NULL
    AND hlcdfap.a2cfar IS NOT NULL
"""
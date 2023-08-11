import sys

# def find_gene(input_file1, input_file2, output_file):
snp_dict = {}
gff_dict = {}
geneset_list = []
with open("D:/snp/snpfile.txt", "r") as snp_origin_file:
    snp_list = snp_origin_file.readlines()
    for list in snp_list:
        snp_id = list.split("\t")[0]
        snp_chr = list.split("\t")[1]
        snp_pos = int(list.strip("\n").split("\t")[2])
        snp_dict[snp_id] = (snp_chr, snp_pos)

with open("D:/snp/ZhongmuNo.1.gff", "r") as gff_file:
    list_gff = gff_file.readlines()
    for list in list_gff:
        gff = list.split("\t")
        if gff[2] == "gene":
            gff_chr = gff[0]
            gff_start = int(gff[3])
            gff_end = int(gff[4])
            gff_geneid = gff[8]
            gff_dict[gff_geneid] = (gff_chr, gff_start, gff_end)

for k_snp, v_snp in snp_dict.items():
    snp_chr1, snp_pos1 = snp_dict[k_snp]
    snp_up = snp_pos1 - 100000
    snp_down = snp_pos1 + 100000
    for k_gff, v_gff in gff_dict.items():
        gene_id1 = k_gff
        gff_chr1, gff_start1, gff_end1 = gff_dict[k_gff]
        if snp_chr1 == gff_chr1[3]:
            if gff_start1 < snp_up and gff_end1 > snp_up:
                geneset_list.append((gff_chr1,str(gff_start1),str(gff_end1),gene_id1))
            elif snp_up < gff_start1 and gff_end1 < snp_down:
                geneset_list.append((gff_chr1,str(gff_start1),str(gff_end1),gene_id1))
            elif gff_start1 < snp_down and snp_down < gff_end1:
                geneset_list.append((gff_chr1,str(gff_start1),str(gff_end1),gene_id1))

with open("D:/snp/geneid.txt", "w") as w:
    for li in geneset_list:
        list = ",".join(li)
        w.write(list+"\n")



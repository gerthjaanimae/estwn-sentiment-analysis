senti=read.csv("senti-estwn.csv", sep="\t", fileEncoding="UTF-8")
#senti$obj_skoor=1-senti$pos_skoor -senti$neg_skoor
#senti=senti[,c("sonaliik", "identifikaator", "pos_skoor", "neg_skoor", "obj_skoor", "sonad", "naited")]
#head(senti)
neutr=senti[senti$pos_skoor < 0.1 & senti$neg_skoor < 0.1,]
vastuolu=senti[senti$pos_skoor > 0.1 & senti$neg_skoor > 0.1,]
tpos=senti[senti$pos_skoor > 0.25 & senti$neg_skoor < 0.1,]
mpos=senti[senti$pos_skoor >= 0.1 & senti$pos_skoor <= 0.25 & senti$neg_skoor < 0.1,]
tneg=senti[senti$pos_skoor < 0.1 & senti$neg_skoor > 0.25,]
mneg=senti[senti$pos_skoor < 0.1 & senti$neg_skoor <= 0.25 & senti$neg_skoor >= 0.1,]
#neutr=neutr[order(-neutr$obj_skoor),]
tpos=tpos[order(-tpos$pos_skoor),]
mpos=mpos[order(-mpos$pos_skoor),]
tneg=tneg[order(-tneg$neg_skoor),]
mneg=mneg[order(-mneg$neg_skoor),]
vastuolu=vastuolu[order(-vastuolu$pos_skoor),]
write.table(neutr, "neutraalsed.csv", quote=FALSE, sep="\t", fileEncoding="utf-8", row.names=FALSE)
jpeg('neutraalsed.jpg')
plot((1-neutr$neg_skoor-neutr$pos_skoor), type="o", col="blue")
dev.off()
write.table(tpos, "tugevalt-positiivsed.csv", quote=FALSE, sep="\t", fileEncoding="UTF-8", row.names=FALSE)
jpeg('tugevalt-positiivsed.jpg')
plot(tpos$pos_skoor, type="o", col="blue")
dev.off()
write.table(mpos, "moodukalt-positiivsed.csv", quote=FALSE, sep="\t", fileEncoding="UTF-8", row.names=FALSE)
jpeg('moodukalt-positiivsed.jpg')
plot(mpos$pos_skoor, type="o", col="blue")
dev.off()

write.table(tneg, "tugevalt-negatiivsed.csv", quote=FALSE, sep="\t", fileEncoding="UTF-8", row.names=FALSE)
jpeg('tugevalt-negatiivsed.jpg')
plot(tneg$neg_skoor, type="o", col="blue")
dev.off()

write.table(mneg, "moodukalt-negatiivsed.csv", quote=FALSE, sep="\t", fileEncoding="UTF-8", row.names=FALSE)
jpeg('moodukalt-negatiivsed.jpg')
plot(mneg$neg_skoor, type="o", col="blue")
dev.off()

write.table(vastuolu, "vastuolulised.csv", quote=FALSE, sep="\t", fileEncoding="UTF-8", row.names=FALSE)
jpeg('vastuolulised.jpg')
plot(vastuolu$neg_skoor, vastuolu$pos_skoor, type="o", col="blue")
dev.off()
jpeg("kõik.jpg")
plot(senti$pos_skoor, senti$neg_skoor, type="o", col="blue")
dev.off()

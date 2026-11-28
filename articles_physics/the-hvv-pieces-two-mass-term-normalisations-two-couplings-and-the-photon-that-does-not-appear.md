# __The $hVV$ Pieces: Two Mass-Term Normalisations, Two Couplings, and the Photon That Does Not Appear__

## Introduction

**The claim.** The list has two pieces in which the scalar multiplies a pair of vectors,

$$
\mathcal{L}_{hVV}=-\frac{g^2v}{2}\,h\,W^+_\mu W^{-\mu}-\frac{(g^2+g_{\mathrm Y}^2)v}{4}\,h\,Z_\mu Z^\mu .
$$

The two coefficients are $2M_W^2/v$ and $M_Z^2/v$, and the factor of two between them is the one this article is about. Written with the conventional $\tfrac12$ in front of the $ZZ$ term the second reads $g_{hZZ}=2M_Z^2/v$. There is no $hAA$ piece and no $h\gamma Z$ piece at tree level.

**The answer.**

$$
\boxed{\;\Bigl[\,hW^+W^-\,\Bigr]=\frac{2M_W^2}{v},\qquad \Bigl[\,hZZ\,\Bigr]=\frac{M_Z^2}{v},\qquad \frac{[hW^+W^-]}{[hZZ]}=\frac{2M_W^2}{M_Z^2}=2\cos^2\theta_W\;}
$$

**Why the two coefficients look unequal in one reading and equal in the other.** This is the one place in the category where a normalisation convention creates an apparent physical discrepancy. Writing the $ZZ$ term with the conventional $\tfrac12$ puts a factor of two into the coupling, so both couplings read $2M_V^2/v$; writing it without the $\tfrac12$ takes the factor out, so the coefficients read $2$ and $1$. The corpus uses the first convention, and the section below separates the convention from the physics.

**The standing.** Both pieces are standard and the corpus's own table is [Electroweak Symmetry Breaking](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html), which prints $g_{hWW}=2M_W^2/v$ and $g_{hZZ}=2M_Z^2/v$. This article derives both from one line and shows why the photon is absent.

## The One Line They Come From

**The scalar kinetic term in the unitary chart.**

$$
-\sum_\mu(D_\mu H)^\dagger(D_\mu H)\supset-\frac{(v+h)^2}{8}\Bigl[g^2(W_1^2+W_2^2)+(gW_3-g_{\mathrm Y}B)^2\Bigr] .
$$

**The linear level of the square.** Writing $(v+h)^2=v^2+2vh+h^2$ and keeping the $2vh$ term,

$$
-\frac{vh}{4}\Bigl[2g^2W^+_\mu W^{-\mu}+(g^2+g_{\mathrm Y}^2)Z_\mu Z^\mu\Bigr],
$$

where $W_1^2+W_2^2=2W^+W^-$ and $(gW_3-g_{\mathrm Y}B)^2=(g^2+g_{\mathrm Y}^2)Z^2$ have been used.

**Reading off the two couplings.** The charged piece is $-\frac{g^2v}{2}hW^+W^-$, so with the convention $\mathcal{L}\supset-g_{hWW}hW^+W^-$ the coupling is $g^2v/2$. The neutral piece is $-\frac{(g^2+g_{\mathrm Y}^2)v}{4}hZ^2$, so with the convention $\mathcal{L}\supset-\frac12g_{hZZ}hZ^2$ the coupling is $\frac{(g^2+g_{\mathrm Y}^2)v}{2}$.

**Both are $2M_V^2/v$, and the arithmetic is one line each.**

$$
\frac{g^2v}{2}=2\,\frac{g^2v^2}{4v}=\frac{2M_W^2}{v},
\qquad
\frac{(g^2+g_{\mathrm Y}^2)v}{2}=2\,\frac{(g^2+g_{\mathrm Y}^2)v^2}{4v}=\frac{2M_Z^2}{v} .
$$

## The Convention That Creates the Appearance of a Discrepancy

**Two ways of writing one vertex.** For a real field the vertex from $\frac12c\,hZ_\mu Z_\nu$ is $ic\,g_{\mu\nu}$, and the vertex from $c'\,hZ_\mu Z_\nu$ is $2ic'g_{\mu\nu}$. The same Lagrangian term therefore carries a coupling that differs by a factor of two between the two conventions.

**The two normalisations, stated once and kept apart.**

| Reading | $hW^+W^-$ | $hZZ$ |
|---|---|---|
| coefficient in $\mathcal{L}$ | $2M_W^2/v$ | $M_Z^2/v$ |
| coupling with $\tfrac12$ in $\mathcal{L}$ | $2M_W^2/v$ | $2M_Z^2/v$ |

The charged row has no $\tfrac12$ because $W^+$ and $W^-$ are distinct fields, so the two ways of writing it coincide. The neutral row has one because $Z$ is its own conjugate, so the $\tfrac12$ convention and the coefficient convention differ by two.

**Why the W's coefficient is twice the Z's.** In units of $M^2/v$ the two coefficients are $2$ and $1$. That is the factor of two this article's title names: it is not a discrepancy but the statement that the charged pair contributes two real fields to the square and the $Z$ contributes one.

**The physical statement, in either reading.** The coefficients are $2M_W^2/v$ and $M_Z^2/v$; the $\tfrac12$-normalised couplings are twice each mass squared over $v$; and the two readings are the same Lagrangian.

## Why the Photon Does Not Appear

**The charge of the vacuum is zero.** The combinations in the square are $W_1^2+W_2^2$ and $(gW_3-g_{\mathrm Y}B)^2$. The photon is the orthogonal combination $A=\sin\theta_WW_3+\cos\theta_WB$, and the mass matrix has $A$ as its null direction. A term $h\,A_\mu A^\mu$ would require the vacuum to carry charge, which it does not.

**No $h\gamma Z$ either.** The neutral mass matrix is rank one: it is the outer product of one vector with itself. A rank-one matrix has no off-diagonal term between its eigenvector and its null direction, so the mixed piece is absent for the same reason that the photon mass is absent.

**What this predicts.** The $h\gamma\gamma$ and $h\gamma Z$ vertices exist at one loop and not at tree level. The tree-level zeros are pieces of the list; the loop-induced vertices are not, because the list is the tree-level Lagrangian.

## The Ratio and the $\rho$ Variable

**One ratio, two readings.**

$$
\frac{[hW^+W^-]}{[hZZ]}=\frac{2M_W^2}{M_Z^2}=2\cos^2\theta_W,\qquad
\frac{g_{hWW}}{g_{hZZ}}=\frac{M_W^2}{M_Z^2}=\cos^2\theta_W .
$$

The first compares the coefficients in $\mathcal{L}$; the second compares the $\tfrac12$-normalised couplings. They differ by the factor of two of the neutral row, and each is $\rho\cos^2\theta_W$ with $\rho=1$ once the comparison is made at the same level.

**Why the custodial relation appears twice.** The ratio of the couplings is the ratio of the masses squared, and the ratio of the masses is the statement $\rho=1$ of [Custodial Symmetry and the Rho Parameter](custodial-symmetry-and-the-rho-parameter.html). The two statements are one, seen on the mass pieces and on the couplings.

**What a deviation would mean.** A scalar multiplet with a different isospin would change both the ratio of the masses and the ratio of the couplings, and it would do so by the same factor. The measurement of the two $hVV$ couplings is therefore a second, independent measurement of $\rho$.

## Checks

1. The count. Two rows, the seventh and eighth of the forty-seven.
2. The coefficients. $g^2v/2=2M_W^2/v$ and $(g^2+g_{\mathrm Y}^2)v/4=M_Z^2/v$.
3. The dimension. $hVV$ has dimension $1+1+1=3$, and the coefficient carries the missing unit.
4. The ratio. $M_W^2/M_Z^2=\cos^2\theta_W$, from $M_Z=M_W/\cos\theta_W$.
5. The photon. The mass matrix's null direction receives no piece, so neither $hAA$ nor $hAZ$ appears.
6. The convention. $\frac12c\,hZ^2$ gives $icg_{\mu\nu}$ and $c'\,hZ^2$ gives $2ic'g_{\mu\nu}$, so the factor of two is the $\tfrac12$.
7. The proportionality. $g_{hVV}=2M_V^2/v$, and the same $v$ as in the mass relation.
8. The common origin. Both pieces are the linear level of $(v+h)^2$, as [The Unitary-Gauge Image](the-unitary-gauge-image-the-lineage-of-every-piece-and-where-the-three-goldstones-went.html) tabulates.
9. The loop statement. $h\gamma\gamma$ and $h\gamma Z$ are absent at tree level and present at one loop, so their absence here is a statement about the order of the expansion.
10. The corpus's table. $g_{hWW}=2M_W^2/v$ and $g_{hZZ}=2M_Z^2/v$ in [Electroweak Symmetry Breaking](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html): the second is the $\tfrac12$-normalised coupling, and its coefficient is $M_Z^2/v$.

## Summary

The two $hVV$ rows are $-\frac{g^2v}{2}hW^+W^-$ and $-\frac{(g^2+g_{\mathrm Y}^2)v}{4}hZZ$. They come from the linear level of the square $(v+h)^2$ in the scalar kinetic term, and their coefficients are $2M_W^2/v$ and $M_Z^2/v$ — the second equal to $g_{hZZ}/2$ in the $\tfrac12$ convention.

The apparent factor of two between the two couplings is a convention. The vertex from a term with $\tfrac12$ in front of $hZ^2$ carries twice the coefficient of a term without it, and the corpus writes the vertex coupling. The ratio $M_W^2/M_Z^2=\cos^2\theta_W$ is the same in either convention.

The photon does not appear, and neither does the $h\gamma Z$ piece. The neutral mass matrix is rank one, and its null direction is the photon; a coupling of the scalar to that direction would require the vacuum to carry charge.

The ratio of the two couplings is the ratio of the two masses squared, which is the custodial relation $\rho=1$ seen on a second set of pieces. A measurement of the two couplings is a measurement of $\rho$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g_{hWW}$, $g_{hZZ}$ | The $\tfrac12$-normalised couplings, $2M_W^2/v$ and $2M_Z^2/v$ |
| $\mathcal{L}_{hVV}$ | The two pieces |
| $v$ | The vacuum value, the same as in the mass relations |
| $\rho$ | $M_W^2/(M_Z^2\cos^2\theta_W)$ |
| $A$ | The photon, the null direction of the neutral mass matrix |

## Further Reading

- [Electroweak Symmetry Breaking: the Doublet, the Potential and the Vector-Boson Masses](electroweak-symmetry-breaking-the-doublet-the-potential-and-the-vector-boson-masses.html). The expansion and the corpus's table of couplings.
- [The Two Vector Masses](the-two-vector-masses-proca-as-the-representative-of-the-condensate.html). The constant level of the same square.
- [The Higgs Kinetic and Mass Pieces](the-higgs-kinetic-and-mass-pieces-and-the-tadpole-condition-that-fixes-v.html). The scalar's own three rows among the six the square produces.
- [Custodial Symmetry and the Rho Parameter](custodial-symmetry-and-the-rho-parameter.html). The ratio, twice.
- [The Lagrangian and the Higgs Field](the-lagrangian-and-the-higgs-field.html). The potential and the radial variable in the corpus's variables.

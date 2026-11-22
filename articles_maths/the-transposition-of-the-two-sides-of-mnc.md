# __The Transposition of the Two Sides of $M_n(\mathbb{C})$__

## Introduction

**The question.** What happens to a two-sided operator $T_{A,B}$ under the transpose of the carrier, and can the left and the right sides be exchanged?

**The answer in one line.** Conjugation by the transpose operator $F(X)=X^{\mathsf T}$ swaps the two sides and transposes both parameters,
$$
FT_{A,B}F=T_{B^{\mathsf T},A^{\mathsf T}},
$$
and no element of the algebra and no single product does the same.

**Why the article is needed.** In the biquaternion series the exchange of the two sides was written with one matrix, because the transpose of the coefficient frame is a conjugation and the frame is $4\times4$. At general $n$ the exchange still exists, but as an operator that is outside the one-sided span and outside the two-sided family. Separating the operator from the element is the point.

**Boundaries.** The families are *The Endomorphisms of $M_n(\mathbb{C})$*; the adjoints are *The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*; the enveloping algebra is *The Enveloping Operator Algebra of $M_n(\mathbb{C})$ and the Bi-module Structure*. The biquaternion original is *The Transposition of the Two Sides*.

**Conventions.** $F(X)=X^{\mathsf T}$, so $F^2=\mathrm I$. The three involutions of the operator layer are
$$
F T F,\qquad T^{\dagger}\ (\text{Hilbert–Schmidt}),\qquad T^{\mathsf T}\ (\text{transposed bilinear form}).
$$

## The Three Transposes

**The table.** For a single product the three operations give

| operation | result | effect on the parameters |
|---|---|---|
| $FTF$ | $T_{B^{\mathsf T},A^{\mathsf T}}$ | swaps the slots and transposes both |
| $T^{\dagger}$ | $T_{A^{*},B^{*}}$ | no swap, conjugate transpose both |
| $T^{\mathsf T}$ | $T_{A^{\mathsf T},B^{\mathsf T}}$ | no swap, transpose both |

**Proposition.** $FT_{A,B}F=T_{B^{\mathsf T},A^{\mathsf T}}$.

*Proof.* $(FT_{A,B}FX)_{ij}$ is the $(i,j)$ entry of $(AX^{\mathsf T}B)^{\mathsf T}$, which is $(B^{\mathsf T}XA^{\mathsf T})_{ij}$. $\square$

**The reading.** The bilinear transpose $T\mapsto T^{\mathsf T}$ never moves a parameter from one slot to the other. Conjugation by $F$ always does. The two agree only when $A$ and $B$ are symmetric and equal, in which case both fix $T_{A,A}$.

**The adjoint pair.** $F$ is self-adjoint and unitary for the Hilbert–Schmidt form, so $FTF$ is unitarily equivalent to $T$. Conjugation by $F$ is therefore an automorphism of the operator algebra of order two, and it is the outer symmetry that the one-sided families lack.

## Exchanging the Sides

**Proposition (the operator does it).** $FL_AF=R_{A^{\mathsf T}}$ and $FR_BF=L_{B^{\mathsf T}}$.

*Proof.* The first is the case $B=\mathrm I$ of the formula above: $FT_{A,\mathrm I}F=T_{\mathrm I,A^{\mathsf T}}=R_{A^{\mathsf T}}$. The second follows by applying the first to $F^2=\mathrm I$. $\square$

**Proposition (no element of the algebra does it).** There is no $D\in M_n$ with $DR_AD^{-1}=L_A$ for all $A$, unless $n=1$.

*Proof.* The identity reads $DXA=ADX$ for all $X$. At $X=\mathrm I$ it gives $DA=AD$; substituting back gives $(DX)A=A(DX)$ for every $X$, so $DX$ is central for every $X$, hence $D$ is scalar. A scalar gives $R_A=L_A$, false. $\square$

**Proposition (no single product does it).** There is no pair $(P,Q)$ with $T_{P,Q}L_AT_{P,Q}^{-1}=L_A$ for all $A$.

*Proof.* $T_{P,Q}L_AT_{Q^{-1},P^{-1}}=T_{PAQ,Q^{-1}P^{-1}}$, which equals $L_A$ only if $Q^{-1}P^{-1}=\mathrm I$ and $PAQ=A$ for all $A$. The first gives $PQ=\mathrm I$; the second then forces $P$ and $Q$ to be scalars, and again $R_A=L_A$. $\square$

**The moral.** The exchange is a genuinely operator-level symmetry. It is not inner, at any $n\ge2$. At $n=2$ it has a familiar matrix because the transpose of the coefficient frame is the quaternion conjugation, which the biquaternion series already wrote down; the existence of that matrix is not an accident of small $n$, but its interpretation as an element of the algebra is.

## The Flip Is Outside the One-Sided Span

**Proposition.** $F\notin\operatorname{span}\{L_A,R_B\}$ for $n\ge2$.

*Proof.* Suppose $F=L_A+R_B$, so $X^{\mathsf T}=AX+XB$ for all $X$. At $X=\mathrm I$ this gives $A+B=\mathrm I$. At $X=E_{ij}$ the $(k,l)$ entry is $\delta_{ki}\delta_{lj}$ on the left and $A_{ki}\delta_{lj}+\delta_{ki}B_{lj}$ on the right. Taking $k=i$ and $l=j$ gives $A_{ii}+B_{jj}=1$. Taking $k=i$ and $l\neq j$ gives $B_{lj}=0$, so $B$ is diagonal; taking $k\neq i$ and $l=j$ gives $A_{ki}=0$, so $A$ is diagonal. Then $A_{ii}+B_{jj}=1$ for all $i,j$, so $B_{jj}$ is independent of $j$ and $A_{ii}$ is independent of $i$: both are scalars with $\alpha+\beta=1$. But then $X^{\mathsf T}=\alpha X+\beta X=X$, false for $n\ge2$. $\square$

**The length.** $F=\sum_{ij}E_{ij}\otimes E_{ji}$, a sum of $n^2$ products, so $\ell(F)\le n^2$. The value of the length is computed in *The Length and the Two Ranks on $M_n(\mathbb{C})$*; what matters here is that it is at least two, since $F$ is not a product.

**The orthogonal direction.** $F$ has both a symmetric part and an antisymmetric part under the transpose of the operator space, namely $F$ itself and the map $X\mapsto-X^{\mathsf T}$ on one half. It is therefore not orthogonal to the one-sided span in a trivial way; its distance to the span is the quantity measured in the finite check below.

## The Group Generated

**The two actions.** For $G,H$ invertible let $\Phi_{G,H}$ be conjugation by $L_GR_{H^{-1}}$, the operator $T\mapsto L_GR_{H^{-1}}\,T\,R_HL_{G^{-1}}$. This is an algebra automorphism of $\operatorname{End}(M_n)$, and $\Phi_{G,H}\Phi_{G',H'}=\Phi_{GG',HH'}$; the kernel is the scalars.

**Proposition (the flip normalises).** $F\Phi_{G,H}F=\Phi_{H^{-\mathsf T},G^{-\mathsf T}}$.

*Proof.* $FL_GR_{H^{-1}}F=R_{G^{\mathsf T}}L_{H^{-\mathsf T}}=L_{H^{-\mathsf T}}R_{G^{\mathsf T}}$, using that the two copies commute and $FL_GF=R_{G^{\mathsf T}}$. $\square$

**The group.** The operators $\Phi_{G,H}$ and $F\Phi_{G,H}$ form the group
$$
\bigl(GL_n\times GL_n\bigr)\rtimes\mathbb{Z}_2\big/ \mathbb{C}^{\times},
$$
of complex dimension $2n^2-1$. Its compact form is $(U(n)\times U(n))\rtimes\mathbb{Z}_2$ modulo the scalars, of real dimension $2n^2-1$.

**What is not claimed.** This is the group of automorphisms of the operator algebra that are built from the two actions and the flip. The full normaliser of the span $\mathfrak{a}$ inside $GL(\operatorname{End}(M_n))$ is not computed here, and it may be larger: the Lie algebra $\mathfrak{a}$ has two copies of $\mathfrak{sl}_n$, and for $n\ge3$ the diagram automorphism $A\mapsto-A^{\mathsf T}$ of each copy preserves $\mathfrak{a}$ as a Lie algebra without being realised by any operator of this group. Whether it is realised at all is an open point of this article.

**The biquaternion reading.** At $n=2$ the complex dimension is $7$ and the real compact dimension is $7$, and the extra $\mathbb{Z}_2$ is the chirality reversal of *Operator Chirality on $M_n(\mathbb{C})$*, implemented by the same operator $F$.

## The Two Transposes of an Adjoint Pair

**The pair.** A pair $(A,B)$ is Hermitian when $A=A^{*}$ and $B=B^{*}$. Then
$$
T_{A,B}^{\dagger}=T_{A,B},\qquad FT_{A,B}F=T_{B^{\mathsf T},A^{\mathsf T}},
$$
so the Hilbert–Schmidt adjoint fixes the product while the flip swaps the two parameters.

**The self-adjointness condition.** $T_{A,B}$ is self-adjoint exactly when $A=A^{*}$ and $B=B^{*}$, because $T_{A,B}^{\dagger}=T_{A^{*},B^{*}}$ and $T_{A,B}=T_{C,D}$ forces $(C,D)=(\lambda A,\lambda^{-1}B)$. So self-adjoint products are the Hermitian pairs.

**The symmetric condition.** $T_{A,B}$ is symmetric for the bilinear form exactly when $A=A^{\mathsf T}$ and $B=B^{\mathsf T}$, that is when both parameters are complex symmetric.

**The fixed set of the flip.** The operators fixed by $T\mapsto FTF$ are those with $T_{A,B}=T_{B^{\mathsf T},A^{\mathsf T}}$, which for a single product means $B=A^{\mathsf T}$. So the flip fixes the products with symmetric parameters and exchanges the rest in pairs.

## The Intertwining Reading

**The two representations.** $A\mapsto L_A$ is a representation of the algebra $M_n$ on the carrier space of operators, and $B\mapsto R_B$ is a representation of $M_n^{\mathrm{op}}$.

**Proposition.** $L\cong R\circ\tau$: the flip intertwines the left representation with the right one composed with the transpose anti-automorphism.

*Proof.* $FL_AF=R_{A^{\mathsf T}}$, which is the defining relation of an intertwiner between $A\mapsto L_A$ and $A\mapsto R_{A^{\mathsf T}}$. $\square$

**Proposition.** $L$ and $R$ are inequivalent as representations of $M_n$ under the identity map of the algebra.

*Proof.* An intertwiner $S$ satisfies $SAX=SXA$ for all $A,X$. For invertible $S$ this gives $AX=XA$ for all $A,X$, so every $A$ is scalar, false for $n\ge2$. $\square$

**The consequence.** The two sides are the same representation only after the anti-automorphism $\tau$ is applied. At $n=2$ the coefficient frame makes $\tau$ look like the conjugation of the algebra, so the twist is invisible; at $n\ge3$ it is visible, and it is the reason the side exchange needs an operator rather than an element.

**The tensor form.** With the intertwiner in place, the operator algebra is $V\otimes V^{*}\otimes V\otimes V^{*}$ as a representation of the two copies, and the flip exchanges the first two factors with the last two. This is the representation-theoretic content of $FT_{A,B}F=T_{B^{\mathsf T},A^{\mathsf T}}$.

## The Finite Check

Computed with numpy for $n=2,3,4,5$ on random complex $A$: the residual $\lVert FT_{A,B}F-T_{B^{\mathsf T},A^{\mathsf T}}\rVert$ is below $10^{-14}$; the residual $\lVert FL_AF-R_{A^{\mathsf T}}\rVert$ is below $10^{-14}$; the residual $\lVert T^{\mathsf T}-T_{A^{\mathsf T},B^{\mathsf T}}\rVert$ is below $10^{-13}$ for the transposed bilinear form.

The distance from $F$ to the one-sided span was computed by least squares on the $n^4\times 2n^2$ system. The residual norm is $\sqrt{n^2-1}$, namely $\sqrt3,\sqrt8,\sqrt{15},\sqrt{24}$ for $n=2,3,4,5$, and the normalised distance is $\sqrt{n^2-1}/n$, namely $0.866,0.943,0.968,0.980$. So $F$ is never in the span, and it approaches the unit sphere of the orthogonal complement as $n$ grows. At $n=2$ the flip is a $4\times4$ permutation matrix of trace $2$ and determinant $-1$.

| $n$ | $\dim\mathfrak{a}=2n^2-1$ | distance $\sqrt{n^2-1}$ | normalised |
|---|---|---|---|
| $2$ | $7$ | $1.732$ | $0.866$ |
| $3$ | $17$ | $2.828$ | $0.943$ |
| $4$ | $31$ | $3.873$ | $0.968$ |
| $5$ | $49$ | $4.899$ | $0.980$ |

## The Frame

**The flip in coordinates.** For $n=2$ the flip exchanges the two sides, and in the four-dimensional frame it swaps the two tensor factors. The alternating form is invariant under it, and the two sides are exchanged by an operator of order two up to a sign.

**The general case.** For $n\ge3$ there is no single matrix $S$ with $SAS^{-1}=A^{\mathsf T}$ for all $A$, because the automorphism group of $M_n$ is inner and the transpose is not an inner automorphism. The symmetry group of the two-sided family is therefore generated by the two independent swaps, one for each side, and it is larger than the group generated by the flip.

**The exact formula.** A symmetry that swaps the sides sends $T_{A,B}$ to $T_{B,A}$ for every pair, and the flip realises it: $FT_{A,B}F=T_{B,A}$. The formula is exact at every $n$, and it is the reason the two-sided family has a symmetry that the one-sided families do not.

**The consequence.** The two-sided structures are classified by the orbits of the group generated by the flip and the two swaps, and at $n=2$ that group is the group of the biquaternion frame, while at $n\ge3$ it is strictly larger.

## Summary

Conjugation by the transpose swaps the two sides and transposes both parameters; the bilinear transpose transposes the parameters in place. No element of the algebra and no single product exchanges the sides, at any $n\ge2$. The transpose operator $F$ is outside the one-sided span and has length at least two. The normaliser of the one-sided span is the semidirect product of the two general linear groups with the flip, of dimension $2n^2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$ | the transpose operator $X\mapsto X^{\mathsf T}$ on the carrier |
| $\mathfrak{a}$ | the span of the one-sided families |
| $T^{\dagger}$ | the Hilbert–Schmidt adjoint |
| $T^{\mathsf T}$ | the adjoint for the transposed bilinear form |
| $G$ | the normaliser of $\mathfrak{a}$ in $GL(M_n)$ |

## Further Reading
- [The Endomorphisms of $M_n(\mathbb{C})$](the-endomorphisms-of-mnc.html), for the three families and their span.
- [Operator Chirality on $M_n(\mathbb{C})$](operator-chirality-on-mnc.html), for the transpose as the chirality reversal.
- [The Enveloping Operator Algebra of $M_n(\mathbb{C})$ and the Bi-module Structure](the-enveloping-operator-algebra-of-mnc.html), for the double centraliser property.
- [The Length and the Two Ranks on $M_n(\mathbb{C})$](the-length-and-the-two-ranks-on-mnc.html), for the length of the flip.
- [The Transposition of the Two Sides](the-transposition-of-the-two-sides.html), for the case $n=2$.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the two-sided theory in the biquaternion frame.

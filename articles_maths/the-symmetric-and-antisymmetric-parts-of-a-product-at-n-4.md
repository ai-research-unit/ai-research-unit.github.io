# __The Symmetric and Antisymmetric Parts of a Product at $n=4$__

## Introduction

**Every product splits as $AB=\tfrac12\{A,B\}+\tfrac12[A,B]$, and whether the two terms are the symmetric and the antisymmetric part of $AB$ depends on the parities of the factors: for two matrices of the same parity the anticommutator is symmetric and the commutator skew, and for opposite parities the roles exchange.**

The article proves the identity, states the parity rule with its four cases, computes the two traces $\operatorname{tr}[A,B]=0$ and $\operatorname{tr}\{A,B\}=2\operatorname{tr}(AB)$, determines the image of each of the four products, and reads the left and right multiplications as sums and differences of the same two maps.

It assumes *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=4$* and *The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=4$* for the closures and the tables. The case $n=2$ is *The Symmetric and Antisymmetric Parts of a Product at $n=2$*. The operator side is *The One-Sided Operators at $n=4$*.

## The Identity

**Proposition.** For all $A,B\in M_4(\mathbb{C})$,

$$
AB=\tfrac12\{A,B\}+\tfrac12[A,B],\qquad \{A,B\}=AB+BA,\quad [A,B]=AB-BA .
$$

**Proof.** Add and subtract: $\tfrac12(AB+BA)+\tfrac12(AB-BA)=AB$.

**Corollary.** The identity is the decomposition of the product into its **symmetric** and **skew** parts whenever those two combinations happen to be symmetric and skew; it is a decomposition of $AB$ into two named combinations, not automatically into the two eigenspaces of the transpose.

**Proof.** The two combinations sum to $AB$ in every case; being eigenvalues of the transpose is an extra property that depends on $A$ and $B$.

**The care that the identity demands.** Writing "$AB$ is the sum of a symmetric and an antisymmetric matrix, namely half the anticommutator and half the commutator" is correct for two factors of the same parity and false in general.

**Proof.** For $S=E_{11}$ and $K=E_{12}-E_{21}$ the anticommutator is $\{S,K\}=E_{11}(E_{12}-E_{21})+(E_{12}-E_{21})E_{11}=E_{12}-E_{21}$, which is antisymmetric and not symmetric. So here the anticommutator is the antisymmetric part and the commutator $[S,K]=E_{12}+E_{21}$ is the symmetric part, which is the reverse of the case of two symmetric factors.

## The Parity Rule

**Theorem.** Let $A,B$ have parities $\varepsilon,\delta\in\{+1,-1\}$ under the transpose. Then

$$
\{A,B\}^{\mathsf T}=\varepsilon\delta\,\{A,B\},\qquad [A,B]^{\mathsf T}=-\varepsilon\delta\,[A,B].
$$

**Proof.** $\{A,B\}^{\mathsf T}=B^{\mathsf T}A^{\mathsf T}+A^{\mathsf T}B^{\mathsf T}=\delta\varepsilon BA+\varepsilon\delta AB=\varepsilon\delta\{A,B\}$, and the same computation with the minus sign.

**Corollary (the four cases).**

| Factors | Anticommutator | Commutator |
|---|---|---|
| symmetric, symmetric | symmetric | skew |
| antisymmetric, antisymmetric | symmetric | skew |
| symmetric, antisymmetric | skew | symmetric |
| antisymmetric, symmetric | skew | symmetric |

**Proof.** The product of the parities is $+1$ in the first two rows and $-1$ in the last two, and the theorem gives the two signs.

**Corollary (the split of a product).** For factors of the same parity, $AB=\tfrac12\{A,B\}+\tfrac12[A,B]$ is the symmetric-plus-antisymmetric decomposition of $AB$; for factors of opposite parity it is the antisymmetric-plus-symmetric decomposition.

**Proof.** The two combinations sum to $AB$ and, by the table, each lies in the stated eigenspace.

**The example that shows the antisymmetric product misbehaving.** $K=E_{12}-E_{21}$ and $K'=E_{23}-E_{32}$ are antisymmetric and $KK'=E_{13}$, whose symmetric part is $\tfrac12(E_{13}+E_{31})$ and whose skew part is $\tfrac12(E_{13}-E_{31})$, both nonzero.

**Proof.** $KK'=E_{13}$ was computed above; its transpose is $E_{31}$, and the two combinations are the displayed halves.

## The Two Traces

**Proposition.** $\operatorname{tr}[A,B]=0$ and $\operatorname{tr}\{A,B\}=2\operatorname{tr}(AB)$ for all $A,B$.

**Proof.** $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, so the difference of traces vanishes and the sum is twice one of them.

**Corollary.** Every commutator is traceless, so $[M_4,M_4]\subset\mathfrak{sl}_4$; and the trace of the anticommutator is twice the trace pairing.

**Proof.** The first is the proposition; the second is the same identity read as $\beta(A,B)=\tfrac12\operatorname{tr}\{A,B\}$.

**Corollary.** For $S$ symmetric and $K$ antisymmetric, $\operatorname{tr}(SK)=0$ is the statement $\beta(S,K)=0$, and it is also the statement that the projection of either factor onto the other's half has trace zero.

**Proof.** The first is the orthogonality of the halves; the second is the same computation read as a pairing.

**The trace of a product of two halves, in coordinates.** With $S=\sum s_{\mu\nu}T_{\mu\nu}$ over the ten positive elements and $K=\sum k_{\rho\sigma}T_{\rho\sigma}$ over the six negative ones, the pairing is $4\sum s_{\mu\nu}k_{\mu\nu}$ with the sums over the same index, and it vanishes because the two index sets are disjoint.

**Proof.** The axis-free pairing is diagonal with entries $\pm4$, so a symmetric and an antisymmetric element have no common nonzero term.

## The Images of the Four Products

**Theorem.** The four bilinear maps have full images inside the half that the parity rule predicts:

$$
\{S,S'\}\text{ spans }\operatorname{Sym}_4,\quad [S,S']\text{ spans }\operatorname{Skew}_4,\quad \{K,K'\}\text{ spans }\operatorname{Sym}_4,\quad [K,K']\text{ spans }\operatorname{Skew}_4,
$$

and likewise $\{S,K\}$ spans $\operatorname{Skew}_4$ and $[S,K]$ spans $\operatorname{Sym}_4$.

**Proof.** For the symmetric ones, $\tfrac12\{E_{ii},E_{ii}\}=E_{ii}$ and $\tfrac12\{E_{ij}+E_{ji},E_{jj}\}=\tfrac12(E_{ij}+E_{ji})$ give all ten; $[E_{ii},E_{ij}+E_{ji}]=E_{ij}-E_{ji}$ gives all six skew units. For the antisymmetric ones, $(E_{ij}-E_{ji})^{2}=-(E_{ii}+E_{jj})$ and $\{E_{ij}-E_{ji},E_{jk}-E_{kj}\}=E_{ik}+E_{ki}$ give the symmetric ones, and the commutator of two skew units is a skew unit. For the mixed ones, $\{E_{ii},E_{ij}-E_{ji}\}=E_{ij}-E_{ji}$ and $[E_{ii},E_{ij}-E_{ji}]=E_{ij}+E_{ji}$.

**Corollary.** The four products are surjective onto the half they must land in, and none of them lands in a proper subspace of it.

**Proof.** A spanning set inside the half is a spanning set of the half.

**The mixed product is always traceless.** For any $S$ and $K$, $\operatorname{tr}(SK)=0$, so the image of the mixed multiplication lies in $\mathfrak{sl}_4$ even though it spans the ten symmetric directions and the six skew ones.

**Proof.** The vanishing of the trace is the orthogonality of the halves; the symmetric and skew directions are all traceless except the scalar, and the scalar is not attained.

**$SK$ and $KS$ differ.** With $S=E_{11}$ and $K=E_{12}-E_{21}$ one has $SK=E_{12}$ and $KS=-E_{21}$.

**Proof.** Multiply: $E_{11}(E_{12}-E_{21})=E_{12}$ and $(E_{12}-E_{21})E_{11}=-E_{21}$.

**What the difference is.** $(SK)^{\mathsf T}=-KS$, so the two products are the negatives of each other's transposes; the two images are therefore the same set up to sign, while the two maps on pairs are different, and the difference is the commutator.

## The Left and Right Multiplications and Their Parts

**Definition.** $L_A(X)=AX$ and $R_A(X)=XA$.

**Proposition.** $L_A+R_A$ is the anticommutator map $X\mapsto\{A,X\}$, and $L_A-R_A$ is the adjoint map $X\mapsto[A,X]$.

**Proof.** Add and subtract the two definitions.

**Corollary.** The adjoint map is the difference of two multiplications, and its image is the commutator span, so $L_A-R_A$ has image inside $\mathfrak{sl}_4$ for every $A$.

**Proof.** The trace of a commutator vanishes.

**Proposition.** For the Hilbert–Schmidt form, $L_A^{\ast}=L_{A^{\ast}}$ and $R_A^{\ast}=R_{A^{\ast}}$.

**Proof.** $\langle L_AX,Y\rangle=\operatorname{tr}((AX)^{\ast}Y)=\operatorname{tr}(X^{\ast}A^{\ast}Y)=\langle X,A^{\ast}Y\rangle$.

**Corollary.** $L_A$ is self-adjoint exactly when $A$ is Hermitian, and skew-adjoint exactly when $A$ is anti-Hermitian; the same for $R_A$.

**Proof.** $L_A^{\ast}=L_A$ is $L_{A^{\ast}}=L_A$, which by faithfulness is $A^{\ast}=A$.

**The reading on the halves.** A symmetric $A$ gives $L_A$ self-adjoint for the trace pairing as well, because $\operatorname{tr}((AX)Y)=\operatorname{tr}(X(AY))$ always holds for the plain pairing once $A$ is symmetric; an antisymmetric $A$ gives $L_A$ skew for that pairing. The full statement of the plain adjoint is *The Adjoints and the Polar Decomposition of an Operator at $n=4$*.

## Summary

The product splits as half the anticommutator plus half the commutator, and the parity of the factors decides which half is symmetric: same parity gives a symmetric anticommutator and a skew commutator, opposite parity the reverse. The naive statement that the product of two antisymmetric matrices is symmetric fails at order four, and the example $E_{13}$ shows it.

The trace of a commutator is zero and the trace of an anticommutator is twice the trace pairing, so every mixed product is traceless and the image of each of the four products is the full half that the parity rule predicts.

The left and right multiplications add to the anticommutator map and subtract to the adjoint map, and their adjoints with respect to the Hilbert–Schmidt form are the multiplications by the dagger.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\{A,B\}$ | the anticommutator $AB+BA$ |
| $[A,B]$ | the commutator $AB-BA$ |
| $\varepsilon,\delta$ | the parities under the transpose |
| $L_A$, $R_A$ | left and right multiplication by $A$ |
| $\beta(A,B)=\operatorname{tr}(AB)$ | the trace pairing |
| $\operatorname{Sym}_4$, $\operatorname{Skew}_4$ | the two halves, dimensions $10$ and $6$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the commutator, the anticommutator and the trace identities.
- [The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=4$](the-four-multiplication-tables-ss-sk-ks-kk-at-n-4.html), for the same products arranged as tables.
- [The One-Sided Operators at $n=4$](the-one-sided-operators-at-n-4.html), for $L_A$ and $R_A$ as operators.
- [The Lie Algebra $\operatorname{Skew}_4$ and $\mathfrak{so}(4)$](the-lie-algebra-skew-4-and-so-4.html), for the commutator on the antisymmetric half.
- [The Symmetric and Antisymmetric Parts of a Product at $n=2$](the-symmetric-and-antisymmetric-parts-of-a-product-at-n-2.html), for the same identity at order two.

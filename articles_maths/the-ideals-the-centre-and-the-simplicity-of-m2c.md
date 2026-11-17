# __The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$__

## Introduction

**The left ideals of $M_2(\mathbb{C})$ are the spaces of maps killing a fixed subspace of $\mathbb{C}^{2}$, and the two-sided ideals are only the two trivial ones.**

The article classifies the left and the right ideals, exhibits the minimal left ideals as the two columns and as one line's worth of them, computes the socle, proves the simplicity and the centrality, and derives that every automorphism and every derivation is inner. It assumes *The Matrix Algebra $M_2(\mathbb{C})$* for the product, the invertibles and the trace. It defers the module reading of the minimal left ideals to *The Minimal Left Ideals of the Biquaternion Algebra* and to *The Regular Module*, and the operators on the algebra to *The Two-Sided Operators and the Segre Cone at $n=2$*.

Two facts are particular to order two. The lattice of left ideals has three levels only, with a projective line of middle elements. The socle is the whole algebra, because the regular module is semisimple; the union of the pencil of minimal left ideals is the rank-one cone, of complex dimension $3$, and it is not the socle.

## Left and Right Ideals

**Definition.** A **left ideal** is a subspace $L$ with $M_2(\mathbb{C})L\subseteq L$; a **right ideal** is a subspace $R$ with $RM_2(\mathbb{C})\subseteq R$; a **two-sided ideal** is both.

**Proposition.** For a subspace $U\subseteq\mathbb{C}^{2}$ the set

$$
L_U=\{A:U\subseteq\ker A\}
$$

is a left ideal, and for a subspace $W\subseteq\mathbb{C}^{2}$ the set

$$
R_W=\{A:\operatorname{im}A\subseteq W\}
$$

is a right ideal.

**Proof.** If $U\subseteq\ker A$ then $U\subseteq\ker(BA)$ for every $B$, because $BA$ kills whatever $A$ kills; so $L_U$ is closed under left multiplication. If $\operatorname{im}A\subseteq W$ then $\operatorname{im}(AB)=A(\operatorname{im}B)\subseteq\operatorname{im}A\subseteq W$; so $R_W$ is closed under right multiplication.

**The two constructions are dual.** Taking kernels gives left ideals and taking images gives right ideals, and the transpose exchanges the two: $\mathrm{im}A^{\mathsf T}=(\ker A)^{\perp}$, so $A\in L_U$ exactly when $A^{\mathsf T}\in R_{U^{\perp}}$.

**The dimensions.** $L_U$ is the space of maps from $\mathbb{C}^{2}/U$ to $\mathbb{C}^{2}$, of dimension $2(2-\dim U)$; $R_W$ is the space of maps from $\mathbb{C}^{2}$ to $W$, of dimension $2\dim W$. Both take the values $0,2,4$ as the subspace grows.

## The Lattice of Left Ideals

**Theorem.** Every left ideal of $M_2(\mathbb{C})$ is $L_U$ for exactly one subspace $U\subseteq\mathbb{C}^{2}$.

**Proof.** Let $L$ be a left ideal and $U=\bigcap_{A\in L}\ker A$; then $L\subseteq L_U$. Choose $A_{0}\in L$ with $\ker A_{0}=U$, possible because the intersection of finitely many kernels is one of them. For any $C$ with $U\subseteq\ker C$, the map $C$ factors through $\mathbb{C}^{2}/U$ and $A_{0}$ induces an isomorphism $\mathbb{C}^{2}/U\to\operatorname{im}A_{0}$; so $C=B A_{0}$ for a suitable $B$, and since $L$ is a left ideal $C\in L$. Hence $L_U\subseteq L$.

**Corollary (the three levels).** The left ideals are $0$ for $U=\mathbb{C}^{2}$, the ideals $L_U$ for a hyperplane $U$, of complex dimension $2$, and the algebra for $U=0$.

**Corollary (the projective line of middle elements).** The two-dimensional left ideals are parametrised by the hyperplanes of $\mathbb{C}^{2}$, that is by $\mathbb{P}^{1}$, and they are the minimal left ideals.

**Proof.** A left ideal of dimension $2$ contains no nonzero left ideal of smaller dimension, since the dimensions are $0,2,4$. The hyperplanes of a two-dimensional space form a projective line.

**The lattice at order two is thin.** At order $n$ the left ideals correspond to the subspaces of $\mathbb{C}^{n}$ and the lattice has $n+1$ levels; at order two there are three, and only the middle one is nontrivial. That lattice is what the biquaternion article *Subspaces and Decompositions of the Biquaternion Algebra* reads as the lattice of the algebra's subspaces.

## The Minimal Left Ideals and the Two Columns

**Example.** Take $U=\mathbb{C}e_{2}$, the second coordinate axis. Then $L_U$ is the set of matrices with second column zero:

$$
L_{\mathbb{C}e_{2}}=\left\{\begin{pmatrix}a&0\\ c&0\end{pmatrix}\right\}=M_2(\mathbb{C})E_{11},
$$

of complex dimension $2$.

**Proof.** $A\in L_U$ exactly when $Ae_{2}=0$, that is exactly when the second column vanishes. Every such matrix is $AE_{11}$, since $E_{11}$ keeps the first column and kills the second.

**Proposition.** Every minimal left ideal is $M_2(\mathbb{C})P$ for a rank-one projection $P$, and it consists of the maps that kill $\ker P$.

**Proof.** A minimal left ideal is $L_U$ for a hyperplane $U$; choose $P$ the projection onto a complement of $U$ along $U$. Then $\ker P=U$ and the maps killing $U$ are exactly the products $AP$.

**Corollary (the two columns).** The left ideals $M_2E_{11}$ and $M_2E_{22}$ are the two coordinate columns; they meet at $0$ and their sum is the algebra.

**Proof.** The first consists of the matrices with second column zero and the second of those with first column zero; such a matrix has both columns zero, and every matrix is the sum of its two columns read as matrices.

**The biquaternion reading.** For a complete family $P_{+},P_{-}=I-P_{+}$ the two minimal left ideals are $M_2P_+$ and $M_2P_-$, and in the Peirce basis they are the two columns $\mathbb{B}_{++}\oplus\mathbb{B}_{-+}$ and $\mathbb{B}_{+-}\oplus\mathbb{B}_{--}$. A minimal left ideal is the image of a $\tilde\Pi_+$ of the corpus, and the choice of $P$ inside its line is the gauge of the frame; the corners are *The Minimal Left Ideals of the Biquaternion Algebra*.

## The Socle

**Definition.** The **socle** is the sum of all minimal left ideals.

**Proposition.** The socle of $M_2(\mathbb{C})$ is the whole algebra, of complex dimension $4$.

**Proof.** The minimal left ideals are the columns $M_2P$ with $P$ of rank one, and two of them already span: $M_2E_{11}\oplus M_2E_{22}=M_2(\mathbb{C})$. So the regular module is the sum of two simple submodules, hence semisimple, hence equal to its socle; the general rule that a semisimple algebra equals its socle is the one recorded in *Simple and Semisimple Modules*.

**The union of the minimal left ideals is not the socle.** An element $uv^{\mathsf T}$ of rank one kills the hyperplane $v^{\perp}$, so it lies in $L_{v^{\perp}}$, and the union of the pencil $L_U$ is the set of elements of rank at most one, of complex dimension $3$. That set is not a subspace: $E_{11}+E_{22}=I$ has rank $2$. The socle is the sum of the minimal left ideals, and the sum is the algebra.

**The rank-one cone is closed under multiplication, which is why the confusion is easy.** For $A,B$ of rank at most one the product $AB$ has rank at most one, by $\operatorname{rank}(AB)\le\min(\operatorname{rank}A,\operatorname{rank}B)$; concretely $uv^{\mathsf T}xy^{\mathsf T}=(v^{\mathsf T}x)\,uy^{\mathsf T}$.

**The Segre quadric is the projectivisation of the union, not of the socle.** The rank-one matrices form the cone on the smooth quadric $\mathbb{P}^{1}\times\mathbb{P}^{1}$ in $\mathbb{P}^{3}$, whose two rulings are the pencil of minimal left ideals and the pencil of minimal right ideals. The quadric is the geometric object of *The Two-Sided Operators and the Segre Cone at $n=2$*, and it is the union of the left ideals.

## Two-Sided Ideals and Simplicity

**Theorem.** The only two-sided ideals of $M_2(\mathbb{C})$ are $0$ and the algebra.

**Proof.** Let $J\neq0$ be two-sided. It is a left ideal, so $J=L_U$ for some $U$, and $U\neq\mathbb{C}^{2}$ because $J\neq0$; choose $A\in J$ with $\ker A=U$. Since $J$ is also a right ideal, $AB\in J$ for every $B$, and $\ker(AB)\supseteq\ker B$. If $U\neq0$ pick $B$ invertible on $U$, so that $\ker(AB)\cap U=0$; then $\bigcap_{C\in J}\ker C\subsetneq U$, contradicting the definition of $U$. Hence $U=0$ and $J=M_2(\mathbb{C})$.

**Corollary.** For $0\neq A$ the two-sided ideal generated by $A$ is the whole algebra.

**Proof.** That ideal is nonzero, so it is the algebra by the theorem.

**Theorem (the centre).** $Z(M_2(\mathbb{C}))=\mathbb{C}I$.

**Proof.** If $A$ is central then $E_{11}A=AE_{11}$ gives $a_{12}=a_{21}=0$, so $A$ is diagonal, and $E_{12}A=AE_{12}$ gives $a_{11}=a_{22}$. A scalar matrix is central.

**Corollary.** $M_2(\mathbb{C})$ is a central simple $\mathbb{C}$-algebra of degree $2$, and its dimension is the square of its degree.

**The algebra is not a division algebra.** It is simple and finite-dimensional, so it is a full matrix algebra over a division ring; that ring is $\mathbb{C}$, and the degree is $2$. The zero divisors are exactly the non-invertibles.

## Automorphisms and Derivations

**Theorem (Skolem–Noether).** Every $\mathbb{C}$-algebra automorphism of $M_2(\mathbb{C})$ is inner, of the form $A\mapsto gAg^{-1}$ with $g\in GL_2(\mathbb{C})$ unique up to a scalar.

**Proof.** Let $V=\mathbb{C}^{2}$ and let $V_{\phi}$ be the twisted module, on which $A$ acts as $\phi(A)$. It is simple of dimension $2$, so an isomorphism $g:V_{\phi}\to V$ exists, and it satisfies $g\phi(A)=Ag$, that is $\phi(A)=g^{-1}Ag$. Two choices of $g$ differ by an element of the centre.

**Corollary.** $\operatorname{Aut}(M_2(\mathbb{C}))\cong PGL_2(\mathbb{C})$, of complex dimension $3$.

**Theorem (Noether).** Every derivation of $M_2(\mathbb{C})$ is inner, $\delta(A)=[D,A]$, with $D$ unique up to a central element.

**Proof.** A derivation satisfies $\delta(I)=0$, since $\delta(I)=\delta(I^{2})=2\delta(I)$. Put $D=\sum_{i}\delta(E_{i1})E_{1i}$; the derivation $A\mapsto[D,A]$ agrees with $\delta$ on the four units, because $\delta(E_{ij})=\delta(E_{i1}E_{1j})=\delta(E_{i1})E_{1j}+E_{i1}\delta(E_{1j})$ and $E_{1j}=E_{11}E_{1j}$, $E_{i1}=E_{i1}E_{11}$ reduce both terms to the two defining values. Two derivations agreeing on a basis agree everywhere.

**Corollary.** $\operatorname{Der}(M_2(\mathbb{C}))=\mathfrak{sl}_2(\mathbb{C})$, of complex dimension $3$.

**The two results are one statement.** The Lie algebra of the automorphism group is the space of derivations, and the Lie algebra of $PGL_2$ is $\mathfrak{sl}_2$. The real forms of the derivation are the subject of *The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form*.

## Modules

**Theorem (Wedderburn).** Every left $M_2(\mathbb{C})$-module is a direct sum of copies of the defining module $\mathbb{C}^{2}$.

**Proof.** The algebra is simple and finite-dimensional, and the defining module is simple; by the density theorem the algebra is the full endomorphism algebra of that module, so a module is a sum of copies of it. Equivalently, the algebra is semisimple, so every module is a sum of simple ones, and a simple module is a quotient of the regular module, which is $\mathbb{C}^{2}\oplus\mathbb{C}^{2}$.

**Corollary (the regular module).** $M_2(\mathbb{C})\cong\mathbb{C}^{2}\oplus\mathbb{C}^{2}$ as a left module, the two summands being the two columns.

**Proof.** The two columns are the minimal left ideals $M_2E_{11}$ and $M_2E_{22}$, each isomorphic to $\mathbb{C}^{2}$ under $v\mapsto(x\mapsto x_{1}v)$, and they sum directly to the algebra.

**The module picture.** A minimal left ideal is a copy of $\mathbb{C}^{2}$ read as a space of maps, and the choice of the copy is the choice of the hyperplane $U$; the two coordinate choices give the two columns. The carrier of *The Regular Module* is this module, and the Peirce coordinates of *Spinors as Peirce Coordinates in Two Dimensions* are its coordinates.

## Summary

The left ideals of $M_2(\mathbb{C})$ are the spaces $L_U=\{A:U\subseteq\ker A\}$ and the right ideals are the spaces $R_W=\{A:\operatorname{im}A\subseteq W\}$; the transpose exchanges the two families. The lattice of left ideals has three levels: $0$, a projective line of two-dimensional minimal left ideals indexed by the hyperplanes of $\mathbb{C}^{2}$, and the algebra. The two coordinate columns are minimal left ideals, they meet at $0$ and span the algebra.

The socle is the whole algebra, because the regular module is semisimple. The union of the minimal left ideals is the rank-one set, of complex dimension $3$, projectivised to the Segre quadric $\mathbb{P}^{1}\times\mathbb{P}^{1}$. The only two-sided ideals are $0$ and the algebra, the centre is $\mathbb{C}I$, and the algebra is central simple of degree $2$. Every automorphism is inner with group $PGL_2(\mathbb{C})$, every derivation is inner with space $\mathfrak{sl}_2(\mathbb{C})$, and every module is a sum of copies of $\mathbb{C}^{2}$.

| Object | At order two |
|---|---|
| Left ideals | $L_U=\{A:U\subseteq\ker A\}$, dimensions $0,2,4$ |
| Minimal left ideals | one for each hyperplane of $\mathbb{C}^{2}$, a $\mathbb{P}^{1}$ of them |
| Socle | the whole algebra, complex dimension $4$ |
| Two-sided ideals | $0$ and $M_2(\mathbb{C})$ |
| Centre | $\mathbb{C}I$ |
| $\operatorname{Aut}$ | $PGL_2(\mathbb{C})$, dimension $3$ |
| $\operatorname{Der}$ | $\mathfrak{sl}_2(\mathbb{C})$, dimension $3$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_U$ | the left ideal of maps killing $U$ |
| $R_W$ | the right ideal of maps with image inside $W$ |
| $J$ | a two-sided ideal |
| $P$ | a rank-one projection, $\ker P$ a hyperplane |
| socle | the sum of the minimal left ideals |
| $Z(A)$ | the centre of the algebra $A$ |
| $\operatorname{Aut}$, $\operatorname{Der}$ | the automorphisms and the derivations |
| $\mathbb{C}^{2}$ | the defining module, the carrier |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the ideals of a full matrix algebra, the density theorem and the simplicity.
- Joseph H. M. Wedderburn, *Lectures on Matrices* (AMS, 1934), for the structure theory and the minimal left ideals.
- [The Matrix Algebra $M_2(\mathbb{C})$](the-matrix-algebra-m2c.html), for the invertibles, the trace and the centre used here.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the same ideals in the biquaternion language.
- [The Regular Module](the-regular-module.html), for the module reading of the algebra acting on itself.

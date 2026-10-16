# __The Sesquilinear Product of the Complexoid Space__

## Introduction

The complex space carries two products: the field product $AC$ and the sesquilinear product $A\bar C$. The first is *Complex Algebra* and its relation to the second is *The Two Products of the Complexoid Space*; this article is the second product alone, as an algebraic structure. It is the complex instance of the general plain sesqualgebra, and on the commutative base the plain setting is the only one.

The product is not associative, and the article's subject is exactly how it fails to be: the associator, the ternary product it defines, the two one-sided multiplications and the monoid they generate, the sandwich, and the commutator with its symmetrisation. It does not treat the product as a form: the Hermitian form $\langle A,C\rangle_{*}=A\bar C$ is *The Hermitian Form and the Positivity of the Complexoid Algebra*, below this article in this category, and the two algebraic norms are *The Two Forms and the Two Algebraic Norms of the Complexoid Space*. It does not treat the invertibility or the norm of the field, which are *Complex Norm and Invertibility*.

**Interpretation and notation.** The element is $A=a+ia'$, a second element is $C=c+ic'$; the base involution is the bar $\bar A=a-ia'$ and ${}^{*}=\bar{\cdot}$. The sesquilinear product is written

$$
A\star C= A\bar C,
$$

the star being reserved for the involution and never written as an operator symbol; the plain product is juxtaposition. The element letters are $A$, $\langle\cdot\rangle$, $C$; the letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ name the four forms of the corpus, and only $\langle\cdot,\cdot\rangle_{*}$ appears in this article, in the adjoint of the sandwich. The single overlap, the letter $\langle\cdot,\cdot\rangle$, is resolved by the slot: it is the middle element of the associator and of the ternary product, and it is the bilinear form only where a form is in play, which in this article is nowhere. The sandwich parameters are $P$ and $Q$.

## The Product and Its Class

**Definition.** The **sesquilinear product** of the complex space is $A\star C=A\bar C$. It is the general plain sesquilinear product of *The Two Products of the Complexoid Space*.

**Proposition (parities).** The product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second: for complex $\lambda$,

$$
(\lambda A)\star C=\lambda(A\star C), \qquad A\star(\lambda C)=\bar\lambda\,(A\star C).
$$

**Proof.** The first identity is the associativity-legality of the scalar in the plain product; the second is $\overline{\lambda C}=\bar\lambda\bar C$.

**Proposition (the two one-sided units).** The element $1$ is a right unit and not a left unit: $A\star1=A$ for every $A$, while $1\star A=\bar A$, which equals $A$ only for real $A$. The product has no two-sided unit.

**Proof.** $A\star1=A\bar 1=A$, and $1\star A=1\bar A=\bar A$. A two-sided unit $\mathrm{U}$ would satisfy $\mathrm{U}\star A=A$, that is $\mathrm{U}\bar A=A$ for every $A$; at $A=i$ this reads $-\mathrm{U}i=i$, so $\mathrm{U}=-1$, while at $A=1$ it reads $\mathrm{U}=1$, and the two values disagree. No two-sided unit exists.

**Proposition (the failure of the field laws).** The product is neither associative nor commutative. It is **conjugate-commutative**,

$$
A\star C=\overline{C\star A},
$$

which is the law that replaces commutativity, and which is the reason the two slots cannot simply be exchanged.

**Proof.** For associativity, the associator computed in §*The Associator and the Ternary Product* is nonzero; for commutativity, $A\star C=A\bar C$ against $C\star A=C\bar A$, which differ at $A=1$, $C=i$. For conjugate-commutativity, $\overline{C\star A}=\overline{C\bar A}=\bar C A=A\bar C=A\star C$.

**Remark (the two one-sided actions).** The two special values of the multiplications of §*The Left and Right Multiplications* are $L_{1}={}^{*}$, the involution, and $R_{1}=\mathrm{id}$; the right unit is the identity at the right and the involution at the left. This asymmetry is the operator form of the missing two-sided unit.

## The Associator and the Ternary Product

**Definition.** The **associator** of the sesquilinear product is

$$
[A,B,C]=(A\star B)\star C-A\star(B\star C).
$$

**Theorem.** For all $A,B,C$,

$$
[A,B,C]= A\bar B\,(\bar C-C).
$$

**Proof.** $(A\star B)\star C=(A\bar B)\star C=(A\bar B)\bar C=A\bar B\bar C$, and $A\star(B\star C)=A\star(B\bar C)=A\overline{B\bar C}=A\bar B C$; the difference is $A\bar \langle \bar C-C\rangle$.

**Corollary (the associator is confined to the anti-self-adjoint part).** The associator vanishes for all $A,B$ exactly when $C$ is self-adjoint, $C=\bar C$. It is therefore a failure carried by the anti-self-adjoint part of the third slot alone, and it vanishes on the whole real subspace.

**Proof.** $A\bar \langle \bar C-C\rangle=0$ for all $A,B$ iff $\bar C-C=0$, since $\mathbb{C}$ has no zero divisor.

**Remark (the conjugate-commutative law and the associator).** The law $A\star C=\overline{C\star A}$ relocates a conjugation across the product, and read on the associator it says that the associator is Hermitian-symmetric in its three slots,

$$
[A,B,C]=\overline{[\bar A,\bar B,\bar C]} .
$$

The verification is one line from the formula: $\overline{[\bar A,\bar B,\bar C]}=\overline{\bar A \langle C-\bar C\rangle}=A\bar \langle \bar C-C\rangle=[A,B,C]$. The defect is therefore conjugate-symmetric in the three slots, and it is non-zero exactly on the anti-self-adjoint part of the third; the conjugate-commutative law relocates the conjugation rather than removing the defect. The sesquilinear product is at this point at its sharpest difference from the field product, which has no associator at all. The general theory of the associator of a sesqualgebra is *The Sesquilinear Associator and the Ternary Product*.

**Definition.** The **ternary product** of the sesquilinear structure is

$$
\{A,B,C\}=(A\star B)\star\bar C= A\bar B C.
$$

**Proposition.** The ternary product is $\mathbb{C}$-linear in the first and third slots and conjugate-linear in the second; it is symmetric in its outer slots, $\{A,B,C\}=\{C,B,A\}$; and it is Hermitian-symmetric,

$$
\overline{\{A,B,C\}}=\{\bar C,\bar B,\bar A\}.
$$

**Proof.** The parities are read on $A\bar B C$. For the outer symmetry, $C\bar B A=A\bar B C$ by the commutativity of the plain product. For the Hermitian symmetry, $\overline{A\bar B C}=\bar A B\bar C$ and $\{\bar C,\bar B,\bar A\}=\bar C B\bar A=\bar A B\bar C$.

**Theorem (the Jordan triple identity).** For all $A,B,U,V,W$,

$$
\{A,B,\{U,V,W\}\}=\{\{A,B,U\},V,W\}-\{U,\{B,A,V\},W\}+\{U,V,\{A,B,W\}\}.
$$

**Proof.** Both sides equal $A\bar B U\bar V W$. On the right the three terms are

$$
A\bar B U\bar V W, \qquad -U\bar B A\bar V W, \qquad U\bar V A\bar B W,
$$

and the second and third cancel after the plain product is put in a common order, $-U\bar B A\bar V W+U\bar V A\bar B W=U\bar B\bar V W(-A+A)=0$; what remains is the left-hand side. The identity is the defining axiom of a Jordan triple system, and its satisfaction is what makes the sesquilinear structure a $J^{*}$-algebra in the sense of *Algebraic J\*-Algebras*.

**Remark.** The ternary product is the sandwich of §*The Sesquilinear Sandwich* read with two arguments fixed; the two are the same object. The plain outer symmetry fails whenever the plain product is non-commutative.

## The Left and Right Multiplications

**Definition.** The **left and right multiplications** of the sesquilinear product are

$$
L_{A}(X)=A\star X=A\bar X, \qquad R_{A}(X)=X\star A=X\bar A .
$$

**Proposition (the parities).** $L_{A}$ is conjugate-linear and $R_{A}$ is linear.

**Proof.** $L_{A}(\lambda X)=A\overline{\lambda X}=\bar\lambda\,A\bar X=\bar\lambda L_{A}(X)$, while $R_{A}(\lambda X)=(\lambda X)\bar A=\lambda R_{A}(X)$.

**Theorem (the composition laws).** Writing $L^{\mathrm{alg}}_{A}(X)=AX$ for the ordinary left multiplication of the field,

$$
L_{A}\circ L_{B}=L^{\mathrm{alg}}_{A\bar B}, \qquad R_{A}\circ R_{B}=R_{AB}, \qquad L_{A}\circ R_{B}=L_{AB}, \qquad R_{A}\circ L_{B}=L_{\bar A B}.
$$

**Proof.** Compute in order: $L_{A}L_{B}(X)=A\overline{B\bar X}=A\bar B X$; $R_{A}R_{B}(X)=(X\bar B)\bar A=X\bar A\bar B=X\overline{AB}=R_{AB}(X)$; $L_{A}R_{B}(X)=A\overline{X\bar B}=AB\bar X=L_{AB}(X)$; and $R_{A}L_{B}(X)=(B\bar X)\bar A=\bar A B\bar X=L_{\bar A B}(X)$.

**Corollary (the closure is on the right).** The right multiplications close under composition, in the forward order, and the map $A\mapsto R_{A}$ is an isomorphism of the multiplicative monoid of the field onto the right family, with identity $R_{1}=\mathrm{id}$. The left multiplications do **not** close: their composite $L_{A}\circ L_{B}=L^{\mathrm{alg}}_{A\bar B}$ is an ordinary multiplication of the field, and it is a left multiplication of the sesquilinear product only in the trivial case $A\bar B=0$. The left family is therefore not a monoid.

**Proof.** The composition laws are the theorem. For the triviality: $L^{\mathrm{alg}}_{D}=L_{C}$ reads $DX=C\bar X$ for all $X$; at $X=1$ it gives $D=C$, at $X=i$ it gives $Di=-Ci$, hence $D=-C$, so $C=D=0$. The special value $L_{1}={}^{*}$ shows that the left family carries the involution rather than a unit.

**Remark (the opposite monoid, read here).** On $\mathbb{C}$ the plain product is commutative, so the opposite of the multiplicative monoid is the monoid itself and no left-family reversal is needed; what survives is the asymmetry of the sesquilinear product proper, namely that the closure sits on the right family and the left family does not close at all. The general operators are *The Left and Right Multiplication Operators of a Sesqualgebra*.

## The Sesquilinear Sandwich

**Definition.** The **sesquilinear sandwich** of parameters $P$ and $Q$ is the operator

$$
S_{P,Q}(X)=P\star X\star Q=P\bar X\bar Q .
$$

The general sandwich $S_{a,b}(x)=a\bar x b$ of *The Sesquilinear Sandwich Operator* is recovered by $a=P$ and $b=\bar Q$.

**Proposition (two decompositions).** The sandwich decomposes into a pair of one-sided multiplications and into an ordinary two-sided multiplication followed by the involution:

$$
S_{P,Q}=R_{Q}\circ L_{P}=T_{P,\bar Q}\circ{}^{*}, \qquad T_{P,D}(X)=PXD .
$$

**Proof.** $R_{Q}L_{P}(X)=(P\bar X)\bar Q=P\bar X\bar Q$, and $T_{P,\bar Q}(\bar X)=P\bar X\bar Q$.

**Theorem (the adjoint with respect to $\langle\cdot,\cdot\rangle_{*}$).** Let the adjoint ${}^{\dagger}$ be taken with respect to the Hermitian form $\langle X,Y\rangle_{*}=X\bar Y$, in the convention $\langle TX,Y\rangle_{*}=\overline{\langle X,T^{\dagger}Y\rangle_{*}}$ for a conjugate-linear $T$ and $\langle TX,Y\rangle_{*}=\langle X,T^{\dagger}Y\rangle_{*}$ for a linear $T$. Then

$$
S_{P,Q}^{\dagger}=S_{\bar Q,\bar P}, \qquad L_{A}^{\dagger}=L_{A}, \qquad R_{A}^{\dagger}=L^{\mathrm{alg}}_{A}.
$$

**Proof.** For the sandwich, $S_{\bar Q,\bar P}(Y)=\bar Q\bar Y P$, so $\langle X,S_{\bar Q,\bar P}Y\rangle_{*}=X\overline{\bar Q\bar Y P}=XQY\bar P$ and $\overline{\langle X,S_{\bar Q,\bar P}Y\rangle_{*}}=\bar X\bar Q\bar Y P$, while $\langle S_{P,Q}X,Y\rangle_{*}=P\bar X\bar Q\bar Y$; the two agree by the commutativity of the plain product. For $L_{A}$, $\langle L_{A}X,Y\rangle_{*}=A\bar X\bar Y$ and $\overline{\langle X,L_{A}Y\rangle_{*}}=\overline{X\overline{A\bar Y}}=\bar X A\bar Y$; the two agree. For $R_{A}$, $\langle R_{A}X,Y\rangle_{*}=X\bar A\bar Y$ and $H(X,L^{\mathrm{alg}}_{A}Y)=X\overline{AY}=X\bar A\bar Y$. The adjoint of the involution itself is ${}^{*}$, since $\langle \bar X,Y\rangle_{*}=\bar X\bar Y=\overline{\langle X,\bar Y\rangle_{*}}$.

**Remark (the operator form of the sandwich).** The sandwich is the general two-sided operator of the sesquilinear structure; it contains the two one-sided families at $P=1$ and $Q=1$, $S_{1,Q}=R_{Q}\circ{}^{*}$ and $S_{P,1}=L_{P}$, and it contains the involution at $P=Q=1$, $S_{1,1}={}^{*}$. The general operator and the two families are *The Sesquilinear Sandwich Operator*; the complex instance is the present computation collapsed to one dimension.

## The Commutator and the Symmetrised Product

**Definition.** The **commutator** and the **symmetrised product** of the sesquilinear structure are

$$
[A,C]=A\star C-C\star A=A\bar C-C\bar A, \qquad A\odot C=A\star C+C\star A=A\bar C+C\bar A .
$$

**Theorem.** For all $A,C$,

$$
[A,C]=2i\operatorname{Im}(A\bar C), \qquad A\odot C=2\operatorname{Re}(A\bar C).
$$

In particular the commutator is purely imaginary and the symmetrised product is real; the commutator is the imaginary part of the Hermitian form and the symmetrisation its real part, each doubled.

**Proof.** For a complex number $A\bar C$ one has $A\bar C=\operatorname{Re}(A\bar C)+i\operatorname{Im}(A\bar C)$ and $\overline{A\bar C}=\operatorname{Re}(A\bar C)-i\operatorname{Im}(A\bar C)$; and $C\bar A=\overline{A\bar C}$. Adding and subtracting gives the two displays.

**Proposition.** The commutator is alternating, $[A,A]=0$, and $\mathbb{R}$-bilinear; its values lie in $i\mathbb{R}$. The symmetrised product is real-valued, symmetric, and $\mathbb{R}$-bilinear.

**Proof.** Alternation and the value set are read on $[A,C]=2i\operatorname{Im}(A\bar C)$; the real-bilinearity is the real-bilinearity of the real and imaginary parts of the sesquilinear product, which is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second.

**Theorem (the Jacobi identity holds).** The commutator is an antisymmetric $\mathbb{R}$-bilinear bracket on the two-dimensional real space, valued in $i\mathbb{R}$ and of centre $\{0\}$; with it, $\mathbb{C}$ is the two-dimensional non-abelian Lie algebra, and the **Jacobi identity** holds:

$$
[[A,C],D]+[[C,D],A]+[[D,A],C]=0 \qquad \text{for all } A,C,D \in \mathbb{C}.
$$

**Proof.** Alternation is $[A,A]=0$; bilinearity is the real-bilinearity of the real and imaginary parts of $A\bar C$; the value set is $[A,C]=2i\operatorname{Im}(A\bar C)$. Write $[A,C]=-2\omega(A,C)\,i$ with the area form $\omega(A,C)=ac'-a'c$. Since $i$ is central and $[i,D]=i\bar D-D\bar i=2i\operatorname{Sc}(D)$, the cyclic sum is

$$
-4i\bigl(\omega(A,C)\operatorname{Sc}(D)+\omega(C,D)\operatorname{Sc}(A)+\omega(D,A)\operatorname{Sc}(C)\bigr),
$$

and the parenthesis is $ac'd-a'cd+cd'a-c'da+da'c-d'ac=0$, the six terms cancelling in pairs. The centre is the kernel of the area form, which is $\{0\}$ because $\omega$ is non-degenerate.

**Remark (why the identity holds, and what collapses).** The identity is not an accident of $\mathbb{C}$ and not a coincidence of the computation. On a **two-dimensional** real space every antisymmetric bilinear bracket satisfies it, whatever its values: a contributing triple must repeat an argument, and the two resulting terms are opposite. The failure of the Jacobi identity is a phenomenon of dimension at least three, and the complex space is too small to exhibit it. What collapses on $\mathbb{C}$ is the antisymmetric layer and not the commutator: the algebra is commutative, so the class-preserving antisymmetrisation $\tfrac12(A\bar C-\bar C A)$ vanishes identically. What plays the role of a failed identity here is the **associator** of the binary product, $[A,B,C]=A\bar \langle \bar C-C\rangle$; the ternary product repairs it. The symmetrised product does not collapse: it is the real part of $\langle\cdot,\cdot\rangle_{*}$ and survives as the symmetric half of the sesquilinear split.

## Summary

The sesquilinear product $A\star C=A\bar C$ is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second; it has the right unit $1$ and no left unit; it is neither associative nor commutative, and it is conjugate-commutative, $A\star C=\overline{C\star A}$. Its associator is $[A,B,C]=A\bar \langle \bar C-C\rangle$, nonzero but confined to the anti-self-adjoint part of the third slot; its ternary product $\{A,B,C\}=A\bar B C$ is symmetric in the outer slots, Hermitian-symmetric and satisfies the Jordan triple identity, which makes the structure a $J^{*}$-algebra. The left multiplications are conjugate-linear and do not close under composition, their composite being the ordinary left multiplication $L^{\mathrm{alg}}_{A\bar B}$; the right multiplications are linear and close in the forward order, so that $A\mapsto R_{A}$ is an isomorphism of the multiplicative monoid of the field onto the right family. The sandwich $S_{P,Q}=R_{Q}\circ L_{P}$ has adjoint $S_{P,Q}^{\dagger}=S_{\bar Q,\bar P}$ with respect to the Hermitian form; the one-sided adjoints are $L_{A}^{\dagger}=L_{A}$ and $R_{A}^{\dagger}=L^{\mathrm{alg}}_{A}$. The commutator $[A,C]=2i\operatorname{Im}(A\bar C)$ is purely imaginary and alternating, and the Jacobi identity holds on it; the symmetrised product $A\odot C=2\operatorname{Re}(A\bar C)$ is the real part of the form. The product read as a form is *The Hermitian Form and the Positivity of the Complexoid Algebra*, below this article in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A\star C=A\bar C$ | the sesquilinear product, written with the star-nothing convention $A\bar C$ |
| $L_{A}$, $R_{A}$ | the sesquilinear left and right multiplications, $A\bar X$ and $X\bar A$ |
| $L^{\mathrm{alg}}_{A}$ | the ordinary left multiplication of the field, $L^{\mathrm{alg}}_{A}(X)=AX$ |
| $S_{P,Q}$ | the sesquilinear sandwich, $S_{P,Q}(X)=P\bar X\bar Q$ |
| $T_{P,D}$ | the ordinary two-sided multiplication, $T_{P,D}(X)=PXD$ |
| $A\star B\star C$ | the binary product iterated, $(A\star B)\star C=A\bar B\bar C$ |
| $\{A,B,C\}$ | the ternary product, $(A\star B)\star\bar C=A\bar B C$ |
| $[A,B,C]$ | the associator, $(A\star B)\star C-A\star(B\star C)$ |
| $[A,C]$ | the commutator, $A\bar C-C\bar A=2i\operatorname{Im}(A\bar C)$ |
| $A\odot C$ | the symmetrised product, $A\bar C+C\bar A=2\operatorname{Re}(A\bar C)$ |
| ${}^{\dagger}$ | the adjoint with respect to $\langle\cdot,\cdot\rangle_{*}$, written on operators and never on elements |

## Further Reading

- Max Koecher, *The Minnesota Notes on Jordan Algebras and Their Applications*, Lecture Notes in Mathematics 1710 (Springer, 1999), for Jordan triple systems and the Jordan triple identity.
- Erhard Neher, "Jordan triple systems by the grid approach", *Lecture Notes in Mathematics* 1280 (Springer, 1987), for the structure theory the ternary product of the sesquilinear structure satisfies.
- Harald Hanche-Olsen and Erling Størmer, *Jordan Operator Algebras* (Pitman, 1984), for $J^{*}$-algebras and the axioms of the sesquilinear square.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for associators, non-associative products and conjugate-linear maps.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for the associator and the ternary products of a non-associative algebra.

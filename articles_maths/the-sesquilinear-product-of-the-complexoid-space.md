# __The Sesquilinear Product of the Complexoid Space__

## Introduction

The complex space carries two products: the field product $Q_1Q_2$ and the sesquilinear product $Q_1\bar Q_2$. The first is *Complex Algebra* and its relation to the second is *The Two Products of the Complexoid Space*; this article is the second product alone, as an algebraic structure. It is the complex instance of the general plain sesqualgebra, and on the commutative base the plain setting is the only one.

The product is not associative, and the article's subject is exactly how it fails to be: the associator, the ternary product it defines, the two one-sided multiplications and the monoid they generate, the sandwich, and the commutator with its symmetrisation. It does not treat the product as a form: the Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ is *The Hermitian Form and the Positivity of the Complexoid Algebra*, below this article in this category, and the two algebraic norms are *The Two Forms and the Two Algebraic Norms of the Complexoid Space*. It does not treat the invertibility or the norm of the field, which are *Complex Norm and Invertibility*.

**Interpretation and notation.** The element is $Q_1=q_1+iq'_1$, a second element is $Q_2=q_2+iq'_2$; the base involution is the bar $\bar Q_1=q_1-iq'_1$ and ${}^{*}=\bar{\cdot}$. The sesquilinear product is written

$$
Q_1\star Q_2= Q_1\bar Q_2,
$$

the superscript star being reserved for the involution and never written as an operator symbol; the plain product is juxtaposition. The elements are written with the letter $Q$, numbered when several occur; the letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ name the four forms of the corpus, and only $\langle\cdot,\cdot\rangle_{*}$ appears in this article, in the adjoint of the sandwich. The sandwich parameters are $Q_1$ and $Q_2$.

## The Product and Its Class

**Definition.** The **sesquilinear product** of the complex space is $Q_1\star Q_2=Q_1\bar Q_2$. It is the general plain sesquilinear product of *The Two Products of the Complexoid Space*.

**Proposition (parities).** The product is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second: for complex $\lambda$,

$$
(\lambda Q_1)\star Q_2=\lambda(Q_1\star Q_2), \qquad Q_1\star(\lambda Q_2)=\bar\lambda\,(Q_1\star Q_2).
$$

**Proof.** The first identity is the associativity-legality of the scalar in the plain product; the second is $\overline{\lambda Q_2}=\bar\lambda\bar Q_2$.

**Proposition (the two one-sided units).** The element $1$ is a right unit and not a left unit: $Q\star1=Q$ for every $Q$, while $1\star Q=\bar Q$, which equals $Q$ only for real $Q$. The product has no two-sided unit.

**Proof.** $Q\star1=Q\bar 1=Q$, and $1\star Q=1\bar Q=\bar Q$. A two-sided unit $\mathrm{U}$ would satisfy $\mathrm{U}\star Q=Q$, that is $\mathrm{U}\bar Q=Q$ for every $Q$; at $Q=i$ this reads $-\mathrm{U}i=i$, so $\mathrm{U}=-1$, while at $Q=1$ it reads $\mathrm{U}=1$, and the two values disagree. No two-sided unit exists.

**Proposition (the failure of the field laws).** The product is neither associative nor commutative. It is **conjugate-commutative**,

$$
Q_1\star Q_2=\overline{Q_2\star Q_1},
$$

which is the law that replaces commutativity, and which is the reason the two slots cannot simply be exchanged.

**Proof.** For associativity, the associator computed in §*The Associator and the Ternary Product* is nonzero; for commutativity, $Q_1\star Q_2=Q_1\bar Q_2$ against $Q_2\star Q_1=Q_2\bar Q_1$, which differ at $Q_1=1$, $Q_2=i$. For conjugate-commutativity, $\overline{Q_2\star Q_1}=\overline{Q_2\bar Q_1}=\bar Q_2 Q_1=Q_1\bar Q_2=Q_1\star Q_2$.

**Remark (the two one-sided actions).** The two special values of the multiplications of §*The Left and Right Multiplications* are $L_{1}={}^{*}$, the involution, and $R_{1}=\mathrm{id}$; the right unit is the identity at the right and the involution at the left. This asymmetry is the operator form of the missing two-sided unit.

## The Associator and the Ternary Product

**Definition.** The **associator** of the sesquilinear product is

$$
[Q_1,Q_2,Q_3]=(Q_1\star Q_2)\star Q_3-Q_1\star(Q_2\star Q_3).
$$

**Theorem.** For all $Q_1,Q_2,Q_3$,

$$
\boxed{\;[Q_1,Q_2,Q_3]= Q_1\bar Q_2\,(\bar Q_3-Q_3)\;}.
$$

**Proof.** $(Q_1\star Q_2)\star Q_3=(Q_1\bar Q_2)\star Q_3=(Q_1\bar Q_2)\bar Q_3=Q_1\bar Q_2\bar Q_3$, and $Q_1\star(Q_2\star Q_3)=Q_1\star(Q_2\bar Q_3)=Q_1\overline{Q_2\bar Q_3}=Q_1\bar Q_2 Q_3$; the difference is $Q_1\bar Q_2(\bar Q_3-Q_3)$.

**Corollary (the associator is confined to the anti-self-adjoint part).** The associator vanishes for all $Q_1,Q_2$ exactly when $Q_3$ is self-adjoint, $Q_3=\bar Q_3$. It is therefore a failure carried by the anti-self-adjoint part of the third slot alone, and it vanishes on the whole real subspace.

**Proof.** $Q_1\bar Q_2(\bar Q_3-Q_3)=0$ for all $Q_1,Q_2$ iff $\bar Q_3-Q_3=0$, since $\mathbb{C}$ has no zero divisor.

**Remark (the conjugate-commutative law and the associator).** The law $Q_1\star Q_2=\overline{Q_2\star Q_1}$ relocates a conjugation across the product, and read on the associator it says that the associator is Hermitian-symmetric in its three slots,

$$
[Q_1,Q_2,Q_3]=\overline{[\bar Q_1,\bar Q_2,\bar Q_3]} .
$$

The verification is one line from the formula: $\overline{[\bar Q_1,\bar Q_2,\bar Q_3]}=\overline{\bar Q_1 Q_2(Q_3-\bar Q_3)}=Q_1\bar Q_2(\bar Q_3-Q_3)=[Q_1,Q_2,Q_3]$. The defect is therefore conjugate-symmetric in the three slots, and it is non-zero exactly on the anti-self-adjoint part of the third; the conjugate-commutative law relocates the conjugation rather than removing the defect. The sesquilinear product is at this point at its sharpest difference from the field product, which has no associator at all. The general theory of the associator of a sesqualgebra is *The Sesquilinear Associator and the Ternary Product*.

**Definition.** The **ternary product** of the sesquilinear structure is

$$
\{Q_1,Q_2,Q_3\}=(Q_1\star Q_2)\star\bar Q_3= Q_1\bar Q_2 Q_3.
$$

**Proposition.** The ternary product is $\mathbb{C}$-linear in the first and third slots and conjugate-linear in the second; it is symmetric in its outer slots, $\{Q_1,Q_2,Q_3\}=\{Q_3,Q_2,Q_1\}$; and it is Hermitian-symmetric,

$$
\overline{\{Q_1,Q_2,Q_3\}}=\{\bar Q_3,\bar Q_2,\bar Q_1\}.
$$

**Proof.** The parities are read on $Q_1\bar Q_2 Q_3$. For the outer symmetry, $Q_3\bar Q_2 Q_1=Q_1\bar Q_2 Q_3$ by the commutativity of the plain product. For the Hermitian symmetry, $\overline{Q_1\bar Q_2 Q_3}=\bar Q_1 Q_2\bar Q_3$ and $\{\bar Q_3,\bar Q_2,\bar Q_1\}=\bar Q_3 Q_2\bar Q_1=\bar Q_1 Q_2\bar Q_3$.

**Theorem (the Jordan triple identity).** For all $Q_1,Q_2,Q_3,Q_4,Q_5$,

$$
\boxed{\;\{Q_1,Q_2,\{Q_3,Q_4,Q_5\}\}=\{\{Q_1,Q_2,Q_3\},Q_4,Q_5\}-\{Q_3,\{Q_2,Q_1,Q_4\},Q_5\}+\{Q_3,Q_4,\{Q_1,Q_2,Q_5\}\}\;}.
$$

**Proof.** Both sides equal $Q_1\bar Q_2 Q_3\bar Q_4 Q_5$. On the right the three terms are

$$
Q_1\bar Q_2 Q_3\bar Q_4 Q_5, \qquad -Q_3\bar Q_2 Q_1\bar Q_4 Q_5, \qquad Q_3\bar Q_4 Q_1\bar Q_2 Q_5,
$$

and the second and third cancel after the plain product is put in a common order, $-Q_3\bar Q_2 Q_1\bar Q_4 Q_5+Q_3\bar Q_4 Q_1\bar Q_2 Q_5=Q_3\bar Q_2\bar Q_4 Q_5(-Q_1+Q_1)=0$; what remains is the left-hand side. The identity is the defining axiom of a Jordan triple system, and its satisfaction is what makes the sesquilinear structure a $J^{*}$-algebra in the sense of *Algebraic J\*-Algebras*.

**Remark.** The ternary product is the sandwich of §*The Sesquilinear Sandwich* read with two arguments fixed; the two are the same object. The plain outer symmetry fails whenever the plain product is non-commutative.

## The Left and Right Multiplications

**Definition.** The **left and right multiplications** of the sesquilinear product are

$$
L_{Q}(X)=Q\star X=Q\bar X, \qquad R_{Q}(X)=X\star Q=X\bar Q .
$$

**Proposition (the parities).** $L_{Q}$ is conjugate-linear and $R_{Q}$ is linear.

**Proof.** $L_{Q}(\lambda X)=Q\overline{\lambda X}=\bar\lambda\,Q\bar X=\bar\lambda L_{Q}(X)$, while $R_{Q}(\lambda X)=(\lambda X)\bar Q=\lambda R_{Q}(X)$.

**Theorem (the composition laws).** Writing $L^{\mathrm{alg}}_{Q}(X)=QX$ for the ordinary left multiplication of the field,

$$
L_{Q_1}\circ L_{Q_2}=L^{\mathrm{alg}}_{Q_1\bar Q_2}, \qquad R_{Q_1}\circ R_{Q_2}=R_{Q_1Q_2}, \qquad L_{Q_1}\circ R_{Q_2}=L_{Q_1Q_2}, \qquad R_{Q_1}\circ L_{Q_2}=L_{\bar Q_1 Q_2}.
$$

**Proof.** Compute in order: $L_{Q_1}L_{Q_2}(X)=Q_1\overline{Q_2\bar X}=Q_1\bar Q_2 X$; $R_{Q_1}R_{Q_2}(X)=(X\bar Q_2)\bar Q_1=X\bar Q_1\bar Q_2=X\overline{Q_1Q_2}=R_{Q_1Q_2}(X)$; $L_{Q_1}R_{Q_2}(X)=Q_1\overline{X\bar Q_2}=Q_1Q_2\bar X=L_{Q_1Q_2}(X)$; and $R_{Q_1}L_{Q_2}(X)=(Q_2\bar X)\bar Q_1=\bar Q_1 Q_2\bar X=L_{\bar Q_1 Q_2}(X)$.

**Corollary (the closure is on the right).** The right multiplications close under composition, in the forward order, and the map $Q\mapsto R_{Q}$ is an isomorphism of the multiplicative monoid of the field onto the right family, with identity $R_{1}=\mathrm{id}$. The left multiplications do **not** close: their composite $L_{Q_1}\circ L_{Q_2}=L^{\mathrm{alg}}_{Q_1\bar Q_2}$ is an ordinary multiplication of the field, and it is a left multiplication of the sesquilinear product only in the trivial case $Q_1\bar Q_2=0$. The left family is therefore not a monoid.

**Proof.** The composition laws are the theorem. For the triviality: $L^{\mathrm{alg}}_{Q_1}=L_{Q_2}$ reads $Q_1X=Q_2\bar X$ for all $X$; at $X=1$ it gives $Q_1=Q_2$, at $X=i$ it gives $Q_1i=-Q_2i$, hence $Q_1=-Q_2$, so $Q_1=Q_2=0$. The special value $L_{1}={}^{*}$ shows that the left family carries the involution rather than a unit.

**Remark (the opposite monoid, read here).** On $\mathbb{C}$ the plain product is commutative, so the opposite of the multiplicative monoid is the monoid itself and no left-family reversal is needed; what survives is the asymmetry of the sesquilinear product proper, namely that the closure sits on the right family and the left family does not close at all. The general operators are *The Left and Right Multiplication Operators of a Sesqualgebra*.

## The Sesquilinear Sandwich

**Definition.** The **sesquilinear sandwich** of parameters $Q_1$ and $Q_2$ is the operator

$$
S_{Q_1,Q_2}(X)=Q_1\star X\star Q_2=Q_1\bar X\bar Q_2 .
$$

The general sandwich $S_{a,b}(x)=a\bar x b$ of *The Sesquilinear Sandwich Operator* is recovered by $a=Q_1$ and $b=\bar Q_2$.

**Proposition (two decompositions).** The sandwich decomposes into a pair of one-sided multiplications and into an ordinary two-sided multiplication followed by the involution:

$$
S_{Q_1,Q_2}=R_{Q_2}\circ L_{Q_1}=T_{Q_1,\bar Q_2}\circ{}^{*}, \qquad T_{Q_1,Q_2}(X)=Q_1XQ_2 .
$$

**Proof.** $R_{Q_2}L_{Q_1}(X)=(Q_1\bar X)\bar Q_2=Q_1\bar X\bar Q_2$, and $T_{Q_1,\bar Q_2}(\bar X)=Q_1\bar X\bar Q_2$.

**Theorem (the adjoint with respect to $\langle\cdot,\cdot\rangle_{*}$).** Let the adjoint ${}^{\dagger}$ be taken with respect to the Hermitian form $\langle X,Y\rangle_{*}=X\bar Y$, in the convention $\langle TX,Y\rangle_{*}=\overline{\langle X,T^{\dagger}Y\rangle_{*}}$ for a conjugate-linear $T$ and $\langle TX,Y\rangle_{*}=\langle X,T^{\dagger}Y\rangle_{*}$ for a linear $T$. Then

$$
S_{Q_1,Q_2}^{\dagger}=S_{\bar Q_2,\bar Q_1}, \qquad L_{Q}^{\dagger}=L_{Q}, \qquad R_{Q}^{\dagger}=L^{\mathrm{alg}}_{Q}.
$$

**Proof.** For the sandwich, $S_{\bar Q_2,\bar Q_1}(Y)=\bar Q_2\bar Y Q_1$, so $\langle X,S_{\bar Q_2,\bar Q_1}Y\rangle_{*}=X\overline{\bar Q_2\bar Y Q_1}=XQ_2Y\bar Q_1$ and $\overline{\langle X,S_{\bar Q_2,\bar Q_1}Y\rangle_{*}}=\bar X\bar Q_2\bar Y Q_1$, while $\langle S_{Q_1,Q_2}X,Y\rangle_{*}=Q_1\bar X\bar Q_2\bar Y$; the two agree by the commutativity of the plain product. For $L_{Q}$, $\langle L_{Q}X,Y\rangle_{*}=Q\bar X\bar Y$ and $\overline{\langle X,L_{Q}Y\rangle_{*}}=\overline{X\overline{Q\bar Y}}=\bar X Q\bar Y$; the two agree. For $R_{Q}$, $\langle R_{Q}X,Y\rangle_{*}=X\bar Q\bar Y$ and $\langle X,L^{\mathrm{alg}}_{Q}Y\rangle_{*}=X\overline{QY}=X\bar Q\bar Y$. The adjoint of the involution itself is ${}^{*}$, since $\langle \bar X,Y\rangle_{*}=\bar X\bar Y=\overline{\langle X,\bar Y\rangle_{*}}$.

**Remark (the operator form of the sandwich).** The sandwich is the general two-sided operator of the sesquilinear structure; it contains the two one-sided families at $Q_1=1$ and $Q_2=1$, $S_{1,Q_2}=R_{Q_2}\circ{}^{*}$ and $S_{Q_1,1}=L_{Q_1}$, and it contains the involution at $Q_1=Q_2=1$, $S_{1,1}={}^{*}$. The general operator and the two families are *The Sesquilinear Sandwich Operator*; the complex instance is the present computation collapsed to one dimension.

## The Commutator and the Symmetrised Product

**Definition.** The **commutator** and the **symmetrised product** of the sesquilinear structure are

$$
[Q_1,Q_2]=Q_1\star Q_2-Q_2\star Q_1=Q_1\bar Q_2-Q_2\bar Q_1, \qquad Q_1\odot Q_2=Q_1\star Q_2+Q_2\star Q_1=Q_1\bar Q_2+Q_2\bar Q_1 .
$$

**Theorem.** For all $Q_1,Q_2$,

$$
\boxed{\;[Q_1,Q_2]=2i\operatorname{Im}(Q_1\bar Q_2), \qquad Q_1\odot Q_2=2\operatorname{Re}(Q_1\bar Q_2)\;}.
$$

In particular the commutator is purely imaginary and the symmetrised product is real; the commutator is the imaginary part of the Hermitian form and the symmetrisation its real part, each doubled.

**Proof.** For a complex number $Q_1\bar Q_2$ one has $Q_1\bar Q_2=\operatorname{Re}(Q_1\bar Q_2)+i\operatorname{Im}(Q_1\bar Q_2)$ and $\overline{Q_1\bar Q_2}=\operatorname{Re}(Q_1\bar Q_2)-i\operatorname{Im}(Q_1\bar Q_2)$; and $Q_2\bar Q_1=\overline{Q_1\bar Q_2}$. Adding and subtracting gives the two displays.

**Proposition.** The commutator is alternating, $[Q,Q]=0$, and $\mathbb{R}$-bilinear; its values lie in $i\mathbb{R}$. The symmetrised product is real-valued, symmetric, and $\mathbb{R}$-bilinear.

**Proof.** Alternation and the value set are read on $[Q_1,Q_2]=2i\operatorname{Im}(Q_1\bar Q_2)$; the real-bilinearity is the real-bilinearity of the real and imaginary parts of the sesquilinear product, which is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second.

**Theorem (the Jacobi identity holds).** The commutator is an antisymmetric $\mathbb{R}$-bilinear bracket on the two-dimensional real space, valued in $i\mathbb{R}$ and of centre $\{0\}$; with it, $\mathbb{C}$ is the two-dimensional non-abelian Lie algebra, and the **Jacobi identity** holds:

$$
[[Q_1,Q_2],Q_3]+[[Q_2,Q_3],Q_1]+[[Q_3,Q_1],Q_2]=0 \qquad \text{for all } Q_1,Q_2,Q_3 \in \mathbb{C}.
$$

**Proof.** Alternation is $[Q,Q]=0$; bilinearity is the real-bilinearity of the real and imaginary parts of $Q_1\bar Q_2$; the value set is $[Q_1,Q_2]=2i\operatorname{Im}(Q_1\bar Q_2)$. Write $[Q_1,Q_2]=-2\omega(Q_1,Q_2)\,i$ with the area form $\omega(Q_1,Q_2)=q_1q'_2-q'_1q_2$. Since $i$ is central in the algebra and $[i,Q_3]=i\bar Q_3-Q_3\bar i=2i\operatorname{Re}(Q_3)$, the cyclic sum is

$$
-4i\bigl(\omega(Q_1,Q_2)\operatorname{Re}(Q_3)+\omega(Q_2,Q_3)\operatorname{Re}(Q_1)+\omega(Q_3,Q_1)\operatorname{Re}(Q_2)\bigr),
$$

and the parenthesis is $q_1q'_2q_3-q'_1q_2q_3+q_2q'_3q_1-q'_2q_3q_1+q_3q'_1q_2-q'_3q_1q_2=0$, the six terms cancelling in pairs. The centre is the kernel of the area form, which is $\{0\}$ because $\omega$ is non-degenerate.

**Remark (why the identity holds, and what collapses).** The identity is not an accident of $\mathbb{C}$ and not a coincidence of the computation. On a **two-dimensional** real space every antisymmetric bilinear bracket satisfies it, whatever its values: a contributing triple must repeat an argument, and the two resulting terms are opposite. The failure of the Jacobi identity is a phenomenon of dimension at least three, and the complex space is too small to exhibit it. What collapses on $\mathbb{C}$ is the antisymmetric layer and not the commutator: the algebra is commutative, so the class-preserving antisymmetrisation $\tfrac12(Q_1\bar Q_2-\bar Q_2 Q_1)$ vanishes identically. What plays the role of a failed identity here is the **associator** of the binary product, $[Q_1,Q_2,Q_3]=Q_1\bar Q_2(\bar Q_3-Q_3)$; the ternary product repairs it. The symmetrised product does not collapse: it is the real part of $\langle\cdot,\cdot\rangle_{*}$ and survives as the symmetric half of the sesquilinear split.

## Summary

The sesquilinear product $Q_1\star Q_2=Q_1\bar Q_2$ is $\mathbb{C}$-linear in the first slot and conjugate-linear in the second; it has the right unit $1$ and no left unit; it is neither associative nor commutative, and it is conjugate-commutative, $Q_1\star Q_2=\overline{Q_2\star Q_1}$. Its associator is $[Q_1,Q_2,Q_3]=Q_1\bar Q_2(\bar Q_3-Q_3)$, nonzero but confined to the anti-self-adjoint part of the third slot; its ternary product $\{Q_1,Q_2,Q_3\}=Q_1\bar Q_2 Q_3$ is symmetric in the outer slots, Hermitian-symmetric and satisfies the Jordan triple identity, which makes the structure a $J^{*}$-algebra. The left multiplications are conjugate-linear and do not close under composition, their composite being the ordinary left multiplication $L^{\mathrm{alg}}_{Q_1\bar Q_2}$; the right multiplications are linear and close in the forward order, so that $Q\mapsto R_{Q}$ is an isomorphism of the multiplicative monoid of the field onto the right family. The sandwich $S_{Q_1,Q_2}=R_{Q_2}\circ L_{Q_1}$ has adjoint $S_{Q_1,Q_2}^{\dagger}=S_{\bar Q_2,\bar Q_1}$ with respect to the Hermitian form; the one-sided adjoints are $L_{Q}^{\dagger}=L_{Q}$ and $R_{Q}^{\dagger}=L^{\mathrm{alg}}_{Q}$. The commutator $[Q_1,Q_2]=2i\operatorname{Im}(Q_1\bar Q_2)$ is purely imaginary and alternating, and the Jacobi identity holds on it; the symmetrised product $Q_1\odot Q_2=2\operatorname{Re}(Q_1\bar Q_2)$ is the real part of the form. The product read as a form is *The Hermitian Form and the Positivity of the Complexoid Algebra*, below this article in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_1\star Q_2=Q_1\bar Q_2$ | the sesquilinear product, written with the star-nothing convention $Q_1\bar Q_2$ |
| $L_{Q}$, $R_{Q}$ | the sesquilinear left and right multiplications, $Q\bar X$ and $X\bar Q$ |
| $L^{\mathrm{alg}}_{Q}$ | the ordinary left multiplication of the field, $L^{\mathrm{alg}}_{Q}(X)=QX$ |
| $S_{Q_1,Q_2}$ | the sesquilinear sandwich, $S_{Q_1,Q_2}(X)=Q_1\bar X\bar Q_2$ |
| $T_{Q_1,Q_2}$ | the ordinary two-sided multiplication, $T_{Q_1,Q_2}(X)=Q_1XQ_2$ |
| $Q_1\star Q_2\star Q_3$ | the binary product iterated, $(Q_1\star Q_2)\star Q_3=Q_1\bar Q_2\bar Q_3$ |
| $\{Q_1,Q_2,Q_3\}$ | the ternary product, $(Q_1\star Q_2)\star\bar Q_3=Q_1\bar Q_2 Q_3$ |
| $[Q_1,Q_2,Q_3]$ | the associator, $(Q_1\star Q_2)\star Q_3-Q_1\star(Q_2\star Q_3)$ |
| $[Q_1,Q_2]$ | the commutator, $Q_1\bar Q_2-Q_2\bar Q_1=2i\operatorname{Im}(Q_1\bar Q_2)$ |
| $Q_1\odot Q_2$ | the symmetrised product, $Q_1\bar Q_2+Q_2\bar Q_1=2\operatorname{Re}(Q_1\bar Q_2)$ |
| ${}^{\dagger}$ | the adjoint with respect to $\langle\cdot,\cdot\rangle_{*}$, written on operators and never on elements |

## Further Reading

- Max Koecher, *The Minnesota Notes on Jordan Algebras and Their Applications*, Lecture Notes in Mathematics 1710 (Springer, 1999), for Jordan triple systems and the Jordan triple identity.
- Erhard Neher, "Jordan triple systems by the grid approach", *Lecture Notes in Mathematics* 1280 (Springer, 1987), for the structure theory the ternary product of the sesquilinear structure satisfies.
- Harald Hanche-Olsen and Erling Størmer, *Jordan Operator Algebras* (Pitman, 1984), for $J^{*}$-algebras and the axioms of the sesquilinear square.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for associators, non-associative products and conjugate-linear maps.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Dover, 1995), for the associator and the ternary products of a non-associative algebra.

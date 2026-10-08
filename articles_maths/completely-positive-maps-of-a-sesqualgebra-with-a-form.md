# __Completely Positive Maps of a Sesqualgebra with a Form__

## Introduction

A **positive map** of a sesqualgebra with a form is an $R$-linear map that carries the cone of the algebraic Hermitian squares into itself; it is **completely positive** when every **amplification** $\varphi \otimes \mathrm{id}_{n}$ on the algebra $M_{n}(A)$ of matrices over $A$ is again positive. The definition is the order-theoretic analogue of the boundedness of an operator, and in the model $A = M_{n}(\mathbb{C})$ with the trace form the completely positive maps are exactly the **Kraus maps** $\varphi(X) = \sum_{i}V_{i}XV_{i}^{*}$; the **Hermitian sandwich** $\Theta_{a}(x) = axa^{*}$ is the Kraus map of rank one, and the **unitary channels** $\Theta_{u}$ with $u$ unitary are the inner automorphisms of the form, which preserve the form's unitary group. The article is the capstone of the operator theory of the layer: after the adjoint, the unitaries, the self-adjoint splitting, the spectra and the polar decomposition, the completely positive maps are the maps that preserve the order of the cone, and the sandwich is the smallest of them.

Three facts organise the article. The **sandwich is completely positive, and this needs no positivity hypothesis**: the identity $\Theta_{a}(y^{*}y) = (ya^{*})^{*}(ya^{*})$ shows that the sandwich carries a Hermitian square to a Hermitian square, and the amplified sandwich is the sandwich by the diagonal matrix $\mathrm{diag}(a,\dots,a)$, so the amplification is positive for every $n$. The **model theorem is Choi's**: for $A = M_{n}(\mathbb{C})$ with the trace form a map is completely positive exactly when it is a sum of sandwiches $\sum_{i}\Theta_{V_{i}}$, and the least number of terms in such a sum is the **Kraus rank**, equal to the rank of the Choi matrix. And **positivity is strictly weaker than complete positivity**: the transpose of $M_{2}(\mathbb{C})$ is positive and not completely positive, its Choi matrix being the flip operator with the eigenvalues $+1$ and $-1$, so the amplification is what the word "completely" adds.

The article defines the order of the cone and the positive and completely positive maps, proves the complete positivity of the sandwich, states the Choi–Kraus theorem in the model with its Choi matrix, develops the unital and the unitary channels and their relation to the inner automorphisms of the form, and works the field and the matrices. The positivity and the cone are *Positivity and the Positive Cone of a Hermitian Form* and *Hermitian Squares and the Algebraic Positive Cone*; the sandwich is *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint* read in the sesquilinear layer; the inner automorphisms are *The Adjoint under a Hermitian Form*, §*The Inner Automorphisms*; the bilinear counterpart is *Completely Positive Maps of a Hilbert Algebra with Hermitian Adjoint*. Throughout, $A$ is a sesqualgebra with a form over a base $(R,\varsigma)$ of one of the two classical kinds of *The Norm Defined by a Form*, with fixed field $k = R^{\varsigma}$ and $R$ complete, $h$ is Hermitian, compatible and nonsingular, the maps are $R$-linear and carry $A$ into itself, and in the model theorem $A = M_{n}(\mathbb{C})$ with the star of the conjugate transpose and the trace form.

## The Positive Maps

### The Order of the Cone

By *Positivity and the Positive Cone of a Hermitian Form*, §*The Algebraic Cone and the Positive Functionals*, and *Hermitian Squares and the Algebraic Positive Cone*, §*The Order*, the **positive cone** of the algebra is the set of the finite sums of the Hermitian squares $x^{*}x$, and the **order** of the Hermitian part is the order of that cone: an element is **positive** when it lies in the cone, and $u \leq v$ when $v - u$ is positive. The order is read by the positive functionals of *Positive Definite Forms and the Order*, and the cone is stable under conjugation by the elements of the algebra by the identity $(ya^{*})^{*}(ya^{*}) = a\,y^{*}y\,a^{*}$.

### The Positive Maps

**Definition.** An $R$-linear map $\varphi : A \to A$ is **positive** when it carries the positive cone into itself: $\varphi(u)$ is positive for every positive $u$.

**Proposition (the sandwich is positive).** For every $a \in A$ the Hermitian sandwich

$$
\Theta_{a}(x) = a\,x\,a^{*}
$$

is $R$-linear, and it is positive; indeed it carries every Hermitian square to a Hermitian square,

$$
\Theta_{a}(y^{*}y) = (ya^{*})^{*}(ya^{*}) ,
$$

and the two sides are equal as elements of $A$.

*Proof.* The linearity is the linearity of the two multiplications. The identity is the computation $a y^{*}y a^{*} = (ya^{*})^{*}(ya^{*})$, using $(ya^{*})^{*} = a y^{*}$; the right side is a Hermitian square, hence positive, so the sandwich carries the generators of the cone into the cone, and it carries their sums into sums by its additivity. $\square$

**Remark (the positivity of the map is not the positivity of the operator).** The proposition is a statement about the **order** of the algebra and not about the sign of the form: $\Theta_{a}$ is order-positive for every $a$, while it is a positive *operator*, $h(\Theta_{a}x,x) \geq 0$ for all $x$, only under further hypotheses. It is self-adjoint for the form only when $a$ is Hermitian, and even then it need not be positive: on $M_{2}(\mathbb{C})$ with the trace form take $a = \operatorname{diag}(1,-1)$ and $x = E_{12}$, so that $\Theta_{a}(x) = -E_{12}$ and $h(\Theta_{a}x,x) = -1$. The two notions of positivity — the order of the cone and the sign of the form — are distinct, and the interest of the completely positive maps is that they belong to the first.

## Amplification and Complete Positivity

### The Amplified Form

**Definition.** On the algebra $M_{n}(A)$ of the $n \times n$ matrices over $A$, with the entrywise product, the involution $(a_{ij})^{*} = (a_{ji}^{*})$ and the form defined by

$$
h_{n}\bigl((a_{ij}),(b_{ij})\bigr) = \sum_{i,j=1}^{n} h(a_{ij},b_{ij}) .
$$

**Proposition (the amplified form is compatible).** If $h$ is Hermitian, compatible and nonsingular, then $h_{n}$ is Hermitian, compatible and nonsingular.

*Proof.* The Hermitian property is the sum of the Hermitian properties of the entries. For the compatibility, let $(XY)_{ij} = \sum_{k}x_{ik}y_{kj}$ be the product; then

$$
h_{n}(XY,Z) = \sum_{i,j,k} h(x_{ik}y_{kj}, z_{ij}) = \sum_{i,j,k} h(y_{kj}, x_{ik}^{*}z_{ij}) = h_{n}(Y, X^{*}Z) ,
$$

which is the compatibility of $h_{n}$. For the nonsingularity, an element of the radical of $h_{n}$ tested against the matrices with a single nonzero entry has every entry in the radical of $h$, so the radical of $h_{n}$ vanishes when that of $h$ does. $\square$

### The Definition

**Definition.** The **amplification** of an $R$-linear map $\varphi : A \to A$ is the map

$$
\varphi \otimes \mathrm{id}_{n} : M_{n}(A) \to M_{n}(A) , \qquad (a_{ij}) \mapsto (\varphi(a_{ij})) ,
$$

acting entrywise. The map $\varphi$ is **$n$-positive** when its amplification is positive, and **completely positive** when it is $n$-positive for every $n \geq 1$.

The terminology is the one of the bilinear layer, and the amplified map is the natural extension of the map to the matrices over the algebra; the amplification is not the tensor product of two algebras but the entrywise action, which is the only one that makes sense for a map that is not an algebra homomorphism.

### The Sandwich Is Completely Positive

**Theorem (the sandwich is completely positive).** For every $a \in A$ the sandwich $\Theta_{a}$ is completely positive, and its amplification is the sandwich by the diagonal matrix,

$$
\Theta_{a} \otimes \mathrm{id}_{n} = \Theta_{\operatorname{diag}(a,\dots,a)} .
$$

*Proof.* The amplification acts entrywise, $(\Theta_{a} \otimes \mathrm{id}_{n})(x_{ij}) = (a x_{ij}a^{*})$, and the sandwich by the diagonal matrix $\tilde a = \operatorname{diag}(a,\dots,a)$ is $(\tilde a X \tilde a^{*})_{ij} = a x_{ij}a^{*}$, which is the same. The amplified sandwich is positive by the positivity of the sandwich applied to $M_{n}(A)$ with the form $h_{n}$, whose cone is the cone of that algebra. $\square$

**Corollary (the sandwich is a channel of Kraus rank one).** The sandwich is the composition of the left multiplication and the right multiplication of *The Adjoint under a Hermitian Form*, §*The Multiplications*, $\Theta_{a} = m_{a} \circ R_{a}$ with $m_{a}(x) = ax$ and $R_{a}(x) = xa^{*}$,

$$
\Theta_{a} = m_{a} \circ R_{a} ,
$$

and its adjoint for the form is $\Theta_{a}^{\dagger} = \Theta_{a^{*}}$, so the sandwich is self-adjoint as an operator exactly when $a$ is Hermitian, while it is a positive map for every $a$.

*Proof.* The composition is $x \mapsto a(xa^{*}) = axa^{*}$, which is the sandwich. The adjoint is $R_{a}^{\dagger}m_{a}^{\dagger} = R_{a^{*}}m_{a^{*}}$, which is $x \mapsto a^{*}xa = \Theta_{a^{*}}(x)$, using the adjoint formulas $m_{x}^{\dagger} = m_{x^{*}}$, $R_{b}^{\dagger} = R_{b^{*}}$. $\square$

## Choi's Theorem and the Kraus Form

### The Kraus Form

**Definition.** A map $\varphi : M_{n}(\mathbb{C}) \to M_{n}(\mathbb{C})$ is a **Kraus map** when there are matrices $V_{1},\dots,V_{r}$ with

$$
\varphi(X) = \sum_{i=1}^{r} V_{i}XV_{i}^{*} .
$$

The matrices $V_{i}$ are the **Kraus operators** and the least $r$ is the **Kraus rank** of $\varphi$.

**Theorem (the Kraus form is completely positive).** Every Kraus map is positive and completely positive.

*Proof.* The Kraus map is a sum of sandwiches $\Theta_{V_{i}}$, each of which is completely positive by the theorem above, and a sum of positive maps is positive. For the amplification, $(\varphi \otimes \mathrm{id}_{m})(X) = \sum_{i}(1_{m}\otimes V_{i})X(1_{m}\otimes V_{i})^{*}$ in the identification $M_{m}(M_{n}(\mathbb{C})) \cong M_{mn}(\mathbb{C})$, which is a Kraus map again, hence positive. $\square$

### Choi's Theorem in the Model

**Theorem (Choi's theorem).** A map $\varphi : M_{n}(\mathbb{C}) \to M_{n}(\mathbb{C})$ is completely positive if and only if it is a Kraus map, and then the Kraus rank is the rank of the **Choi matrix**

$$
C_{\varphi} = \sum_{i,j=1}^{n} E_{ij} \otimes \varphi(E_{ij}) ,
$$

the block matrix whose positivity is the complete positivity of $\varphi$ and whose rank is the least number of Kraus operators.

*Proof.* The theorem is the finite-dimensional Choi–Kraus theorem for a map of a matrix algebra. The reconstruction $\varphi(X) = \sum_{i,j}X_{ij}\varphi(E_{ij})$ shows that $\varphi$ is determined by the images of the matrix units, and the columns of the Choi matrix are those images arranged in blocks; a decomposition $C_{\varphi} = VV^{*}$ with $V$ of $r$ columns reads the columns of $V$ as the Kraus operators, and the positivity of $C_{\varphi}$ is the existence of such a decomposition by the spectral theorem. $\square$

**Example (the sandwich has rank one).** The Choi matrix of the sandwich $\Theta_{a}$ on $M_{n}(\mathbb{C})$ is the rank-one matrix $\lvert a\rangle\langle a\rvert$ in the vectorised basis, $C_{\Theta_{a}} = \mathrm{vec}(a)\,\mathrm{vec}(a)^{*}$, so the Kraus rank of the sandwich is one and every completely positive map of the model is a sum of sandwiches. The example is the reason the sandwich is the elementary completely positive map of the layer.

### Positivity Is Strictly Weaker than Complete Positivity

**Theorem (the transpose).** The transpose $\varphi(X) = X^{T}$ of $M_{2}(\mathbb{C})$ is positive and not completely positive.

*Proof.* The transpose is positive: $X \geq 0$ implies $X^{T} \geq 0$. Its Choi matrix in the basis of the matrix units is $\sum_{i,j}E_{ij} \otimes E_{ij}^{T} = \sum_{i,j}E_{ij}\otimes E_{ji}$, the flip operator, whose eigenvalues are $+1$ on the symmetric part and $-1$ on the antisymmetric part; the negative eigenvalue makes the Choi matrix not positive semi-definite, so by Choi's theorem the map is not completely positive. $\square$

## Channels with a Form

### Unital and Multiplicative Channels

**Theorem (the classification of the sandwich).** For $a \in A$ on a unital object,

$$
\Theta_{a}(1) = a\,a^{*} , \qquad \Theta_{a}(x)\Theta_{a}(y) = a\,x\,(a^{*}a)\,y\,a^{*} ,
$$

so the sandwich is **unital**, $\Theta_{a}(1) = 1$, exactly when $a a^{*} = 1$; it is **multiplicative**, $\Theta_{a}(xy) = \Theta_{a}(x)\Theta_{a}(y)$, as soon as $a^{*}a = 1$, and in the matrix model the converse holds for $a \neq 0$; and it is an **automorphism** of the algebra exactly when $a$ is unitary, in which case $\Theta_{a} = \alpha_{a}$ is the inner automorphism by $a$.

*Proof.* The two identities are the definitions. If $a^{*}a = 1$ then $\Theta_{a}(x)\Theta_{a}(y) = a x (a^{*}a) y a^{*} = axya^{*} = \Theta_{a}(xy)$, so the sandwich is multiplicative. Conversely in the matrix model a nonzero multiplicative sandwich is a nonzero endomorphism of $M_{n}(\mathbb{C})$, hence injective because the matrix algebra is simple, and injectivity of $\Theta_{a}$ forces $a$ invertible: if $av = 0$ for some $v \neq 0$, then $\Theta_{a}(vw^{*}) = avw^{*}a^{*} = 0$ for every $w$. Then $a^{*}a = 1$, and an invertible $a$ with $a^{*}a = 1$ is unitary. Multiplicativity alone does not force $a^{*}a = 1$ in a general object, the zero sandwich $\Theta_{0} = 0$ being multiplicative with $0^{*}0 = 0$; the two conditions are often conflated, and the reader is warned. The unitary case is the conjunction of $aa^{*} = 1$ and $a^{*}a = 1$, and then $\Theta_{a}(x) = axa^{*} = axa^{-1}$ is the inner automorphism of *The Adjoint under a Hermitian Form*, §*The Inner Automorphisms*; conversely an automorphism is a bijective sandwich, so $a$ is invertible with $a^{*}a = 1$, that is $a$ is unitary. $\square$

### The Unitary Channels

**Theorem (the unitary channels form a group).** The assignment $u \mapsto \Theta_{u}$ is a homomorphism from the unitary group $U(A,h)$ into the group of the $*$-automorphisms of $A$; its image is the group of the inner automorphisms by the unitary elements, and each $\Theta_{u}$ is a completely positive channel that is **unitary as an operator of the form**, hence preserves the form, $h(\Theta_{u}x,\Theta_{u}y) = h(x,y)$.

*Proof.* The composition law $\Theta_{u}\Theta_{v} = \Theta_{uv}$ is *The Hermitian Sandwich on a Hilbert Algebra with Hermitian Adjoint* read in the sesquilinear layer, and it is the same identity as the multiplicativity above; each $\Theta_{u}$ preserves the involution, $\Theta_{u}(x^{*}) = ux^{*}u^{*} = (uxu^{*})^{*} = \Theta_{u}(x)^{*}$, so it is a $*$-automorphism, and it is inner because $u$ is invertible. For the form, the adjoint of the sandwich is $\Theta_{u}^{\dagger} = \Theta_{u^{*}}$ by the corollary above, so $\Theta_{u}^{\dagger}\Theta_{u} = \Theta_{u^{*}}\Theta_{u} = \Theta_{u^{*}u} = \Theta_{1} = \mathrm{id}$ and symmetrically $\Theta_{u}\Theta_{u}^{\dagger} = \mathrm{id}$; the operator $\Theta_{u}$ is therefore unitary in the sense of *Unitary and Isometric Operators of the Form*, §*The Equivalences*, and a unitary operator preserves the form by its definition. $\square$

**Remark (channels and states).** The positive maps of the layer are the order-preserving maps of the cone, the completely positive ones the maps whose amplifications are order-preserving, and the unital ones are the **channels**; the composition of two channels is a channel, the identity is a channel, and the unitary channels are the invertible ones. The order-theoretic refinement of the layer is the statement that the channels form a monoid and the unitary channels a subgroup, and it is the noncommutative measure theory of *Completely Positive Maps of a Hilbert Algebra with Hermitian Adjoint* read for a compatible sesquilinear form.

## Worked Cases

### The Field

**Example (the field).** Let $A = \mathbb{C}$ with $h(z,w) = z\overline{w}$. An $R$-linear map is $\varphi(z) = \mu z$ for a complex $\mu$, and it is positive exactly when $\mu \geq 0$: the cone of the algebra is the set of the squares $z\overline{z} = \lvert z\rvert^{2} \geq 0$, and $\mu\lvert z\rvert^{2}$ must stay nonnegative for every $z$. Every positive map is a Kraus map of rank one, $\varphi = \Theta_{a}$ with $a = \sqrt{\mu}$, and it is completely positive because the amplification is the sandwich by $\sqrt{\mu}$ on the diagonal. The example is the smallest in which positivity and complete positivity coincide, and the coincidence is the reason a scalar map has no "quantum" obstruction.

### The Matrices

**Example (the matrices).** Let $A = M_{n}(\mathbb{C})$ with the trace form $h(X,Y) = \operatorname{tr}(XY^{*})$. The sandwich $\Theta_{a}(X) = aXa^{*}$ is completely positive of Kraus rank one by the general theorem, its Choi matrix is $\lvert a\rangle\langle a\rvert$, and it is unital exactly when $aa^{*} = 1$ and multiplicative exactly when $a = 0$ or $a^{*}a = 1$ (the zero sandwich being multiplicative too); the inner automorphisms of the trace form are the channels $\Theta_{u}$ with $u$ unitary, which are exactly the $*$-automorphisms of the matrix algebra that preserve the trace form. The transpose $X \mapsto X^{T}$ is the standard positive and not completely positive map, its Choi matrix being the flip operator. The example is the model of the article and the smallest in which all the phenomena — the sandwich, the Kraus form, the rank, the channels and the obstruction — are visible.

## Summary

A map of a sesqualgebra with a form is **positive** when it carries the **cone of the Hermitian squares** into itself and **completely positive** when every **amplification** $\varphi \otimes \mathrm{id}_{n}$ on $M_{n}(A)$ with the amplified compatible form $h_{n}$ is positive. The **Hermitian sandwich** $\Theta_{a}(x) = axa^{*}$ is completely positive and needs no positivity hypothesis, because it carries a Hermitian square to a Hermitian square, $\Theta_{a}(y^{*}y) = (ya^{*})^{*}(ya^{*})$, and its amplification is the sandwich by $\operatorname{diag}(a,\dots,a)$; its adjoint is $\Theta_{a}^{\dagger} = \Theta_{a^{*}}$, so it is self-adjoint exactly when $a$ is Hermitian. In the model $M_{n}(\mathbb{C})$ with the trace form the completely positive maps are the **Kraus maps** $\sum_{i}V_{i}XV_{i}^{*}$ by **Choi's theorem**, the Kraus rank being the rank of the **Choi matrix**, and the sandwich is the rank-one case. **Positivity is strictly weaker** than complete positivity: the transpose is positive and not completely positive. The sandwich is **unital** exactly when $aa^{*} = 1$, **multiplicative** as soon as $a^{*}a = 1$ (and in the matrix model exactly when $a = 0$ or $a^{*}a = 1$), and an **automorphism** exactly when $a$ is unitary, in which case it is the inner automorphism $\alpha_{a}$; the **unitary channels** form a subgroup of the channel monoid, and they are the inner automorphisms by the unitary elements.

## Summary of Notation

| symbol | meaning |
|---|---|
| $x^{*}x$ | a Hermitian square, the generator of the positive cone |
| $\Theta_{a}(x) = axa^{*}$ | the Hermitian sandwich |
| $\Theta_{a}(y^{*}y) = (ya^{*})^{*}(ya^{*})$ | the sandwich carries a square to a square |
| $h_{n}((a_{ij}),(b_{ij})) = \sum_{i,j}h(a_{ij},b_{ij})$ | the amplified form on $M_{n}(A)$ |
| $\varphi \otimes \mathrm{id}_{n}$ | the amplification of a map |
| $\varphi$ completely positive | $\varphi \otimes \mathrm{id}_{n}$ is positive for every $n$ |
| $\Theta_{a} = m_{a} \circ R_{a}$ | the sandwich is a left and a right multiplication |
| $\Theta_{a}^{\dagger} = \Theta_{a^{*}}$ | the adjoint of the sandwich |
| $\varphi(X) = \sum_{i}V_{i}XV_{i}^{*}$ | the Kraus form of a completely positive map |
| $C_{\varphi} = \sum_{i,j}E_{ij}\otimes\varphi(E_{ij})$ | the Choi matrix, positive iff $\varphi$ is completely positive |
| $C_{\Theta_{a}} = \lvert a\rangle\langle a\rvert$ | the Choi matrix of the sandwich has rank one |
| $\Theta_{a}(1) = aa^{*}$, $\Theta_{a}(xy) = \Theta_{a}(x)\Theta_{a}(y)$ if $a^{*}a = 1$ | the unital and the multiplicative sandwiches |
| $\Theta_{u}$, $u$ unitary | the unitary channels, the inner automorphisms |

## Further Reading

- Man-Duen Choi, *Completely positive linear maps on complex matrices*, Linear Algebra and its Applications **10** (1975), 285–290, for the Choi matrix and the characterisation of the completely positive maps.
- Karl Kraus, *States, Effects, and Operations* (Lecture Notes in Physics 190, Springer, 1983), for the Kraus operators and the completely positive maps of a matrix algebra.
- Erling Størmer, *Positive Linear Maps of Operator Algebras* (Springer Monographs in Mathematics, 2013), for the positive and completely positive maps of an operator algebra and the order of the cone.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras I* (Academic Press, 1983), for the positive elements of an algebra with involution and the order they define.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the sandwich maps, the inner automorphisms of an algebra with involution and the conjugations.
- Israel Gohberg, Peter Lancaster and Leiba Rodman, *Indefinite Linear Algebra and Applications* (Birkhäuser, 2005), for the positive maps and the cones attached to an indefinite form.

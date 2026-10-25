# __The Adjoint Operators of the Antisymmetric Quaternionic Sesqualgebra__

## Introduction

To an element $\tilde Q_3$ of the antisymmetric quaternionic sesqualgebra of *Introduction to the Antisymmetric Quaternionic Sesqualgebra* the block attaches the left multiplication

$$
L_{\tilde Q_3}\tilde Q_2=\tilde Q_3\diamond\tilde Q_2=\vec Q_3\times\overline{\vec R},
$$

the map that pairs $\tilde Q_3$ with the second slot of the multiplication. The map is **conjugate-linear** in $\tilde Q_2$, since it is the composition of the coefficient conjugation with a complex-linear map, and this single fact removes the ordinary operator calculus from the block: the left multiplications do not form an associative algebra of operators, the map $\tilde Q_3\mapsto L_{\tilde Q_3}$ is $\mathbb{C}$-linear in the parameter (the first slot is the linear one) while the operator itself is conjugate-linear in its argument, and the adjoint with respect to the form of the block is again conjugate-linear. This article reads the operators one by one. The **left multiplication** is described with its matrix in the real basis, its rank, its kernel and its image. The **adjoint** with respect to the Krein form is then computed, in the class of conjugate-linear maps, and it turns out to be the negative of the operator itself. The **derivations** of the block are computed, and they form the direct sum of the endomorphisms of the centre and of the three-dimensional real skew maps of the vector parts; from them the **structure group** of the block, the group of invertible linear maps preserving the multiplication, is read. The **composition** of two left multiplications is finally computed, and with it the conjugate-linear invariants of the block. The reading runs parallel to the operator articles of the two algebras and of the two sesqualgebras, and it is the operator side of the multiplication.

The block is *Introduction to the Antisymmetric Quaternionic Sesqualgebra*; its pairing with the form is *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*; its diagonal and the failure of the Jacobi identity are *The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra*; the general construction of the parts is *The Symmetric and Antisymmetric Parts of a Sesqualgebra Product*; and the form is *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*. This article owns the operators of the block.

## The Left Multiplication

### The Rule and the Class

**Definition.** The **left multiplication** by $\tilde Q_3$ is $L_{\tilde Q_3}\tilde Q_2=\tilde Q_3\diamond\tilde Q_2=\vec Q_3\times\overline{\vec R}$.

**Proposition.** The left multiplication is **conjugate-linear**:

$$
L_{\tilde Q_3}(\tilde Q_2+\tilde Q_4)=L_{\tilde Q_3}\tilde Q_2+L_{\tilde Q_3}\tilde Q_4,\qquad
L_{\tilde Q_3}(A\tilde Q_2)=\overline{A}\,L_{\tilde Q_3}\tilde Q_2\qquad(A\in\mathbb{C}),
$$

and it depends on $\tilde Q_3$ through $\vec Q_3$ alone.

*Proof.* The cross product $\vec Q_3\times\overline{\vec R}$ is additive in $\tilde Q_2$ and conjugate-linear in $\overline{\vec R}$; a central $\tilde Q_3$ has $\vec Q_3=0$ and the map is zero.

**Remark (the operator calculus is unavailable).** Because the first slot of the block is the linear one and the second the conjugate-linear one, the map $\tilde Q_3\mapsto L_{\tilde Q_3}$ is $\mathbb{C}$-linear in $\tilde Q_3$ while the operator is conjugate-linear in its argument, and the left multiplications do not close under composition into an algebra in the ordinary sense: the composition of two of them is complex-linear, as computed below, so the family of operators is a real vector space stable under composition into a different class, and not a complex algebra of operators. The block is not associative, so there is no regular representation of the kind carried by the algebras, and the reading is done with the single operators and their adjoints.

### The Matrix, the Rank and the Kernel

**Proposition (the matrix for a vector element).** For $\tilde Q_3=\vec e_x$, in the ordered real basis $(e_t,\vec e_x,\vec e_y,\vec e_z,ie_t,i\vec e_x,i\vec e_y,i\vec e_z)$ the map kills $e_t,\vec e_x,ie_t,i\vec e_x$ and acts as

$$
\vec e_y\mapsto \vec e_z,\quad \vec e_z\mapsto-\vec e_y,\quad i\vec e_y\mapsto-i\vec e_z,\quad i\vec e_z\mapsto i\vec e_y,
$$

so, on the vector subspace, its matrix is the conjugate-linear map given by the two-by-two skew block in the $(\vec e_y,\vec e_z)$ directions composed with the coefficient conjugation: $\vec e_y\mapsto \vec e_z$ while $i\vec e_y\mapsto-i\vec e_z=-\mathrm{i}\,\vec e_z$, so the map does not commute with $i$ and is conjugate-linear, as the class demands.

*Proof.* Direct evaluation of $\vec Q_3\times\overline{\vec R}$ at $\vec Q_3=\vec e_x$ on the real basis: $\vec e_x\times \vec e_y=\vec e_z$, $\vec e_x\times \vec e_z=-\vec e_y$, $\vec e_x\times(i\vec e_y)=-i\vec e_z$, $\vec e_x\times(i\vec e_z)=i\vec e_y$, and $\vec e_x\times \vec e_x=0$, with the centre killed.

**Theorem (the rank, the kernel and the image).** For a nonzero vector element $\tilde Q_3$ with $\vec Q_3\neq0$,

$$
\boxed{\;
\ker L_{\tilde Q_3}=\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3},\qquad
\mathrm{im}\,L_{\tilde Q_3}=\{\vec V\in\mathrm{Vect}(\mathbb{B}):(\vec Q_3,\vec V)=0\}
\;},
$$

the centre direct sum a complex line in the kernel, and the complex two-dimensional subspace orthogonal to $\vec Q_3$ for the bilinear dot product in the image. The rank of $L_{\tilde Q_3}$ over $\mathbb{R}$ is $4$, its nullity is $4$, and its trace is $0$.

*Proof.* The equation $\vec Q_3\times\overline{\vec R}=0$ says that $\overline{\vec R}$ is a complex multiple of $\vec Q_3$, that is $\vec R\in\mathbb{C}\overline{\vec Q_3}$; together with the centre, killed by the map, this is the kernel, of real dimension $2+2=4$. The image is the set of cross products with the fixed vector $\vec Q_3$, which is the orthogonal complement of $\vec Q_3$ in the three complex dimensions, of real dimension $4$; the rank is therefore $4$, and the nullity is $8-4=4$. The trace is the sum of the diagonal entries, and each is zero in the basis above: the map is conjugate-linear on the whole space, $L_{\tilde Q_3}(\lambda\tilde Q_2)=\overline{\lambda}\,L_{\tilde Q_3}\tilde Q_2$, and a conjugate-linear map of the real space has zero real trace, its real matrix carrying a block $B$ along the real directions and the block $-B$ along the imaginary ones; concretely the $\vec R$-coefficient of $\vec Q_3\times\overline{\vec R}$ is $(\vec Q_3\times\overline{\vec R},\vec R)=0$ in the real directions, and the imaginary directions obey the same by conjugate-linearity.

**Remark (the kernel and the image are complex subspaces).** The kernel and the image of the left multiplication are complex subspaces of the complex space, even though the map itself is conjugate-linear: the kernel is the centre together with a complex line, and the image is the complex plane orthogonal to $\vec Q_3$. The conjugate-linearity of the map sends $i\tilde Q_2$ to $-i\,L_{\tilde Q_3}\tilde Q_2$, but the kernel and the image are stable under $i$, as the formulas show.

## The Adjoint with respect to the Form

**Definition.** For a conjugate-linear map $T$ of the space, its **adjoint** $T^{\dagger}$ is the conjugate-linear map with

$$
K\bigl(T\tilde Q_2,\tilde Q_4\bigr)=\overline{K\bigl(\tilde Q_2,T^{\dagger}\tilde Q_4\bigr)}
\qquad\text{for all }\tilde Q_2,\tilde Q_4,
$$

the conjugate on the right because both $K$ and $T$ are conjugate-linear, the two conjugations cancelling for the composite.

**Theorem.** The adjoint of the left multiplication is its negative:

$$ \boxed{\; L_{\tilde Q_3}^{\dagger}=-L_{\tilde Q_3} \;}, $$

a conjugate-linear map. Equivalently, $\langle\tilde Q_3\diamond\tilde Q_2,\tilde Q_4\rangle_{\natural*}=-\overline{\langle\tilde Q_2,\tilde Q_3\diamond\tilde Q_4\rangle_{\natural*}}$.

*Proof.* The left-hand side is $\langle\vec Q_3\times\overline{\vec R},\tilde Q_4\rangle_{\natural*}$, which reads $-\,(\vec Q_3\times\overline{\vec R},\overline{\vec Q_4})$; the right-hand side is $-\overline{\langle\tilde Q_2,\vec Q_3\times\overline{\vec Q_4}\rangle_{\natural*}}$, whose inner term reads $(\vec R,\overline{\vec Q_3\times\overline{\vec Q_4}})$, and conjugating gives $(\overline{\vec R},\vec Q_3\times\overline{\vec Q_4})$. The two sides are $-\det[\vec Q_3,\overline{\vec R},\overline{\vec Q_4}]$ and $\det[\overline{\vec R},\vec Q_3,\overline{\vec Q_4}]$, the two sign readings of the same triple product, and they agree.

**Remark (the adjoint is conjugate-linear, and this is settled).** The class of the adjoint is forced: a conjugate-linear map has a conjugate-linear adjoint with respect to a form that is conjugate-linear in one slot, and a linear adjoint would not satisfy the defining identity. The block settles the question in the corpus sense: the adjoint is read in the **conjugate-linear** class, and it is again the negative of the operator. An operator equal to the negative of its adjoint is the analogue for the block of a skew operator, and the relation is the operator form of the conjugate-alternation of the multiplication.

## The Derivations and the Structure Group

**Definition.** A **derivation** of the block is a real-linear map $D$ with

$$
D(\tilde Q_1\diamond\tilde Q_2)=D\tilde Q_1\diamond\tilde Q_2+\tilde Q_1\diamond D\tilde Q_2
\qquad\text{for all }\tilde Q_1,\tilde Q_2 .
$$

**Theorem (the derivations).** The derivations of the block form a real vector space of dimension $7$, the direct sum

$$ \boxed{\; \mathrm{Der}(\diamond)=\mathrm{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})\oplus\mathfrak{so}(3,\mathbb{R}) \;}, $$

where the first summand consists of the maps $\tilde Q_2\mapsto\lambda(Q_{2t})e_t$ for $\mathbb{R}$-linear $\lambda:\mathbb{C}\to\mathbb{C}$, of real dimension $4$, and the second consists of the complex-linear skew maps of the vector part with real entries, of real dimension $3$.

*Proof.* Let $D\tilde Q_2=\lambda(Q_{2t})e_t+D_V(\vec Q_2)$. Substituting into the defining identity and using that the block kills the centre in both slots, the centre part $\lambda$ cancels on both sides for every $\mathbb{R}$-linear $\lambda$, which gives the first summand. On the vector part, the identity reads $D_V(\vec Q_1\times\overline{\vec Q_2})=D_V\vec Q_1\times\overline{\vec Q_2}+\vec Q_1\times\overline{D_V\vec Q_2}$; taking $\vec Q_1,\vec Q_2$ real reduces it to $D_V(\vec Q_1\times\vec Q_2)=D_V\vec Q_1\times\vec Q_2+\vec Q_1\times D_V\vec Q_2$, the classical derivation condition for the cross product, whose solutions are the skew maps of $\mathbb{R}^{3}$; and taking one argument imaginary forces the entries to be real, so the second summand is $\mathfrak{so}(3,\mathbb{R})$, of real dimension $3$. The two summands are independent, and no derivation mixes the centre with the vector part, since a map carrying the centre into the vector part fails the identity on a real pair. The total dimension is $4+3=7$.

**Theorem (the structure group).** The group of invertible real-linear maps preserving the block contains the subgroup

$$
\bigl\{\tilde Q_2\mapsto\lambda(Q_{2t})e_t+g\vec Q_2\ :\ \lambda\in GL_{\mathbb{R}}(\mathbb{C}),\ g\in SO(3,\mathbb{R})\bigr\}\cong GL(2,\mathbb{R})\times SO(3,\mathbb{R}),
$$

of real dimension $4+3=7$; its Lie algebra is $\mathrm{Der}(\diamond)$.

*Proof.* For $\lambda\in GL_{\mathbb{R}}(\mathbb{C})$ and $g\in SO(3,\mathbb{R})$ the map is invertible, and $\lambda$ acts on the centre which the block kills, while $g(\vec Q_1\times\overline{\vec Q_2})=g\vec Q_1\times g\overline{\vec Q_2}=g\vec Q_1\times\overline{g\vec Q_2}$ for a real **orthogonal** map of determinant one (the real entries make $g$ commute with the conjugation), so the multiplication is preserved. The Lie algebra of the subgroup is the summand decomposition of the linearisation, which is $\mathrm{Der}(\diamond)$ by the preceding theorem: the skew maps $\mathfrak{so}(3,\mathbb{R})$ of the derivation are the linearisations of the determinant-one orthogonal maps. A reflection $g$ of determinant $-1$ reverses the cross product and fails the identity.

**Remark (the block is more symmetric than its class suggests).** The structure group is the product of the real-linear maps of the scalar coordinate and the real orthogonal maps of determinant one on the vector part; it does not act complex-linearly on the whole space, because $\lambda$ is only real-linear, while the vector-part factor, having real entries, is complex-linear and commutes with the conjugation. The group is the block's substitute for the group of the two algebras, and it is the group under which the conjugate cross product is invariant.

## The Composition and the Conjugate Invariants

**Theorem (the square of a left multiplication).** For all $\tilde Q_2$,

$$
L_{\tilde Q_3}^2\tilde Q_2=\overline{\vec Q_3}\,(\vec Q_3,\vec R)-(\vec Q_3,\overline{\vec Q_3})\,\vec R,
$$

a complex-linear map of the vector part, nonzero in general.

*Proof.* $L_{\tilde Q_3}^2\tilde Q_2=\vec Q_3\times\overline{\vec Q_3\times\overline{\vec R}}$, and expanding the double cross product gives $\overline{\vec Q_3}(\vec Q_3,\vec R)-(\vec Q_3,\overline{\vec Q_3})\vec R$.

**Remark (the composition of two left multiplications is complex-linear).** More generally $L_{\tilde Q_3}L_{\tilde Q_1}\tilde Q_2=\vec Q_3\times\overline{\vec Q_1\times\overline{\vec R}}$, and the two conjugations cancel, so the composition is $\mathbb{C}$-linear; the family of left multiplications is therefore a real vector space whose products are complex-linear, stable under no complex-linear algebra structure on a single class.

**Proposition (the operator and its conjugate).** Define the **conjugate** of the left multiplication by $\overline{L}_{\tilde Q_3}\tilde Q_2=\overline{L_{\tilde Q_3}\overline{\tilde Q_2}}$, again conjugate-linear. Then $\overline{L}_{\tilde Q_3}=L_{\overline{\vec Q_3}}$, and

$$
L_{\tilde Q_3}L_{\overline{\vec Q_3}}\tilde Q_2=\vec Q_3\times(\vec Q_3\times\vec R),\qquad
L_{\overline{\vec Q_3}}L_{\tilde Q_3}\tilde Q_2=\overline{\vec Q_3}\times(\overline{\vec Q_3}\times\vec R),
$$

both $\mathbb{C}$-linear.

*Proof.* By definition $\overline{L}_{\tilde Q_3}\tilde Q_2=\overline{\vec Q_3\times\overline{\overline{\tilde Q_2}}}=\overline{\vec Q_3}\times\overline{\tilde Q_2}=L_{\overline{\vec Q_3}}\tilde Q_2$. For the products, $L_{\tilde Q_3}L_{\overline{\vec Q_3}}\tilde Q_2=\vec Q_3\times\overline{\overline{\vec Q_3}\times\overline{\vec R}}=\vec Q_3\times(\vec Q_3\times\vec R)$, the inner conjugation cancelling the coefficient conjugation of $\vec Q_3$ and the one of the slot; the other product is the same with $\vec Q_3$ conjugated.

**Theorem (the conjugate invariant).** For all $\tilde Q_3,\tilde Q_2$,

$$
K\bigl(L_{\tilde Q_3}\tilde Q_2,L_{\tilde Q_3}\tilde Q_2\bigr)
=-\bigl|\vec Q_3\times\overline{\vec R}\bigr|^{2}\le0,
$$

and it vanishes exactly when $L_{\tilde Q_3}\tilde Q_2=0$.

*Proof.* The self-pairing of the pure vector $\vec Q_3\times\overline{\vec R}$ under the form, as in *The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra*.

**Remark (the invariants are conjugate-linear).** The invariant $\langle L_{\tilde Q_3}\tilde Q_2,L_{\tilde Q_3}\tilde Q_2\rangle_{\natural*}$ is a quadratic form in $\tilde Q_2$ read through the conjugation of the second slot, and it is the operator form of the negative definiteness of the form on the vector subspace. The block carries no invariant of the ordinary polynomial kind, since its second slot is conjugate-linear; the invariants are the conjugate-linear ones, and the operator admits the real structure of the space and no complex polynomial identity beyond the square above.

## Summary

The left multiplication $L_{\tilde Q_3}\tilde Q_2=\vec Q_3\times\overline{\vec R}$ is conjugate-linear, kills the centre, has rank $4$, nullity $4$ and trace $0$, with kernel $\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ and image the complex plane orthogonal to $\vec Q_3$; its adjoint with respect to the Krein form is its negative, $L_{\tilde Q_3}^{\dagger}=-L_{\tilde Q_3}$, in the conjugate-linear class that the block forces. The derivations of the block form the seven-dimensional real space $\mathrm{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})\oplus\mathfrak{so}(3,\mathbb{R})$, the scalar maps of the centre together with the real skew maps of the vector part, and the structure group contains $GL(2,\mathbb{R})\times SO(3,\mathbb{R})$ with that Lie algebra; a reflection of the vector part fails to preserve the block. The square of a left multiplication is the complex-linear map $\overline{\vec Q_3}(\vec Q_3,\vec R)-(\vec Q_3,\overline{\vec Q_3})\vec R$, the composition of two is complex-linear, and the conjugate invariant is $\langle L_{\tilde Q_3}\tilde Q_2,L_{\tilde Q_3}\tilde Q_2\rangle_{\natural*}=-|\vec Q_3\times\overline{\vec R}|^{2}\le0$. The operator calculus of the associative and the bilinear blocks is replaced at every step by the conjugate-linear class of the block.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_{\tilde Q_3}\tilde Q_2=\vec Q_3\times\overline{\vec R}$ | the left multiplication, conjugate-linear |
| $\ker L_{\tilde Q_3}=\mathbb{C}e_t\oplus\mathbb{C}\overline{\vec Q_3}$ | the kernel, of real dimension $4$ |
| $\mathrm{im}\,L_{\tilde Q_3}=\{\vec V:(\vec Q_3,\vec V)=0\}$ | the image, a complex plane |
| rank $4$, nullity $4$, trace $0$ | the invariants of the operator |
| $L_{\tilde Q_3}^{\dagger}=-L_{\tilde Q_3}$ | the adjoint, conjugate-linear |
| $\mathrm{Der}(\diamond)=\mathrm{End}_{\mathbb{R}}(\mathbb{C}_{\mathbb{B}})\oplus\mathfrak{so}(3,\mathbb{R})$ | the derivations, of real dimension $7$ |
| $GL(2,\mathbb{R})\times SO(3,\mathbb{R})$ | the structure group |
| $L_{\tilde Q_3}^2\tilde Q_2=\overline{\vec Q_3}(\vec Q_3,\vec R)-(\vec Q_3,\overline{\vec Q_3})\vec R$ | the square of the operator |
| $\overline{L}_{\tilde Q_3}=L_{\overline{\vec Q_3}}$, $L_{\tilde Q_3}L_{\overline{\vec Q_3}}\tilde Q_2=\vec Q_3\times(\vec Q_3\times\vec R)$ | the conjugate operator and the two products |
| $\langle L_{\tilde Q_3}\tilde Q_2,L_{\tilde Q_3}\tilde Q_2\rangle_{\natural*}=-\lvert\vec Q_3\times\overline{\vec R}\rvert^{2}$ | the conjugate invariant |

## Further Reading

- [Introduction to the Antisymmetric Quaternionic Sesqualgebra](introduction-to-the-antisymmetric-quaternionic-sesqualgebra.html), for the block.
- [The Sesquilinear Pairing of the Antisymmetric Quaternionic Sesqualgebra](the-sesquilinear-pairing-of-the-antisymmetric-quaternionic-sesqualgebra.html), for the form the adjoint is taken with respect to.
- [The Conjugate Cross Product and the Jacobi Failure of the Antisymmetric Quaternionic Sesqualgebra](the-conjugate-cross-product-and-the-jacobi-failure-of-the-antisymmetric-quaternionic-sesqualgebra.html), for the conjugate cross product and its cone.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the form and the vector subspace.
- [The Symmetric and Antisymmetric Parts of a Sesqualgebra Product](the-symmetric-and-antisymmetric-parts-of-a-sesqualgebra-product.html), for the general construction of a part.
- [Introduction to the Symmetric Quaternionic Sesqualgebra](introduction-to-the-symmetric-quaternionic-sesqualgebra.html), for the same operators in the two matrix models.

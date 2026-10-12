# __Annihilators__

## Introduction

An element annihilates a structure when multiplying by it kills the product on the whole space. The quaternion space carries six structures, so the question has six answers, and they are read here side by side. The article defines the left, the right and the two-sided annihilating set of a structure, proves them equal for each of the six, and compares the six sets. The answer is $\{0\}$ for five of the six and the scalar line for the cross product alone, and the comparison is the content. The products are *The Two General Products of the Quaternion $\mathbb{R}$ Space* and *The 6 Products of the Quaternion Real Space*, the six structures are *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, all above this article in this category.

## The Annihilating Sets

**Definition.** For a product $\star$ on $\mathbb{H}$, the **left annihilating set** is
$$
\ell(\star)=\{\tilde x:\tilde x\star\tilde y=0\ \text{for every }\tilde y\} ,
$$
the **right annihilating set** is $r(\star)=\{\tilde x:\tilde y\star\tilde x=0\ \text{for every }\tilde y\}$, and the **two-sided** set is $\ell(\star)\cap r(\star)$.

The left annihilating set is the common kernel of the left multiplication operators $L_{\tilde y}$, and $\tilde x\in\ell(\star)$ exactly when the operator $L_{\tilde x}$ is zero. It is a subspace, and for each of the six structures it is a two-sided ideal: it is carried into itself by multiplication on either side, trivially when it is $\{0\}$ and by the vanishing of the product when it is not. When $\star$ is commutative the two one-sided sets coincide.

The **radical of the product** is the two-sided set read through the product; the radical of the form $\operatorname{Sc}(\tilde x\star\tilde y)$ contains it, being generally larger, and it is treated with the two forms of the two general products in *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, above this article in this category. The two notions agree for the four structures whose form does not vanish identically, as the last section records.

## The Criterion

**Proposition (the diagonal test).** For a product $\star$ that is $\mathbb{R}$-linear in its second slot, an element lies in the left annihilating set if and only if it annihilates each of the four units,
$$
\tilde x\in\ell(\star)\iff \tilde x\star e_\mu=0\ \text{for}\ \mu=0,1,2,3 .
$$

*Proof.* The map $\tilde y\mapsto\tilde x\star\tilde y$ is linear, so it is the zero map exactly when it vanishes on a basis of the space; the four units are such a basis. The same test applies to the right annihilating set, with the order of the factors exchanged.

The criterion reduces every computation below to at most four elementary products. Its content is not the linearity, which all six share, but the four values it reads: they are the columns of the left multiplication operator, and the annihilating set is the set of parameters for which all four columns vanish.

## The Two General Structures

**Theorem.** For the general plain product $\tilde p\tilde q$ and the general quaternionic product $\tilde p^{\natural}\tilde q$, both one-sided annihilating sets and the two-sided set are $\{0\}$.

**Proof.** For the plain product, $\tilde x\tilde y=0$ for every $\tilde y$ forces $\tilde x=0$, because every nonzero quaternion is invertible: multiply by $\tilde y=\tilde x^{-1}$ on the right. For the quaternionic product, put $\tilde y=e_0$, so that $\tilde x^{\natural}=\tilde x^{\natural}e_0=0$, whence $\tilde x=0$; the right set is empty except for $0$ in the same way. Since the two products agree in giving only $0$, the two-sided sets agree too.

The two computations use the same fact in two guises: the plain product is a division, and ${}^{\natural}$ is a bijection carrying $e_0$ nowhere but $e_0$; the quaternionic product is the plain product composed with an anti-involution of the first slot, so its left annihilating set is the image under ${}^{\natural}$ of the plain one, which is $\{0\}$.

## The Two Symmetric Structures

**Theorem.** For the Jordan product $\tilde p\bullet\tilde q$ and the quaternionic symmetric product $N(\tilde p,\tilde q)e_0$, the left, the right and the two-sided annihilating sets are $\{0\}$.

**Proof.** The Jordan product is commutative, so the two one-sided sets coincide; testing $\tilde y=e_0$ gives $\tilde x\bullet e_0=\tilde x$, because $e_0$ is the two-sided unit of the Jordan product, whence $\tilde x=0$. The symmetric quaternionic product is $N(\tilde x,\tilde y)e_0$, and the diagonal test reads $N(\tilde x,e_\mu)=x_\mu$ for $\mu=0,1,2,3$, so the four vanish only at $\tilde x=0$.

The two symmetric structures behave like the two general ones on this question, and for a visible reason: each has a slot that reads the element itself. The Jordan product carries the unit $e_0$ in both slots, and the scalar-valued product reads all four coordinates of the element across the four units.

## The Two Antisymmetric Structures

**Theorem (the cross product and its centre).** For the cross product $\tilde p\wedge\tilde q=\mathbf p\times\mathbf q$ the left, the right and the two-sided annihilating sets are the scalar line
$$
\ell(\wedge)=r(\wedge)=\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0 ,
$$
the centre of the algebra; the centre of the Lie algebra on the vector subspace is smaller, $\{0\}$. For the quaternionic cross product $\tilde p\wedge^{\natural}\tilde q$ the three sets are $\{0\}$.

**Proof.** The plain cross product depends only on the two vector parts, so a scalar element, having zero vector part, annihilates everything: $\mathbb{R}e_0\subseteq\ell(\wedge)$. Conversely, if $\tilde x$ has a nonzero vector part $\mathbf x$, the vector $\mathbf x\times\mathbf y$ does not vanish for every $\mathbf y$, so $\tilde x\notin\ell(\wedge)$; the same argument with the roles exchanged gives the right set, and the two are equal. The centre of the bracket on the vector subspace is $\{0\}$ because no axis line is parallel to every vector. For the quaternionic cross product the diagonal test gives $\tilde x\wedge^{\natural}e_0=-\mathbf x$, which vanishes only for a scalar $\tilde x=s$, and then $\tilde x\wedge^{\natural}e_1=s e_1$, which vanishes only for $s=0$; the right set is computed in the same way.

The scalar line is the annihilating set of the cross product and the centre of the algebra at once, and the two facts are one: a scalar commutes with every element, so the commutator, of which the cross product is half, kills it in both slots. The quaternionic cross product is the commutator of the product with the conjugation in the first slot, and this conjugation destroys the central direction: the scalar line, which annihilates the plain cross product, does not annihilate this one, because $e_0\wedge^{\natural}\tilde q$ is the vector part of $\tilde q$ and does not vanish identically.

## The Six Annihilating Sets Side by Side

| structure | product | left annihilating set | reason |
|---|---|---|---|
| $\mathrm{GPA}$ | $\tilde p\tilde q$ | $\{0\}$ | division |
| $\mathrm{SPA}$ | $\tilde p\bullet\tilde q$ | $\{0\}$ | test $\tilde y=e_0$, the unit of the Jordan product |
| $\mathrm{APA}$ | $\tilde p\wedge\tilde q=\mathbf p\times\mathbf q$ | $\mathbb{R}_{\mathbb{H}}$ | the scalars have no vector part |
| $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | $\{0\}$ | test $\tilde y=e_0$ |
| $\mathrm{SQA}$ | $N(\tilde p,\tilde q)e_0$ | $\{0\}$ | the diagonal test reads $x_\mu$ |
| $\mathrm{AQA}$ | $\tilde p\wedge^{\natural}\tilde q$ | $\{0\}$ | $\tilde y=e_0$ forces $\tilde x$ real, and then $\tilde y=e_1$ kills it |

**Theorem (the six annihilating sets).** Among the six structures the annihilating set is $\{0\}$ for all but one, and it is the scalar line $\mathbb{R}_{\mathbb{H}}$ for the cross product $\mathrm{APA}$ alone. In all six the left, the right and the two-sided sets coincide.

*Proof.* The five rows with $\{0\}$ are the three theorems above; the row of $\mathrm{APA}$ is the same. The coincidence of the one-sided sets: the two symmetric products are commutative; the plain product is the algebra and its left and right sets were computed separately; the quaternionic product is the plain product with the first factor conjugated on the left and read through the same anti-involution on the right; and the quaternionic cross product was tested on both sides.

Five of the six structures are faithful in the sense that no nonzero element kills the whole space, and the sixth fails: the cross product forgets the scalar slot. The failure is also the only place a nontrivial ideal appears, and it is one-dimensional. The count is worth stating plainly: the annihilating set separates the six into a block of five and a single exception, and the exception is the only structure whose product ignores the scalar part of its first argument.

## The Annihilating Set and the Zero Divisors

The annihilating set is the thinnest of the element theories: an element that kills the product on the whole space certainly kills it on a partner, so the annihilating set lies in the zero-divisor set together with the origin,
$$
\ell(\star)\subseteq\{0\}\cup\{\text{zero divisors of }\star\} ,
$$
with equality only when every zero divisor annihilates the whole space. The inclusion is strict for every structure of the six that has a zero divisor, and the gap is the subject of *Zero Divisors*, below this article in this category. The two extremes are the general plain product, where both sets are $\{0\}$, and the cross products, where the zero-divisor set is the whole punctured space while the annihilating set is a line or a point.

**Consequence for the forms.** A product that vanishes for every second argument has zero scalar part, so the annihilating set of the product is contained in the radical of the associated form,
$$
\ell(\star)\subseteq\operatorname{rad}\operatorname{Sc}(\tilde p\star\tilde q) .
$$
The inclusion is strict for the two cross products: the scalar forms $\operatorname{Sc}(\tilde p\wedge\tilde q)$ and $\operatorname{Sc}(\tilde p\wedge^{\natural}\tilde q)$ vanish identically, of radical all of $\mathbb{H}$, while the annihilating sets are the scalar line and the origin. For the four other structures the two notions agree and are as small as possible: the plain form $\operatorname{Sc}(\tilde p\tilde q)$ has radical $\{0\}$, since $\tilde y=e_0$ gives $\operatorname{Sc}(\tilde x)=x_0$ and $\tilde y=e_k$ gives $\operatorname{Sc}(\tilde x e_k)=-x_k$, and the quaternion form $\operatorname{Sc}(\tilde p^{\natural}\tilde q)=N(\tilde p,\tilde q)$ is definite, of radical $\{0\}$, by *The 2 Forms over the Quaternion $\mathbb{R}$ Space*.

## Summary

The left, the right and the two-sided annihilating sets of the general plain product are $\{0\}$, by the division property of the plain algebra; those of the symmetric plain product are $\{0\}$, because the Jordan product carries the unit $e_0$; those of the antisymmetric plain product are the scalar line, the centre of the algebra, because the cross product forgets the scalar slot; those of the general quaternionic product are $\{0\}$, by the anti-involution of its first slot; those of the symmetric quaternionic product are $\{0\}$, because the scalar-valued product reads all four coordinates; and those of the antisymmetric quaternionic product are $\{0\}$, because the conjugation in its first slot destroys the central direction. In all six the left and the right sets coincide, so the annihilating set is a two-sided ideal, $\{0\}$ in five cases and the centre in the sixth. The radical of the two general forms is $\{0\}$ as well, so for the four structures with a nonvanishing form the product and the form agree, while for the two cross products the zero form has radical all of $\mathbb{H}$ and the agreement fails.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\ell(\star)$, $r(\star)$ | left and right annihilating sets of the product $\star$ |
| $\ell\cap r$ | the two-sided annihilating set, the radical of the product |
| $\{0\}$ | the value for GPA, SPA, GQA, SQA and AQA |
| $\mathbb{R}_{\mathbb{H}}$ | the annihilating set of the cross product, the centre of the algebra |
| $e_\mu$ | the four units, the diagonal test of the criterion |
| GPA, SPA, APA, GQA, SQA, AQA | the six structures of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* |

## Further Reading

- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the products.
- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six products and their laws.
- *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-6-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures and their names.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), above this article in this category, for the radicals of the two forms.
- *Zero Divisors* (`articles_maths/quaternion-zero-divisors.md`), above this article in this category, for the companion question of the zero divisors.

# __Annihilators in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space__

## Introduction

An element annihilates a structure when multiplying by it kills the product on the whole space. The quaternion space carries six structures, so the question has six answers, and they are read here side by side. The article defines the left, the right and the two-sided annihilating set of a structure, proves them equal for each of the six, and compares the six sets. The answer is $\{0\}$ for five of the six and the scalar line for the cross product alone, and the comparison is the content. **The two one-sided annihilating sets coincide in all six structures**, because the norm $N$ of the quaternion real space is positive definite: the asymmetry of the biquaternion space, where the plain product and the general quaternionic sesquilinear product separate the two sides at an element of vanishing norm, has no counterpart over $\mathbb{R}$, the two structures that separate there being the two that need the complex coefficients to reach the cone at all.

**Scope and owners.** The products are *The Two General Products of the Quaternion $\mathbb{R}$ Space* and *The 6 Products of the Quaternion Real Space*, the six structures are *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, and the forms are *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, all above this article in this category.

## The Annihilating Set of a Product

**Definition.** For a product $\star$ on $\mathbb{H}$, the **left annihilating set** is
$$
\ell(\star)=\{\tilde x:\tilde x\star\tilde y=0\ \text{for every }\tilde y\} ,
$$
the **right annihilating set** is $r(\star)=\{\tilde x:\tilde y\star\tilde x=0\ \text{for every }\tilde y\}$, and the **two-sided** set is $\ell(\star)\cap r(\star)$.

The left annihilating set is the common kernel of the left multiplication operators $L_{\tilde y}$, and $\tilde x\in\ell(\star)$ exactly when the operator $L_{\tilde x}$ is zero. It is a subspace, and for each of the six structures it is a two-sided ideal: it is carried into itself by multiplication on either side, trivially when it is $\{0\}$ and by the vanishing of the product when it is not. When $\star$ is commutative the two one-sided sets coincide.

**The radical, and the form.** The **radical of the product** is the two-sided set read through the product, and the radical of the form $\operatorname{Sc}(\tilde x\star\tilde y)$ contains it, being generally larger; the two are treated with the two forms of the two general products in *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, above this article in this category. The two notions agree for the four structures whose form does not vanish identically, as §*Results* records.

**The criterion of the four units.** For a product $\star$ that is $\mathbb{R}$-linear in its second slot, an element lies in the left annihilating set exactly when it annihilates each of the four units,
$$
\tilde x\in\ell(\star)\iff \tilde x\star e_\mu=0\ \text{for}\ \mu=0,1,2,3 ,
$$
because the map $\tilde y\mapsto\tilde x\star\tilde y$ is linear and vanishes exactly when it vanishes on a basis of the space, and the four units are such a basis. The same test applies to the right annihilating set, with the order of the factors exchanged. It reduces every computation below to at most four elementary products, and its content is not the linearity, which all six share, but the four values it reads: they are the columns of the left multiplication operator, and the annihilating set is the set of parameters for which all four columns vanish.

**The coordinates, the norm and the remarkable subspaces.** In the units $e_0,e_1,e_2,e_3$ of the space $\mathbb{H}$, write $\tilde p=p_0e_0+\vec p$ and likewise $\tilde x=x_0e_0+\vec x$, with $\vec p=p_1e_1+p_2e_2+p_3e_3$; then $\tilde p^{\natural}=p_0e_0-\vec p$. The **dot product** is $(\vec p,\vec x)=\sum_kp_kx_k$, the **cross product** is $\vec p\times\vec x$, and the **norm** is $N(\tilde p)=p_0^{2}+(\vec p,\vec p)=p_0^{2}+|\vec p|^{2}$, the positive definite form $N(\tilde p,\tilde p)$ of *The 2 Forms over the Quaternion $\mathbb{R}$ Space*, in coordinates of *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*. The **centre** is $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is $\mathrm{Vect}(\mathbb{H})=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$; a **plane** is a real subspace of dimension two, written $\mathbb{R}\{u,v\}$ with its generators displayed, and a **line** is written $\mathbb{R}u$.

**Two algebraic norms, and the one that decides.** The six products carry two **algebraic norms** and no more (*The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space*): the algebraic norm of a product is its scalar form read at the two equal arguments, each of the two is carried by two products, and the two antisymmetrisations carry none. They are the plain one, $N_P(\tilde p)=\tilde p^{2}$, whose scalar coefficient is $B(\tilde p)=p_0^{2}-|\vec p|^{2}$ and which is indefinite, carried by $\mathrm{GPA}$ and $\mathrm{SPA}$, and the quaternion one, $N_Q(\tilde p)=\tilde p^{\natural}\tilde p=N(\tilde p)e_0$, which is positive definite, carried by $\mathrm{GQA}$ and $\mathrm{SQA}$. **The norm that decides every annihilating set below is $N$**, the positive definite one. The plain norm does not decide: at $\tilde p=e_0+e_1$ its scalar coefficient is $B=0$ while $N=2$ and the element is invertible, $\tilde p^{-1}=\tfrac12(e_0-e_1)$. **Every statement below names its norm**: the deciding norm is written $N$, and the generic $\mathrm{Norm}$ of the owner articles is instantiated here by the positive definite norm $N(\tilde p)=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}$. The two antisymmetrisations carry no algebraic norm, and their annihilating sets are read from the vector part alone.


## The Six Structures and their Annihilators

The two general products split into the six structures through the symmetrisation and the antisymmetrisation (*The 6 Products of the Quaternion Real Space*). Each structure is read below with its product, the criterion and the annihilating set; the six answers group in three pairs, the two general products, the two symmetric products and the two antisymmetric products, and a pair shares its proof. The six are in the order of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

### $\mathrm{GPA}$, the general plain algebra

The product is $\tilde p\tilde q$. It is associative, it carries the two-sided unit $e_0$, and it is a division: every nonzero element has the two-sided inverse $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$, by the criterion of the norm $N$, $N(\tilde p)\neq0$, of *Norm and Invertibility in the General Plain Algebra*.

**The annihilating set is $\{0\}$.** If the element kills every partner on the left, then $\tilde x=\tilde x\tilde x^{-1}=0$ after multiplying $\tilde x\tilde y=0$ at the partner $\tilde y=\tilde x^{-1}$, and the right set is empty except for the origin in the same way. The left multiplication is of rank four at every nonzero element and the set is as small as it can be.

*Annihilators of the General Plain Algebra* owns the operator, its rank and its determinant.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde p^{\natural}\tilde q$. The first factor carries the natural conjugation, a bijection of $\mathbb{H}$ that fixes the centre, and the product is the plain product composed with that anti-involution.

**The annihilating set is $\{0\}$.** At the partner $\tilde y=e_0$ the condition reads $\tilde x^{\natural}=0$, whence $\tilde x=0$; the right set is empty except for the origin in the same way.

*Annihilators of the General Quaternionic Algebra* owns the operator and its rank.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product
$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr)=\bigl(p_0q_0-(\vec p,\vec q)\bigr)e_0+p_0\vec q+q_0\vec p .
$$
It is commutative, so the two one-sided sets are one set, and it carries the two-sided unit $e_0$.

**The annihilating set is $\{0\}$.** At the partner $\tilde y=e_0$ the product is $\tilde x\bullet e_0=\tilde x$, because $e_0$ is the two-sided unit, and it vanishes only at the origin.

*Annihilators of the Symmetric Plain Algebra* owns the operator and the shape of the annihilator of an element on the remarkable subspaces.

### $\mathrm{SQA}$, the symmetric quaternionic algebra

The product is the symmetrisation of the preceding one,
$$
\tfrac12\bigl(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p\bigr)=N(\tilde p,\tilde q)e_0,\qquad N(\tilde p,\tilde q)=p_0q_0+(\vec p,\vec q) .
$$
It is central, commutative and symmetric, and its value is the form of *The 2 Forms over the Quaternion $\mathbb{R}$ Space* read at the two arguments.

**The annihilating set is $\{0\}$.** The criterion reads $N(\tilde x,e_\mu)=x_\mu$ for $\mu=0,1,2,3$, the four coordinates of the element one by one, so the four values vanish together only at the origin.

*Annihilators of the Symmetric Quaternionic Algebra* owns the operator and the hyperplane it cuts.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator
$$
\tilde p\wedge\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\vec p\times\vec q .
$$
It is alternating, so it vanishes at the two equal arguments, $\tilde p\wedge\tilde p=0$, and there is no form there and no norm.

**The annihilating set is the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$, the centre of the algebra.** The product depends only on the two vector parts, so a scalar element, having zero vector part, kills every partner and lies in the set. Conversely, an element with a nonzero vector part $\vec x$ fails: the vector $\vec x\times\vec y$ does not vanish for every partner $\vec y$. **The centre of the Lie algebra on the vector subspace is smaller, $\{0\}$**, because no axis line is parallel to every vector.

*Annihilators of the Antisymmetric Plain Algebra* owns the operator and the centre of the bracket.

### $\mathrm{AQA}$, the antisymmetric quaternionic algebra

The product is the antisymmetrisation of the general quaternionic one,
$$
\tfrac12\bigl(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p\bigr)=p_0\vec q-q_0\vec p-\vec p\times\vec q ,
$$
a pure element at every pair. It is alternating, and its first factor carries the conjugation, which destroys the central direction.

**The annihilating set is $\{0\}$.** The criterion reads $\tilde x\wedge^{\natural}e_0=-\vec x$, which vanishes only for a scalar element $\tilde x=s$, and then $\tilde x\wedge^{\natural}e_1=se_1$, which vanishes only for $s=0$. The right set is computed in the same way, and the scalar line that annihilates the plain cross product does not annihilate this one.

*Annihilators of the Antisymmetric Quaternionic Algebra* owns the operator and the failure of the central direction.

## Results

### The Six Annihilating Sets

**Read the cells.** The annihilating set of a structure is the set of elements that the product kills at every partner, and the table records the six sets with the reason each one is what it is. The vector part of $\tilde x$ is $\vec x$, the half is read in the order general, symmetric and antisymmetric, and §*The Annihilating Set of a Product* carries the criterion, the coordinates and the two algebraic norms. Every set can be checked by multiplying a candidate into the four units, and the span notation $\mathbb{R}\{u,v\}$ is the real span of $u$ and $v$.

| half | structure | the product | the annihilating set, and why |
|---|---|---|---|
| the general products | $\mathrm{GPA}$ | $\tilde p\tilde q$ | The set is $\{0\}$, because a nonzero element is invertible and the origin alone kills every partner. |
| | $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | The set is $\{0\}$, because the natural conjugation is a bijection and the partner $e_0$ reads $\tilde x^{\natural}$, which vanishes only at the origin. |
| the symmetric products | $\mathrm{SPA}$ | $\tilde p\bullet\tilde q$ | The set is $\{0\}$, because the unit $e_0$ is a partner of the product and reads the element itself, $\tilde x\bullet e_0=\tilde x$, which vanishes only at the origin. |
| | $\mathrm{SQA}$ | $N(\tilde p,\tilde q)e_0$ | The set is $\{0\}$, because the value at the four units reads the four coordinates of the element, and the four real equations force the origin. |
| the antisymmetric products | $\mathrm{APA}$ | $\tilde p\wedge\tilde q=\vec p\times\vec q$ | The set is the scalar line $\mathbb{R}_{\mathbb{H}}$, because a scalar has no vector part and the cross product reads the vector parts alone, while a nonzero vector part fails at a partner. |
| | $\mathrm{AQA}$ | $\tilde p\wedge^{\natural}\tilde q$ | The set is $\{0\}$, because the partner $e_0$ forces a real element and the partner $e_1$ then kills it. |

**Theorem (the six annihilating sets).** Among the six structures the annihilating set is $\{0\}$ for all but one, and it is the scalar line $\mathbb{R}_{\mathbb{H}}$ for the cross product $\mathrm{APA}$ alone.

*Proof.* The five rows with $\{0\}$ are the five subsections above, and the row of $\mathrm{APA}$ completes the six.

Five of the six structures are faithful in the sense that no nonzero element kills the whole space, and the sixth fails: the cross product forgets the scalar slot. The failure is also the only place a nontrivial ideal appears, and it is one-dimensional. The count is worth stating plainly: the annihilating set separates the six into a block of five and a single exception, and the exception is the only structure whose product ignores the scalar part of its first argument.

### The Two One-Sided Annihilating Sets

**Theorem (the two sides coincide in all six structures).** The left and the right annihilating sets are equal for each of the six structures of the quaternion real space.

*Proof.* The two symmetric products are commutative, so the two multiplications of an element are one operator and the two sets are one set. The plain product is a division, so an element that kills every partner on one side kills every partner on the other; the quaternionic product is the plain product with the first factor carrying the natural conjugation, a bijection, so it behaves the same way. The two antisymmetric products are alternating, and the sign that exchanges the two factors does not change whether a product vanishes. **The $\mathbb{R}$ case has no exception.** In the biquaternion space the same theorem has two exceptions, the plain product and the general quaternionic sesquilinear product, and both appear only at an element of vanishing norm; over $\mathbb{R}$ the norm $N$ is positive definite and vanishes at the origin alone.

## The Annihilating Set and the Zero Divisors

**Whatever structure $\star$ of the six is taken, every element of its annihilating set other than the origin is a zero divisor of that same structure.** **The other inclusion fails in the four structures that have a zero divisor, that is in every structure but the two general products.** The first is definitional: an element that kills the product on every partner kills it on one, so it is a zero divisor with every partner as its witness, and the origin is exempt because the zero of $\mathbb{H}$ is never a zero divisor. The annihilating set therefore lies in the zero-divisor set together with the origin,
$$
\ell(\star)\subseteq\{0\}\cup\{\text{zero divisors of }\star\} ,
$$
with equality exactly for the two general products, whose zero-divisor set is empty and whose annihilating set is the origin alone. The inclusion is strict for the four structures that have a zero divisor, and the gap is the subject of *Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, below this article in this category. The two extremes are the general plain product, where both sets are as small as possible, and the cross products, where the zero-divisor set is the whole punctured space while the annihilating set is a line or a point.

**Consequence for the forms.** A product that vanishes for every second argument has zero scalar part, so the annihilating set of the product is contained in the radical of the associated form,
$$
\ell(\star)\subseteq\operatorname{rad}\operatorname{Sc}(\tilde p\star\tilde q) .
$$
The inclusion is strict for the two cross products. The scalar forms $\operatorname{Sc}(\tilde p\wedge\tilde q)$ and $\operatorname{Sc}(\tilde p\wedge^{\natural}\tilde q)$ vanish identically, of radical all of $\mathbb{H}$, while the annihilating sets are the scalar line and the origin. For the four other structures the two notions agree and are as small as possible. The plain form $\operatorname{Sc}(\tilde p\tilde q)$ has radical $\{0\}$: the partner $\tilde y=e_0$ gives $\operatorname{Sc}(\tilde x)=x_0$ and the partner $\tilde y=e_k$ gives $\operatorname{Sc}(\tilde x e_k)=-x_k$. The quaternion form $\operatorname{Sc}(\tilde p^{\natural}\tilde q)=N(\tilde p,\tilde q)$ is definite, of radical $\{0\}$, by *The 2 Forms over the Quaternion $\mathbb{R}$ Space*.

## Summary

The annihilating set of a product is the set of elements that the product kills at every partner; it is the common kernel of the one-sided multiplications, and its dimension is the number of free real parameters in the equation $\tilde x\star\tilde y=0$. The six structures of the quaternion real space give six answers, each written above with its reason.

Three facts summarize the six structures.

- **The annihilating set is the origin alone in five of the six structures, and the scalar line in the sixth.** The general plain product is a division; the general quaternionic product carries the natural conjugation, a bijection; the symmetric plain product carries the unit $e_0$; the symmetric quaternionic product reads all four coordinates at the four units; and the antisymmetric quaternionic product is forced to a real element at $e_0$ and then killed at $e_1$. The antisymmetric plain product alone fails to be faithful, and its annihilating set is the scalar line $\mathbb{R}_{\mathbb{H}}$, the centre of the algebra, because the cross product forgets the scalar slot.
- **The two one-sided annihilating sets coincide in all six structures**, so the annihilating set is a two-sided ideal of each of them, $\{0\}$ in five cases and the centre in the sixth. The biquaternion space separates the two sides in two of its twelve structures, and there only at an element of vanishing norm; over $\mathbb{R}$ the norm $N$ is positive definite and there is no such element.
- **The radical of the product and the radical of the form agree for the four structures with a nonvanishing form, and they fail for the two cross products.** The plain form and the quaternion form are nondegenerate, of radical $\{0\}$, while the two cross products have the zero scalar form, of radical all of $\mathbb{H}$, and their annihilating sets are the scalar line and the origin.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\ell(\star)$, $r(\star)$ | left and right annihilating sets of the product $\star$ |
| $\ell\cap r$ | the two-sided annihilating set, the radical of the product |
| $\{0\}$ | the value for GPA, GQA, SPA, SQA and AQA |
| $\mathbb{R}_{\mathbb{H}}$ | the annihilating set of the cross product, the centre of the algebra |
| $e_\mu$ | the four units, the diagonal test of the criterion |
| GPA, GQA, SPA, SQA, APA, AQA | the six structures of *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space* |

## Further Reading

- *Zero Divisors in the Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-quaternion-r-space.md`), above this article in this category, for the companion question of the zero divisors and the six zero-divisor sets.
- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the annihilator and the zero divisor stated once for a general product.
- *The Algebraic Structures over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternion-r-space.md`), for the six structures and their names.
- *The 6 Products of the Quaternion Real Space* (`articles_maths/the-6-products-of-the-quaternion-real-space.md`), for the six products and their laws.
- *The Two General Products of the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-two-general-products-of-the-quaternion-r-space.md`), for the two general products and the class-preserving exchange.
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), above this article in this category, for the radicals of the two forms.
- *The 2 Algebraic Norms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternion-r-space.md`), for the two algebraic norms, the multiplicativity and the invertibility criteria.
- *Annihilators in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternion-c-space.md`), for the companion reading of the twelve structures of the biquaternion space, where an element of the cone carries two planes.

The six owners of the subsections, in the order of the table, are:

- *Annihilators of the General Plain Algebra* (`articles_maths/annihilators-of-the-general-plain-algebra-of-quaternions.md`), for $\mathrm{GPA}$.
- *Annihilators of the General Quaternionic Algebra* (`articles_maths/annihilators-of-the-general-quaternionic-algebra-of-quaternions.md`), for $\mathrm{GQA}$.
- *Annihilators of the Symmetric Plain Algebra* (`articles_maths/annihilators-of-the-symmetric-plain-algebra-of-quaternions.md`), for $\mathrm{SPA}$.
- *Annihilators of the Symmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for $\mathrm{SQA}$.
- *Annihilators of the Antisymmetric Plain Algebra* (`articles_maths/annihilators-of-the-antisymmetric-plain-algebra-of-quaternions.md`), for $\mathrm{APA}$.
- *Annihilators of the Antisymmetric Quaternionic Algebra* (`articles_maths/annihilators-of-the-antisymmetric-quaternionic-algebra-of-quaternions.md`), for $\mathrm{AQA}$.


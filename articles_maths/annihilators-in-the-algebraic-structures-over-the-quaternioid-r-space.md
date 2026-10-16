# __Annihilators in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space__

## Introduction

An element annihilates a structure when multiplying by it kills the product on the whole space. Beside the algebra product of the *Quaternions* category, the quaternion space carries the three companion structures of this category, so the question has three answers, and they are read here side by side. The article defines the left, the right and the two-sided annihilating set of a structure, proves them equal for each of the three, and compares the three sets. The answer is $\{0\}$ for the symmetric plain algebra and the general quaternionic algebra, and the scalar line for the antisymmetric plain algebra, and the comparison is the content. **The two one-sided annihilating sets coincide in all three structures**, because the norm $\langle\cdot\rangle_{\natural}$ of the quaternion real space is positive definite: the asymmetry of the biquaternion space, where the plain product and the general quaternionic sesquilinear product separate the two sides at an element of vanishing norm, has no counterpart over $\mathbb{R}$, the structures that separate there being the ones that need the complex coefficients to reach the cone at all.

**Scope and owners.** The products are *The 6 Products of the Quaternioid Real Space*; the three companion structures are *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, the general quaternionic algebra's entry being *Introduction to the General Quaternionic Algebra*, the symmetric plain algebra's *Introduction to the Symmetric Plain Algebra* and the antisymmetric plain algebra's *Introduction to the Antisymmetric Plain Algebra*; and the forms are *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*. The algebra-product annihilators are owned by *Annihilators of the Quaternion Algebra* in the *Quaternions* category, and are named once for the contrast.

## The Annihilating Set of a Product

**Definition.** For a product $\star$ on $\mathbb{H}$, the **left annihilating set** is

$$
\ell(\star)=\{\tilde x:\tilde x\star\tilde y=0\ \text{for every }\tilde y\} ,
$$

the **right annihilating set** is $r(\star)=\{\tilde x:\tilde y\star\tilde x=0\ \text{for every }\tilde y\}$, and the **two-sided** set is $\ell(\star)\cap r(\star)$.

The left annihilating set is the common kernel of the left multiplication operators $L_{\tilde y}$, and $\tilde x\in\ell(\star)$ exactly when the operator $L_{\tilde x}$ is zero. It is a subspace, and for each of the three companion structures it is a two-sided ideal: it is carried into itself by multiplication on either side, trivially when it is $\{0\}$ and by the vanishing of the product when it is not. When $\star$ is commutative the two one-sided sets coincide.

**The radical, and the form.** The **radical of the product** is the two-sided set read through the product, and the radical of the form $\operatorname{Sc}(\tilde x\star\tilde y)$ contains it, being generally larger; the two are treated with the two forms in *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*. The two notions agree for the two companion structures whose form does not vanish identically, as §*Results* records.

**The criterion of the four units.** For a product $\star$ that is $\mathbb{R}$-linear in its second slot, an element lies in the left annihilating set exactly when it annihilates each of the four units,

$$
\tilde x\in\ell(\star)\iff \tilde x\star e_\mu=0\ \text{for}\ \mu=0,1,2,3 ,
$$

because the map $\tilde y\mapsto\tilde x\star\tilde y$ is linear and vanishes exactly when it vanishes on a basis of the space, and the four units are such a basis. The same test applies to the right annihilating set, with the order of the factors exchanged. It reduces every computation below to at most four elementary products, and its content is not the linearity, which all three share, but the four values it reads: they are the columns of the left multiplication operator, and the annihilating set is the set of parameters for which all four columns vanish.

**The coordinates, the norm and the remarkable subspaces.** In the units $e_0,e_1,e_2,e_3$ of the space $\mathbb{H}$, write $\tilde p=p_0e_0+\vec p$ and likewise $\tilde x=x_0e_0+\vec x$, with $\vec p=p_1e_1+p_2e_2+p_3e_3$; then $\tilde p^{\natural}=p_0e_0-\vec p$. The **dot product** is $(\vec p,\vec x)=\sum_kp_kx_k$, the **cross product** is $\vec p\times\vec x$, and the **norm** is $\langle\tilde p\rangle_{\natural}=p_0^{2}+(\vec p,\vec p)=p_0^{2}+|\vec p|^{2}$, the positive definite form $\langle\tilde p,\tilde p\rangle_{\natural}$ of *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*, in coordinates of *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*. The **centre** is $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$ and the **vector subspace** is $\mathrm{Vect}(\mathbb{H})=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$; a **plane** is a real subspace of dimension two, written $\mathbb{R}\{u,v\}$ with its generators displayed, and a **line** is written $\mathbb{R}u$.

**Two algebraic norms, and the one that decides.** The companion products carry two **algebraic norms** and no more (*The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*): the algebraic norm of a product is its scalar form read at the two equal arguments, and the two antisymmetrisations carry none. They are the plain one, $\langle\tilde p\rangle=p_0^{2}-|\vec p|^{2}$, which is indefinite, carried by $\mathrm{SPA}$; and the quaternion one, $\langle\tilde p\rangle_{\natural}=p_0^{2}+|\vec p|^{2}$, which is positive definite, carried by $\mathrm{GQA}$. The algebra product carries the plain norm as well, and that reading is owned by the *Quaternions* category. **The norm that decides every annihilating set below is $\langle\cdot\rangle_{\natural}$**, the positive definite one. The plain norm does not decide: at $\tilde p=e_0+e_1$ its value is $\langle\cdot\rangle=0$ while $\langle\cdot\rangle_{\natural}=2$ and the element is invertible, $\tilde p^{-1}=\tfrac12(e_0-e_1)$. **Every statement below names its norm**: the deciding norm is written $\langle\cdot\rangle_{\natural}$, and the generic $\mathrm{Norm}$ of the owner articles is instantiated here by the positive definite norm $\langle\tilde p\rangle_{\natural}=p_0^{2}+p_1^{2}+p_2^{2}+p_3^{2}$. The antisymmetrisation carries no algebraic norm, and its annihilating set is read from the vector part alone.

## The Three Companion Structures and their Annihilators

Each structure is read below with its product, the criterion and the annihilating set. The three are in the order of *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*.

### $\mathrm{GQA}$, the general quaternionic algebra

The product is $\tilde p^{\natural}\tilde q$. The first factor carries the natural conjugation, a bijection of $\mathbb{H}$ that fixes the centre, and the product is the algebra product composed with that anti-involution.

**The annihilating set is $\{0\}$.** At the partner $\tilde y=e_0$ the condition reads $\tilde x^{\natural}=0$, whence $\tilde x=0$; the right set is empty except for the origin in the same way.

*Square Roots of One and the Idempotents of the General Quaternionic Algebra* and *Introduction to the General Quaternionic Algebra* own the operator and its rank.

### $\mathrm{SPA}$, the symmetric plain algebra

The product is the Jordan product

$$
\tilde p\bullet\tilde q=\tfrac12\bigl(\tilde p\tilde q+\tilde q\tilde p\bigr)=\bigl(p_0q_0-(\vec p,\vec q)\bigr)e_0+p_0\vec q+q_0\vec p .
$$

It is commutative, so the two one-sided sets are one set, and it carries the two-sided unit $e_0$.

**The annihilating set is $\{0\}$.** At the partner $\tilde y=e_0$ the product is $\tilde x\bullet e_0=\tilde x$, because $e_0$ is the two-sided unit, and it vanishes only at the origin.

*The Multiplication Operators of the Symmetric Plain Algebra* and *Introduction to the Symmetric Plain Algebra* own the operator and the shape of the annihilator of an element on the remarkable subspaces.

### $\mathrm{APA}$, the antisymmetric plain algebra

The product is the commutator

$$
\tilde p\wedge\tilde q=\tfrac12\bigl(\tilde p\tilde q-\tilde q\tilde p\bigr)=\vec p\times\vec q .
$$

It is alternating, so it vanishes at the two equal arguments, $\tilde p\wedge\tilde p=0$, and there is no form there and no norm.

**The annihilating set is the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$, the centre of the algebra.** The product depends only on the two vector parts, so a scalar element, having zero vector part, kills every partner and lies in the set. Conversely, an element with a nonzero vector part $\vec x$ fails: the vector $\vec x\times\vec y$ does not vanish for every partner $\vec y$. **The centre of the Lie algebra on the vector subspace is smaller, $\{0\}$**, because no axis line is parallel to every vector.

*The Lie Algebra of the Antisymmetric Plain Algebra* and *Introduction to the Antisymmetric Plain Algebra* own the operator and the centre of the bracket.

## Results

### The Three Annihilating Sets

**Read the cells.** The annihilating set of a structure is the set of elements that the product kills at every partner, and the table records the three sets with the reason each one is what it is. The vector part of $\tilde x$ is $\vec x$, and §*The Annihilating Set of a Product* carries the criterion, the coordinates and the two algebraic norms. Every set can be checked by multiplying a candidate into the four units.

| structure | the product | the annihilating set, and why |
|---|---|---|
| $\mathrm{GQA}$ | $\tilde p^{\natural}\tilde q$ | The set is $\{0\}$, because the natural conjugation is a bijection and the partner $e_0$ reads $\tilde x^{\natural}$, which vanishes only at the origin. |
| $\mathrm{SPA}$ | $\tilde p\bullet\tilde q$ | The set is $\{0\}$, because the unit $e_0$ is a partner of the product and reads the element itself, $\tilde x\bullet e_0=\tilde x$, which vanishes only at the origin. |
| $\mathrm{APA}$ | $\tilde p\wedge\tilde q=\vec p\times\vec q$ | The set is the scalar line $\mathbb{R}_{\mathbb{H}}$, because a scalar has no vector part and the cross product reads the vector parts alone, while a nonzero vector part fails at a partner. |

**Theorem (the three annihilating sets).** Among the three companion structures the annihilating set is $\{0\}$ for the general quaternionic algebra and the symmetric plain algebra, and it is the scalar line $\mathbb{R}_{\mathbb{H}}$ for the antisymmetric plain algebra alone. The algebra product of the same space has the annihilating set $\{0\}$, as owned by *Annihilators of the Quaternion Algebra*.

*Proof.* The two rows with $\{0\}$ are the two subsections above, and the row of $\mathrm{APA}$ completes the three.

Two of the three structures are faithful in the sense that no nonzero element kills the whole space, and the third fails: the cross product forgets the scalar slot. The failure is also the only place a nontrivial ideal appears, and it is one-dimensional. The count is worth stating plainly: the annihilating set separates the three companion structures into a pair and a single exception, and the exception is the only structure whose product ignores the scalar part of its first argument.

### The Two One-Sided Annihilating Sets

**Theorem (the two sides coincide in all three structures).** The left and the right annihilating sets are equal for each of the three companion structures of the quaternion real space.

*Proof.* The symmetric plain product is commutative, so the two multiplications of an element are one operator and the two sets are one set. The general quaternionic product is the algebra product with the first factor carrying the natural conjugation, a bijection, so an element that kills every partner on one side kills every partner on the other. The antisymmetric plain product is alternating, and the sign that exchanges the two factors does not change whether a product vanishes. **The $\mathbb{R}$ case has no exception.** In the biquaternion space the same theorem has two exceptions, the plain product and the general quaternionic sesquilinear product, and both appear only at an element of vanishing norm; over $\mathbb{R}$ the norm $\langle\cdot\rangle_{\natural}$ is positive definite and vanishes at the origin alone.

## The Annihilating Set and the Zero Divisors

**Whatever structure $\star$ of the three is taken, every element of its annihilating set other than the origin is a zero divisor of that same structure.** **The other inclusion fails in the structures that have a zero divisor, that is in every companion structure but the general quaternionic algebra.** The first is definitional: an element that kills the product on every partner kills it on one, so it is a zero divisor with every partner as its witness, and the origin is exempt because the zero of $\mathbb{H}$ is never a zero divisor. The annihilating set therefore lies in the zero-divisor set together with the origin,

$$
\ell(\star)\subseteq\{0\}\cup\{\text{zero divisors of }\star\} ,
$$

with equality exactly for the general quaternionic algebra (and the algebra product, owned by the *Quaternions* category), whose zero-divisor set is empty and whose annihilating set is the origin alone. The inclusion is strict for the two structures that have a zero divisor, and the gap is the subject of *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*. The two extremes are the general quaternionic product, where both sets are as small as possible, and the cross product, where the zero-divisor set is the whole punctured space while the annihilating set is the scalar line.

**Consequence for the forms.** A product that vanishes for every second argument has zero scalar part, so the annihilating set of the product is contained in the radical of the associated form,

$$
\ell(\star)\subseteq\operatorname{rad}\operatorname{Sc}(\tilde p\star\tilde q) .
$$

The inclusion is strict for the antisymmetric plain product. Its scalar form $\operatorname{Sc}(\tilde p\wedge\tilde q)$ vanishes identically, of radical all of $\mathbb{H}$, while the annihilating set is the scalar line. For the two other structures the two notions agree and are as small as possible. The quaternion form $\operatorname{Sc}(\tilde p^{\natural}\tilde q)=\langle\tilde p,\tilde q\rangle_{\natural}$ is definite, of radical $\{0\}$, by *The 2 Forms over the Quaternioid $\mathbb{R}$ Space*; and the plain form $\operatorname{Sc}(\tilde p\tilde q)$ on the symmetric product has radical $\{0\}$ on the Jordan algebra's scalar reading, the partner $\tilde y=e_0$ giving $\operatorname{Sc}(\tilde x)=x_0$ and the partner $\tilde y=e_k$ giving $\operatorname{Sc}(\tilde x e_k)=-x_k$ for the algebra product.

## Summary

The annihilating set of a product is the set of elements that the product kills at every partner; it is the common kernel of the one-sided multiplications, and its dimension is the number of free real parameters in the equation $\tilde x\star\tilde y=0$. The three companion structures of the quaternion real space give three answers, each written above with its reason.

Three facts summarize the three structures.

- **The annihilating set is the origin alone in two of the three structures, and the scalar line in the third.** The general quaternionic product carries the natural conjugation, a bijection; the symmetric plain product carries the unit $e_0$; and the antisymmetric plain product alone fails to be faithful, its annihilating set being the scalar line $\mathbb{R}_{\mathbb{H}}$, the centre of the algebra, because the cross product forgets the scalar slot.
- **The two one-sided annihilating sets coincide in all three structures**, so the annihilating set is a two-sided ideal of each of them, $\{0\}$ in two cases and the centre in the third. The biquaternion space separates the two sides in two of its structures, and there only at an element of vanishing norm; over $\mathbb{R}$ the norm $\langle\cdot\rangle_{\natural}$ is positive definite and there is no such element.
- **The radical of the product and the radical of the form agree for the two structures with a nonvanishing form, and they fail for the antisymmetric plain product.** The plain and the quaternion forms are nondegenerate, of radical $\{0\}$, while the cross product has the zero scalar form, of radical all of $\mathbb{H}$, and its annihilating set is the scalar line.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\ell(\star)$, $r(\star)$ | left and right annihilating sets of the product $\star$ |
| $\ell\cap r$ | the two-sided annihilating set, the radical of the product |
| $\{0\}$ | the value for $\mathrm{GQA}$ and $\mathrm{SPA}$, and for the algebra product |
| $\mathbb{R}_{\mathbb{H}}$ | the annihilating set of the cross product, the centre of the algebra |
| $e_\mu$ | the four units, the diagonal test of the criterion |
| $\mathrm{SPA},\mathrm{APA},\mathrm{GQA}$ | the three companion structures of *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* |

## Further Reading

- *Zero Divisors in the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/zero-divisors-in-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the companion question of the zero divisors and the three zero-divisor sets.
- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the annihilator and the zero divisor stated once for a general product.
- *The Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-algebraic-structures-over-the-quaternioid-r-space.md`), for the three companion structures and their names.
- *The 6 Products of the Quaternioid Real Space* (`articles_maths/the-6-products-of-the-quaternioid-real-space.md`), for the companion products and their laws.
- *The 2 Forms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternioid-r-space.md`), for the radicals of the two forms.
- *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternioid-r-space.md`), for the two algebraic norms and the invertibility criteria.
- *Annihilators of the Quaternion Algebra* (`articles_maths/annihilators-of-the-quaternion-algebra.md`), in the *Quaternions* category, for the algebra-product operator, its rank and its determinant.
- *Annihilators in the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/annihilators-in-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the companion reading over the biquaternion space, where an element of the cone carries two planes.

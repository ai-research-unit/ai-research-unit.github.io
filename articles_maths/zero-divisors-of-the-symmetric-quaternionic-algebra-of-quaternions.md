# __Zero Divisors of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic product is the operation $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$ of *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, the quaternion form placed on the scalar line. A scalar-valued operation has no room for a mystery in its equations: the product $\tilde p\star\tilde q$ vanishes exactly when its coefficient vanishes. This article reads that single criterion and its consequences for the zero-divisor structure of the block. The definition of the **zero divisor**, of the **annihilator** and of the **regular element** is the general one of *Definitions for the Study of the 6 Algebraic Structures*, and the criterion is the only computation of the article; everything after it is a reading of the criterion.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_1e_2=e_3$; an element is $\tilde q=q_0e_0+\mathbf q$ with $\mathbf q=\sum_kq_ke_k$. The **quaternion conjugation** is $\tilde q^{\natural}=q_0e_0-\mathbf q$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$ and the **plain form** is $B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p\tilde q)$. The **symmetric quaternionic product** is $\tilde p\star\tilde q=\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)=N(\tilde p,\tilde q)e_0$.

Throughout, a **zero divisor** of the block is an element $\tilde a\neq0$ for which there is $\tilde b\neq0$ with $\tilde a\star\tilde b=0$ or $\tilde b\star\tilde a=0$; the block is commutative, so the two conditions coincide and no side has to be named. The **annihilator** of $\tilde a$ is $\mathrm{Ann}(\tilde a)=\{\tilde q:\tilde a\star\tilde q=0\}$, and $\tilde a$ is **regular** when it is not a zero divisor. These are the definitions of *Definitions for the Study of the 6 Algebraic Structures* read for a commutative operation.

## The Criterion

**Theorem (the zero-divisor criterion).** For $\tilde p,\tilde q\in\mathbb{H}$,

$$
\tilde p\star\tilde q=0\quad\Longleftrightarrow\quad N(\tilde p,\tilde q)=0 .
$$

*Proof.* The product is $N(\tilde p,\tilde q)e_0$ by the governing formula of *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, and a real multiple of $e_0$ vanishes exactly when the real coefficient does.

**Corollary (the annihilator is a form-zero set).** For every $\tilde p$,

$$
\mathrm{Ann}(\tilde p)=\{\tilde q:N(\tilde p,\tilde q)=0\}=\tilde p^{\perp},
$$

the set of elements whose pairing with $\tilde p$ under the quaternion form vanishes.

*Proof.* Immediate from the criterion; the last equality is the definition of the form-perpendicular set of $\tilde p$.

**Remark (the criterion is not a square condition).** The element $\tilde p$ need not be isotropic: the criterion kills $\tilde p\star\tilde q$ for a suitable $\tilde q$ even when $\tilde p\star\tilde p\neq0$. The block therefore separates two things that coincide in many algebras: the vanishing of a *square* and the vanishing of a *product*, and the separation is the whole point of this article. The square $\tilde p\star\tilde p=N(\tilde p,\tilde p)e_0$ never vanishes off $0$, because the form is definite; the products vanish on a large set, because a definite form still pairs an element with many others to zero.

## The Families

**Theorem (the zero-divisor pairs).** The pairs $(\tilde p,\tilde q)$ with $\tilde p\star\tilde q=0$ form the quadric

$$
\{(\tilde p,\tilde q)\in\mathbb{H}\times\mathbb{H}:p_0q_0+\mathbf p\cdot\mathbf q=0\},
$$

a real hypersurface of $\mathbb{H}\times\mathbb{H}\cong\mathbb{R}^8$ of real dimension $7$. In terms of the scalar and vector parts the pairs fall into three families:

- **both pure**, $p_0=q_0=0$: then $\mathbf p\cdot\mathbf q=0$, so the two vector parts are perpendicular;
- **exactly one pure**, say $p_0=0\ne q_0$: then $\mathbf p\cdot\mathbf q=0$, the scalar coordinate $q_0$ being free and the vector part $\mathbf q$ constrained to the plane perpendicular to $\mathbf p$;
- **both nonpure**, $p_0q_0\ne0$: then $q_0=-\dfrac{\mathbf p\cdot\mathbf q}{p_0}$, the **scalar compensation** that offsets the pairing of the vector parts.

*Proof.* The quadric is the zero set of the polynomial $p_0q_0+\mathbf p\cdot\mathbf q$, which is not identically zero, so the set is a hypersurface of the eight-dimensional product; the three families are the splitting of the equation according to which scalar coordinates vanish, and the display of the third family is the equation solved for $q_0$.

**Corollary (the annihilator of a nonzero element is a hyperplane).** For $\tilde p\neq0$, the set $\mathrm{Ann}(\tilde p)=\tilde p^{\perp}$ is a linear hyperplane of $\mathbb{H}$, of real dimension $3$; it contains $\tilde p$ exactly when $N(\tilde p,\tilde p)=0$, which never happens for $\tilde p\neq0$; and $\mathrm{Ann}(0)=\mathbb{H}$.

*Proof.* The vector $\tilde p\neq0$ has some nonzero coordinate; the linear form $N(\tilde p,\cdot)$ is nonzero and its zero set is a hyperplane, of dimension $4-1=3$. The second statement is the definiteness $N(\tilde p,\tilde p)>0$. The last is the definition: $0\star\tilde q=0$ for every $\tilde q$.

**Remark (the annihilator is not faithful in the element).** The map $\tilde p\mapsto\mathrm{Ann}(\tilde p)$ is constant on the punctured lines: $\mathrm{Ann}(\lambda\tilde p)=\mathrm{Ann}(\tilde p)$ for every $\lambda\neq0$, because the form is linear in each slot. It is a surjection of the punctured space onto the set of hyperplanes through $0$, and its fibres are the punctured lines.

## The Zero-Divisor Set

**Theorem (the zero-divisor set is the whole punctured space).** Every nonzero element of $\mathbb{H}$ is a zero divisor of the block; the zero-divisor set is $\mathbb{H}\setminus\{0\}$, and $0$ is the only regular element.

*Proof.* Let $\tilde p\neq0$. The annihilator $\tilde p^{\perp}$ is a hyperplane of dimension $3$, hence contains a nonzero element $\tilde q$; then $\tilde p\star\tilde q=0$ with both factors nonzero, so $\tilde p$ is a zero divisor. Conversely $0$ is not a zero divisor, because $0\star\tilde q=0$ for every $\tilde q$ and the defining clause needs $\tilde a\neq0$; and $0$ is regular because it is neither a left nor a right zero divisor.

**Corollary (the regular elements reduce to zero).** The set of regular elements of the block is $\{0\}$. In particular there is no nonzero element that is cancellable, and the block is as far from an integral domain as a commutative scalar-valued operation can be.

*Proof.* The theorem gives that every nonzero element is a zero divisor, and $0$ is regular; these are all the elements.

**Remark (the maximal set, on a definite form).** The maximality of the zero-divisor set is usually read on an indefinite form, whose isotropic directions make products vanish. Here the coefficient is positive definite and there is no isotropic direction, yet the zero-divisor set is maximal, because the vanishing requires a *pair* and not a single element. This is the exotic point of the block, and it is the reason the article separates the zero-divisor set from the isotropic set: the first is everything nonzero, the second is only the origin.

**Remark (a witness, and the contrast with the plain block).** The pair $(\tilde p,\tilde q)=(e_0,e_1)$ gives $e_0\star e_1=N(e_0,e_1)e_0=0$ with $e_1\neq0$, so $e_0$ is a zero divisor of the block. In the symmetric plain algebra the same element is a unit, $e_0\bullet\tilde q=\tilde q$, and is not a zero divisor (*Zero Divisors of the Symmetric Plain Algebra*): the two scalar-valued-looking blocks of the six behave oppositely at the unit.

## The Relation to the Isotropic Elements

**Proposition (the form is the plain form with a conjugation).** For all $\tilde p,\tilde q$, the quaternion form is the plain form with the second argument conjugated,

$$
N(\tilde p,\tilde q)=B(\tilde p,\tilde q^{\natural})=\mathrm{Sc}\bigl(\tilde p\,\tilde q^{\natural}\bigr).
$$

*Proof.* Since $\tilde q^{\natural}=q_0e_0-\mathbf q$, the product $\tilde p\tilde q^{\natural}$ has scalar part $p_0q_0-\mathbf p\cdot(-\mathbf q)=p_0q_0+\mathbf p\cdot\mathbf q=N(\tilde p,\tilde q)$, and $\mathrm{Sc}(\tilde p\tilde q^{\natural})=B(\tilde p,\tilde q^{\natural})$ by the definition of the plain form.

**Corollary (the zero-divisor criterion in the plain form).** $\tilde p\star\tilde q=0$ if and only if $B(\tilde p,\tilde q^{\natural})=0$; the zero-divisor criterion of the block is the vanishing of the **plain form**, evaluated at $\tilde p$ and the conjugate of $\tilde q$.

*Proof.* Compose the theorem of §*The Criterion* with the proposition.

Now the plain form $B$ is indefinite of signature $(1,3)$, and its isotropic elements are the nonzero solutions of $B(\tilde q,\tilde q)=q_0^{2}-|\mathbf q|^{2}=0$, the cone of real dimension $3$ with two families (*The 2 Forms over the Quaternion $\mathbb{R}$ Space*). The quaternion form $N$ is definite, and its only isotropic element is $0$. The block's zero-divisor pairs are the pairs that the plain form kills at $\tilde q^{\natural}$, a much larger class than the isotropic elements of either form. The apparent paradox is resolved by the two forms being different: the coefficient of the *product* is the definite form, while the *criterion* is the vanishing of the indefinite one on a conjugate pair.

Over $\mathbb{R}$ the two objects coincide as the empty set: the isotropic set of $N$ is $\{0\}$, and the two general products are division algebras with no zero-divisor at all. What is stable is the maximality of the block's own set; what changes is the isotropic set, a cone in the complex case and a single point over $\mathbb{R}$, so that the block is maximal in both algebras and is the more isolated over $\mathbb{R}$, its isotropic set lying strictly inside it there rather than filling a cone.

## The Comparison with the Other Five Structures

The zero divisors of a structure are read with the general definition of *Definitions for the Study of the 6 Algebraic Structures*; the six operations are those of *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*.

**Proposition (the two non-symmetric general products have none).** The general plain product $\tilde p\tilde q$ and the general quaternionic product $\tilde p^{\natural}\tilde q$ have no zero divisor: their only element annihilated by a nonzero factor is $0$.

*Proof.* For the plain product, $\tilde p\tilde q=0$ with $\tilde p\neq0$ forces $\tilde q=0$, because $\mathbb{H}$ is a division algebra (*Norm and Invertibility in the General Plain Algebra* and *Ideals and Simplicity of the General Plain Algebra*). For the quaternionic product, $\tilde p^{\natural}\tilde q=0$ is $\tilde p^{\natural}\tilde q=0$, and $\tilde p^{\natural}\neq0$, so the same division property gives $\tilde q=0$.

**Proposition (the symmetric plain block).** The zero divisors of the symmetric plain product are exactly the nonzero pure quaternions.

*Proof.* Write $\tilde p\bullet\tilde q=(p_0q_0-\mathbf p\cdot\mathbf q)e_0+p_0\mathbf q+q_0\mathbf p$. If both elements are pure, the value is $-(\mathbf p\cdot\mathbf q)e_0$, which vanishes exactly when $\mathbf p\cdot\mathbf q=0$. If exactly one is pure, say $p_0=0\ne q_0$, the vector part is $q_0\mathbf p$, which vanishes only for $\mathbf p=0$; so no such pair is a zero-divisor pair. If both are nonpure, the vector part $p_0\mathbf q+q_0\mathbf p$ forces $\mathbf q=-(q_0/p_0)\mathbf p$, and the scalar part $p_0q_0-\mathbf p\cdot\mathbf q=0$ then reads $p_0q_0+(q_0/p_0)|\mathbf p|^{2}=0$, that is $q_0\bigl(p_0^{2}+|\mathbf p|^{2}\bigr)/p_0=0$, which forces $\tilde p=0$, a contradiction. So the zero-divisor pairs have both factors pure and perpendicular vector parts, and a pure element is a zero divisor exactly when it is nonzero.

**Theorem (the block is the maximal row of the two symmetric structures).** Among the six structures, the zero-divisor set is maximal, equal to $\mathbb{H}\setminus\{0\}$, for the antisymmetric plain product, the antisymmetric quaternionic product and the symmetric quaternionic product; it is the proper set of the nonzero pure quaternions for the symmetric plain product; and it is empty for the two general products.

*Proof.* An antisymmetric product is alternating, $\tilde x\circ\tilde x=0$ for every $\tilde x$, so every nonzero element has a nonzero annihilator, namely itself; this gives the maximality of the two antisymmetric rows and, incidentally, a reason different from the block's. The block's maximality is the theorem of §*The Zero-Divisor Set*; the symmetric plain row is the proposition above; and the two general rows are the first proposition. The six rows exhaust the catalogue.

| structure | zero-divisor set | reason |
|---|---|---|
| $\mathrm{GPA}$ | $\varnothing$ (only $0$) | division algebra |
| $\mathrm{SPA}$ | the nonzero pure quaternions | perpendicular pure pairs |
| $\mathrm{APA}$ | $\mathbb{H}\setminus\{0\}$ (maximal) | alternation |
| $\mathrm{GQA}$ | $\varnothing$ (only $0$) | division algebra |
| $\mathrm{SQA}$ | $\mathbb{H}\setminus\{0\}$ (maximal) | the definite form vanishes on suitable pairs |
| $\mathrm{AQA}$ | $\mathbb{H}\setminus\{0\}$ (maximal) | alternation |

**Remark (three maximal sets, three reasons).** The three maximal rows are maximal for three different reasons: the two antisymmetric ones because each element is its own annihilator, the block because the form zero sets are hyperplanes despite definiteness, and the symmetric plain one is not maximal at all. The block is the only maximal row whose coefficient is definite, and this is its precise originality among the six.

## Summary

The symmetric quaternionic product vanishes on a pair exactly when the quaternion form vanishes on it, $\tilde p\star\tilde q=0\Leftrightarrow N(\tilde p,\tilde q)=0$. The annihilator of a nonzero element is the form-perpendicular hyperplane $\tilde p^{\perp}$ of real dimension $3$, the pairs are the quadric $\{N=0\}$ of real dimension $7$ with the three families of pure/pure, one-pure and nonpure factors, and the zero-divisor set is the whole punctured space $\mathbb{H}\setminus\{0\}$, with $0$ the only regular element. The criterion is the vanishing of the plain form at a conjugate pair, $N(\tilde p,\tilde q)=B(\tilde p,\tilde q^{\natural})$; the coefficient of the product is definite and has no isotropic element but $0$, while the criterion uses the indefinite plain form, and this is why the block has a maximal zero-divisor set with no isotropic direction and no square-zero element. Among the six structures the antisymmetric plain, the antisymmetric quaternionic and the symmetric quaternionic structures have the maximal set, the symmetric plain structure has only the nonzero pure quaternions, and the two general structures have none.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_0$ | the symmetric quaternionic product |
| $N(\tilde p,\tilde q)=p_0q_0+\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$ | the quaternion form, definite |
| $B(\tilde p,\tilde q)=p_0q_0-\mathbf p\cdot\mathbf q=\mathrm{Sc}(\tilde p\tilde q)$ | the plain form, indefinite |
| $\mathrm{Ann}(\tilde a)=\tilde a^{\perp}$ | the annihilator, a hyperplane of real dimension $3$ for $\tilde a\neq0$ |
| $\{N=0\}$ | the quadric of zero-divisor pairs, real dimension $7$ |
| $N(\tilde p,\tilde q)=B(\tilde p,\tilde q^{\natural})$ | the bridge between the criterion and the plain form |

## Further Reading

- *Introduction to the Symmetric Quaternionic Algebra of Quaternions* (`articles_maths/introduction-to-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the product and its governing formula
- *Definitions for the Study of the 6 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-6-algebraic-structures.md`), for the zero divisor, the annihilator and the regular element
- *The 2 Forms over the Quaternion $\mathbb{R}$ Space* (`articles_maths/the-2-forms-over-the-quaternion-r-space.md`), for the two forms, their signatures and their isotropic elements
- *Zero Divisors of the Symmetric Plain Algebra* (`articles_maths/zero-divisors-of-the-symmetric-plain-algebra-of-quaternions.md`), for the comparison with the other symmetric block
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra-of-quaternions.md`), for the isotropic elements of the block

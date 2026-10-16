# __Zero Divisors of the General Plain Algebra of the Reduced Biquaternions__

## Introduction

The multiplication of the general plain algebra has **zero divisors**, and the article reads them as one object: the **null cone** of the reduced norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$. The cone is the set
$$
\mathcal{N}=\bigl\{T\neq0:\langle T\rangle_{\natural}=0\bigr\}=\bigl\{T\neq0:A^{2}=B^{2}\bigr\}=\mathbb{C}^{\times}\Pi_{1}\cup\mathbb{C}^{\times}\Pi_{2},
$$
the union of the two **idempotent lines** with the origin removed, each a complex line of real dimension two. The two lines are the maximal ideals of the algebra; the elements of one annihilate the elements of the other; and the zero divisors of the multiplication are exactly the elements of the cone.

The cone is **degenerate**: the reduced norm factors as the product of two linear forms,
$$
\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B),
$$
so its vanishing set is the union of the two lines $A+B=0$ and $A-B=0$ and not an irreducible quadric cone. This is the geometric form of the fact that the algebra is a direct product of two fields: a product of two fields has zero divisors, and its zero divisors are the two factors.

**The results.** The zero divisors of the multiplication are the nonzero elements of the two idempotent lines $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$, and they are exactly the elements of vanishing reduced norm. The two lines are the two maximal ideals; they meet only at the origin; each is closed under multiplication; and the product of an element of one line with an element of the other is zero, so the whole of one line annihilates the whole of the other. The cone is homogeneous, and each of its two components is of real dimension two; the complement of the cone in $\mathbb{B}_{\mathrm{r}}\setminus\{0\}$ is the group of units.

**Boundaries.** The criterion of invertibility and the reduced norm are *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*, above this article in this category; the multiplicativity of the reduced norm is *The Four Products, Their Forms and Their Algebraic Norms*. The annihilators of the zero divisors, one line annihilating the other, are *Annihilators of the General Plain Algebra of the Reduced Biquaternions*, below this article; the idempotents and the projections are *Square Roots of One and the Idempotents of the General Plain Algebra of the Reduced Biquaternions*; and the structure of the algebra as a direct product of two fields is *Introduction to the General Plain Algebra of the Reduced Biquaternions*. The complex and real quadrics of the four forms are *The Four Products, Their Forms and Their Algebraic Norms*.

## The Null Cone

### The Definition and the Equation

**The null cone of the multiplication is the nonzero vanishing set of the reduced norm, and its equation is $A^{2}=B^{2}$.**

**Definition.** The **null cone** of the general plain algebra is
$$
\mathcal{N}=\bigl\{T\in\mathbb{B}_{\mathrm{r}}:T\neq0,\ \langle T\rangle_{\natural}=A^{2}-B^{2}=0\bigr\}.
$$

**Theorem (the equation).** The null cone is the union of the two complex lines
$$
\mathcal{N}=\mathbb{C}^{\times}\Pi_{1}\cup\mathbb{C}^{\times}\Pi_{2},
$$
with $\mathbb{C}^{\times}=\mathbb{C}\setminus\{0\}$.

*Proof.* $\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B)=0$ holds iff $A+B=0$ or $A-B=0$, since the complex numbers have no zero divisors. The condition $A+B=0$ is $B=-A$, that is $T=A(1-j)=2A\Pi_{2}$ with $A\in\mathbb{C}^{\times}$; the condition $A-B=0$ is $B=A$, giving $T=A(1+j)=2A\Pi_{1}$ with $A\in\mathbb{C}^{\times}$. The two families are the two punctured lines.

**Corollary (the zero divisors of the multiplication are the cone).** An element is a zero divisor of the multiplication exactly when it is in the null cone.

*Proof.* If $T\neq0$ and $\langle T\rangle_{\natural}=0$ then one idempotent coordinate vanishes, so $T$ annihilates the idempotent on the other coordinate: $T=2A\Pi_{1}$ gives $T\Pi_{2}=0$ with $\Pi_{2}\neq0$. Conversely if $T$ is a zero divisor, $TW=0$ with $W\neq0$; in the idempotent coordinates the product is componentwise, so one coordinate of $T$ vanishes, that is $\langle T\rangle_{\natural}=0$. The criterion is *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*, where invertibility is $\langle T\rangle_{\natural}\neq0$.

### The Two Lines

**Each line is a complex line of real dimension two, spanned by an idempotent, and the two lines meet only at the origin.**

**Theorem (the two lines).** The two components of the cone are
$$
\mathbb{C}\Pi_{1}=\{A(1+j):A\in\mathbb{C}\}=\mathbb{R}\{1+j,\;i+ij\},\qquad
\mathbb{C}\Pi_{2}=\{A(1-j):A\in\mathbb{C}\}=\mathbb{R}\{1-j,\;i-ij\},
$$
real two-planes through the origin, and they meet only at $0$.

*Proof.* $A\Pi_{1}=\tfrac12 A(1+j)=\tfrac12\bigl[a(1+j)+a^{\prime}(i+ij)\bigr]$, so the real span is spanned by $1+j$ and $i+ij$; the same for the second line. If $A\Pi_{1}=B\Pi_{2}$ with both nonzero, then $A\Pi_{1}=B\Pi_{2}$ and multiplying by $\Pi_{1}$ gives $A\Pi_{1}=B\Pi_{1}\Pi_{2}=0$, so $A=0$, a contradiction; the intersection is therefore the origin.

**Corollary (the cone is homogeneous and two-component).** If $T$ is in the cone and $\lambda\in\mathbb{C}^{\times}$, then $\lambda T$ is in the cone, and it lies on the same line; the cone has two connected components up to the origin, the two lines.

*Proof.* $\lambda(A\Pi_{i})=(\lambda A)\Pi_{i}$ stays on the line, and $\lambda\neq0$ keeps the element nonzero; the two lines are connected after removing the origin, being punctured complex lines, and they meet only at the origin, so the components are the two.

### The Degeneracy

**The cone is degenerate: it is the union of two lines and not an irreducible quadric, because the reduced norm factors into two linear forms.**

**Theorem (the factorization and the degeneracy).** The reduced norm of the multiplication is the product of the two linear forms
$$
\langle T\rangle_{\natural}=(A+B)(A-B),
$$
and the cone is the union of the two hyperplanes $A+B=0$ and $A-B=0$; the quadratic form $\langle\cdot,\cdot\rangle_{\natural}$ is **degenerate** on no point but its zero set is **reducible**.

*Proof.* The factorization is the difference of two squares. A vanishing set of a product of two linear forms is the union of two hyperplanes; equivalently, the polarity of the quadratic form $\langle\cdot,\cdot\rangle_{\natural}$ has $\langle T,U\rangle_{\natural}=0$ for the whole line of each linear form, and the singular locus of the cone contains the two lines.

**Remark (the complex cone against the real cone).** The equation $\langle T\rangle_{\natural}=0$ is a **complex** equation: writing $\langle T\rangle_{\natural}=\mathrm{Re}N+i\,\mathrm{Im}N$ with
$$
\mathrm{Re}N=a^{2}-a'^{2}-b^{2}+b'^{2},\qquad \mathrm{Im}N=2(aa'-bb'),
$$
the null cone is the set where **both** vanish, the union of the two complex lines above. The real quadric of the single real equation $\mathrm{Re}N=0$ is a larger cone, of real dimension three, and it is **not** the zero-divisor set. The zero divisors are the complex null cone, and the distinction is the one the corpus keeps between a complex form and its real part.

## The Structure of the Zero Divisors

### The Two Families and Their Closure

**Each line is closed under multiplication, and the product of two elements of different lines is zero.**

**Theorem (the product of two zero divisors).** For $A,B\in\mathbb{C}$,
$$
(A\Pi_{1})(B\Pi_{1})=(AB)\Pi_{1},\qquad (A\Pi_{2})(B\Pi_{2})=(AB)\Pi_{2},\qquad (A\Pi_{1})(B\Pi_{2})=0,
$$
so the cone together with $0$ is closed under multiplication, and the product of two elements of different lines vanishes.

*Proof.* $\Pi_{1}^{2}=\Pi_{1}$, $\Pi_{2}^{2}=\Pi_{2}$ and $\Pi_{1}\Pi_{2}=0$ (*Reduced Biquaternion Space*); the products follow by bilinearity.

**Remark (the cone is not an additive subgroup).** The set $\mathcal{N}\cup\{0\}$ is closed under multiplication but not under addition: $\Pi_{1}+\Pi_{2}=1$, which is a unit and is not in the cone. The union of the two ideals is therefore a **union of ideals** and not an ideal, and the algebra has the two maximal ideals in place of a single maximal ideal.

### The Maximal Ideals

**The two lines are the two maximal ideals of the algebra, and they are the only ones.**

**Theorem (the maximal ideals).** The two-sided ideals of the algebra are $0$, $\mathbb{C}\Pi_{1}$, $\mathbb{C}\Pi_{2}$ and $\mathbb{B}_{\mathrm{r}}$; the two maximal ideals are the idempotent lines, and they are the annihilators of the two projections.

*Proof.* The algebra is the direct product $\mathbb{C}\Pi_{1}\oplus\mathbb{C}\Pi_{2}$ of two fields (*Reduced Biquaternion Space*); the ideals of a direct product of two fields are the products of an ideal of each factor, and a field has only $0$ and itself, so the four products are $0$, $\mathbb{C}\Pi_{1}$, $\mathbb{C}\Pi_{2}$ and the whole algebra. The maximal ones are the two lines, the kernels of the two projections.

### The Annihilation of One Line by the Other

**Every element of one line annihilates every element of the other, and the two lines are the annihilators of each other.**

**Theorem (mutual annihilation).** For $A,B\in\mathbb{C}^{\times}$,
$$
(A\Pi_{1})(B\Pi_{2})=0=(B\Pi_{2})(A\Pi_{1}),
$$
and the annihilator of a nonzero element of one line is exactly the other line.

*Proof.* The product vanishes by the previous theorem. If $T=A\Pi_{1}$ with $A\neq0$ and $TW=0$ for $W=C\Pi_{1}+D\Pi_{2}$, then $TW=AC\Pi_{1}$ is zero only if $C=0$, that is $W\in\mathbb{C}\Pi_{2}$; the same on the other side. The annihilators are read again, with the two-sided annihilator of the structure, in *Annihilators of the General Plain Algebra of the Reduced Biquaternions*, below this article.

## The Complement: the Units

**The complement of the null cone in the nonzero elements is the group of units, and it is connected.**

**Theorem (the complement).** The complement of the cone is the group of units,
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\bigl\{T:\langle T\rangle_{\natural}\neq0\bigr\}=\mathbb{B}_{\mathrm{r}}\setminus\bigl(\mathcal{N}\cup\{0\}\bigr)\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$
and it is **connected**.

*Proof.* The criterion and the isomorphism are *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*; an element is a unit iff $\langle T\rangle_{\natural}\neq0$ iff it is outside the cone and nonzero. The set $\{N\neq0\}$ is the complement of the union of two real two-planes, and in the idempotent coordinates it is the pair $(q_1,q_2)$ with $q_1=A+B\neq0$ and $q_2=A-B\neq0$, that is $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, a product of two punctured complex planes; each punctured plane is connected and a product of connected sets is connected.

**Remark (the algebra is not a division algebra).** The cone is not empty and not the origin; the two lines contain nonzero elements, so the algebra **has zero divisors**, is **not a field** and is **not a division algebra** (*Introduction to the General Plain Algebra of the Reduced Biquaternions*). The absence of division is read from the two lines and is the geometric content of the failure of the algebra to be simple.

## Summary

The zero divisors of the multiplication are the null cone of the reduced norm,
$$
\mathcal{N}=\bigl\{T\neq0:\langle T\rangle_{\natural}=A^{2}-B^{2}=0\bigr\}=\mathbb{C}^{\times}\Pi_{1}\cup\mathbb{C}^{\times}\Pi_{2},
$$
the union of the two idempotent lines $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$ with the origin removed, each a complex line of real dimension two, each spanned over $\mathbb{R}$ by an idempotent and the imaginary multiple of an idempotent, and the two meeting only at the origin. The cone is **degenerate** and reducible: the reduced norm factors, $\langle T\rangle_{\natural}=(A+B)(A-B)$, and the cone is the union of the two hyperplanes $A+B=0$ and $A-B=0$, not an irreducible quadric. The zero-divisor set is the **complex** null cone, the set where both $\mathrm{Re}N$ and $\mathrm{Im}N$ vanish; the real quadric $\{\mathrm{Re}N=0\}$ is larger and is not the zero-divisor set.

Each line is closed under multiplication, $(A\Pi_{i})(B\Pi_{i})=(AB)\Pi_{i}$, and the product of two elements of different lines vanishes, $(A\Pi_{1})(B\Pi_{2})=0$; the two lines are the two **maximal ideals** of the algebra, they are the annihilators of each other, and the algebra is not a field and not a division algebra. The complement of the cone in the nonzero elements is the group of units,
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\{\langle T\rangle_{\natural}\neq0\}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$
and it is connected, the punctured complex planes being connected.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{N}=\{T\neq0:\langle T\rangle_{\natural}=0\}$ | the null cone, the zero-divisor set |
| $\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B)$ | the reduced norm, factoring into two linear forms |
| $\mathbb{C}^{\times}\Pi_{1}$, $\mathbb{C}^{\times}\Pi_{2}$ | the two punctured idempotent lines |
| $A+B=0$, $A-B=0$ | the two hyperplanes of the cone |
| $\mathrm{Re}N=a^{2}-a'^{2}-b^{2}+b'^{2}$, $\mathrm{Im}N=2(aa'-bb')$ | the real and imaginary parts of the reduced norm |
| $\mathbb{C}\Pi_{1}$, $\mathbb{C}\Pi_{2}$ | the two maximal ideals |
| $(A\Pi_{1})(B\Pi_{2})=0$ | the mutual annihilation of the two lines |
| $\mathbb{B}_{\mathrm{r}}^{\times}=\{\langle T\rangle_{\natural}\neq0\}$ | the complement of the cone, the group of units |

## Further Reading

- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article in this category, for the criterion $\langle T\rangle_{\natural}\neq0$ and the group of units.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), above this article, for the reduced norm, its multiplicativity and the complex quadrics of the four forms.
- *Introduction to the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the maximal ideals and the absence of division.
- *Annihilators of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the annihilator of an element and the two-sided annihilator of the structure.
- *Zero Divisors of the Biquaternion Algebra* (`articles_maths/zero-divisors-of-the-biquaternion-algebra.md`), the non-commutative counterpart, for the same object over an algebra with more families.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the definition of a zero divisor used here.

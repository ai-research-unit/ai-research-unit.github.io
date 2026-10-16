# __Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions__

## Introduction

This article studies the algebraic norm that the multiplication of the general plain algebra carries, and the invertibility of its elements. The **algebraic norm of the multiplication** is the diagonal of its scalar-part form, the general plain bilinear algebraic norm
$$
\langle T\rangle=A^{2}+B^{2},
$$
complex-valued and indefinite, and it is **not multiplicative**. The invertibility is decided by a **different** quadratic form, the **reduced norm**
$$
\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B),
$$
which is the determinant of the multiplication, the reduced norm of the algebra and the algebraic norm of the general quaternionic bilinear product; an element is invertible exactly when $\langle T\rangle_{\natural}\neq0$, with the group of units the complement of the two punctured idempotent lines.

The distinction is the subject of the article. The word *norm* is used in the corpus for the diagonal of a scalar-part form (*Conventions in Mathematics*, §*The Conjugations*), and the multiplication carries exactly one such diagonal, the plain bilinear algebraic norm $\langle\cdot\rangle$; but $\langle\cdot\rangle$ is **not** the invertibility criterion of the multiplication, and the criterion is carried by another form. The article records the algebraic norm of the multiplication and, separately, the criterion, and it states the **absence** of a criterion from the algebraic norm rather than a criterion that does not exist — the pattern of *Norm and Invertibility in the Biquaternion Algebra* of the biquaternion category.

**The results.** The multiplication carries one algebraic norm, the diagonal of its scalar-part form, $\langle T\rangle=A^{2}+B^{2}$, complex-valued, indefinite of real signature $(2,2)$, of Gram matrix $\operatorname{diag}(1,-1,1,-1)$ on the real basis and $\operatorname{diag}(1,1)$ on the complex basis, with the complex quadric as its vanishing set. It is **not multiplicative**: $\langle TW\rangle\neq \langle T\rangle\langle W\rangle$ in general, the pair $T=\Pi_{1}$, $W=\Pi_{2}$ separating the two sides, $\langle \Pi_{1}\Pi_{2}\rangle=\langle 0\rangle=0$ against $\langle \Pi_{1}\rangle\langle \Pi_{2}\rangle=\tfrac14$. It does **not** decide invertibility: $\langle T\rangle=0$ does not force $T$ non-invertible and $\langle T\rangle\neq0$ does not force $T$ invertible. The criterion is the reduced norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$, which **is** multiplicative, $\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural}$, vanishes exactly on the zero divisors, and gives the group of units as the complement of the two punctured idempotent lines. Each section states its result first and then proves it.

**Boundaries.** The four products, the four forms and the four algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms*, above this article in this category; the reduced norm, its multiplicativity and its role as determinant are proved there, and they are used here as given. The algebra, its unit and its zero divisors are *Introduction to the General Plain Algebra of the Reduced Biquaternions*, above this article; the zero divisors and their geometry are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*, below this article; the definitions of the unit, the inverse and the group of units are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*. The structure of the group of units as a Lie group and its components are *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*, below this article in this category.

## The Algebraic Norm of the Multiplication

**The multiplication carries exactly one algebraic norm, the diagonal of its scalar-part form, $\langle T\rangle=A^{2}+B^{2}$; it is complex-valued and indefinite, and its vanishing set is the complex quadric.**

**Definition.** The **algebraic norm of the multiplication** is the diagonal of the scalar-part form of the multiplication,
$$
\langle T\rangle=\mathrm{Sc}\bigl(TT\bigr)=A^{2}+B^{2},
$$
equivalently $\langle T\rangle=\langle T,T\rangle$ for the general plain bilinear form
$$
\langle T,W\rangle=\mathrm{Sc}(TW)=AC+BD.
$$
The two arities of the letter are one object: with two arguments the form, with one argument its diagonal.

**Proposition (the values).** In the real coordinates $A=a+ia'$, $\langle\cdot,\cdot\rangle=b+ib'$,
$$
\langle T\rangle=a^{2}-a'^{2}+b^{2}-b'^{2}+2i(aa'+bb'),
$$
so $\langle\cdot,\cdot\rangle$ is **complex-valued**, real exactly on the quadric $aa'+bb'=0$, which contains the real subalgebra $\mathbb{R}\{1,j\}$ and its translate $i\mathbb{R}\{1,j\}$; it is **homogeneous of degree two**, $\langle \lambda T\rangle=\lambda^{2}\langle T\rangle$ for $\lambda\in\mathbb{C}$, with the form of the same letter as its polarisation, $\langle T+W\rangle-\langle T\rangle-\langle W\rangle=2B(T,W)$.

*Proof.* $A^{2}=(a^{2}-a'^{2})+2iaa'$ and $B^{2}=(b^{2}-b'^{2})+2ibb'$; adding gives the display. The reality set is where the imaginary part $2(aa'+bb')$ vanishes, the quadric $aa'+bb'=0$ of real dimension three, which contains the two real two-planes named. The homogeneity and the polarisation are the homogeneity and the polarisation of a quadratic form.

**Theorem (the Gram matrix and the signature).** On the complex basis $1,j$ the Gram matrix of $\langle\cdot,\cdot\rangle$ is $G_{B}=\operatorname{diag}(1,1)$; on the real basis $1,i,j,ij$ it is $\operatorname{diag}(1,-1,1,-1)$; the form is non-degenerate and its real signature is $(2,2)$; its vanishing set is the **complex quadric** $\{\langle T\rangle=0\}$.

*Proof.* $\langle 1,1\rangle=\langle j,j\rangle=1$ on the complex basis, since $j^{2}=1$; $\langle i,i\rangle=\mathrm{Sc}(i^{2})=-1$ and $\langle ij,ij\rangle=\mathrm{Sc}((ij)^{2})=-1$ on the real basis. The four diagonal entries being nonzero, the form is non-degenerate; two are positive and two negative, so the real signature is $(2,2)$. The vanishing set is the complex quadric, a complex cone, and it is **not** the zero-divisor cone of the algebra.

**Corollary (the norm of a product of two elements).** $\langle T\rangle=A^{2}+B^{2}$ vanishes exactly on the two complex lines $\mathbb{C}(1+ij)$ and $\mathbb{C}(1-ij)$, whose real forms are the planes $\mathbb{R}\{1+ij,\,i-j\}$ and $\mathbb{R}\{1-ij,\,i+j\}$, and it is not a sign of anything about invertibility; the next section proves the absence.

## The Algebraic Norm Is Not Multiplicative

**The algebraic norm of the multiplication is not multiplicative: $\langle TW\rangle\neq \langle T\rangle\langle W\rangle$ in general, and the pair $T=\Pi_{1}$, $W=\Pi_{2}$ separates the two sides.**

**Proposition.** The algebraic norm of the multiplication is **not** multiplicative:
$$
\langle TW\rangle\neq \langle T\rangle\,\langle W\rangle\quad\text{in general.}
$$

*Proof.* In the idempotent coordinates the multiplication is componentwise, $T=(q_1,q_2)$, $W=(q_1',q_2')$, with $q_1=A+B$ and $q_2=A-B$; the algebraic norm is $\langle T\rangle=A^{2}+B^{2}=\tfrac12(q_1^{2}+q_2^{2})$. The pair $T=\Pi_{1}=(1,0)$ and $W=\Pi_{2}=(0,1)$ gives $TW=0$, so $\langle TW\rangle=0$, while $\langle \Pi_{1}\rangle=\tfrac12(1+0)=\tfrac12$ and $\langle \Pi_{2}\rangle=\tfrac12(0+1)=\tfrac12$, and $\langle T\rangle\langle W\rangle=\tfrac14\neq0$. The two values differ, and multiplicativity fails.

**Remark (the multiplicative algebraic norm is another form).** Of the four algebraic norms of the space the multiplicative one is $\langle\cdot\rangle_{\natural}$, the algebraic norm of the general quaternionic bilinear product, $\langle T\rangle_{\natural}=A^{2}-B^{2}$; it is a different quadratic form on the same space, and it is **not** the algebraic norm of the multiplication. The multiplication is the ordinary product of a commutative ring with zero divisors, and its algebraic norm $\langle\cdot\rangle$, complex-valued and indefinite of signature $(2,2)$, fails multiplicativity and **does not decide invertibility either**, as the next section states.

## The Algebra Is Associative and Unital

**The multiplication is associative and unital, with the two-sided unit $1$ and a genuine group of units, a proper subset of the nonzero elements because the product has zero divisors.**

The unit of the multiplication is $1$, two-sided and unique, and the product is associative, so the inverse of an element is unique when it exists and the invertible elements form the **group of units** of the multiplication, a genuine group (*Introduction to the General Plain Algebra of the Reduced Biquaternions*; *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Unit and the Inverse*).

The multiplication has zero divisors: $\Pi_{1}\Pi_{2}=0$ with $\Pi_{1},\Pi_{2}$ nonzero. The algebra is therefore not a division algebra, and the group of units is a proper subset of $\mathbb{B}_{\mathrm{r}}\setminus\{0\}$. The zero divisors, their two lines and their geometry are *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*, and they are cited here, not read.

## The Reduced Norm and the Invertibility Criterion

**The invertibility of the multiplication is decided by the reduced norm $\langle T\rangle_{\natural}=A^{2}-B^{2}$, the determinant of the multiplication and the algebraic norm of the general quaternionic bilinear product; an element is a unit exactly when $\langle T\rangle_{\natural}\neq0$.**

**Theorem (the criterion).** For $T=A+Bj$,
$$
T\ \text{is invertible}\iff \langle T\rangle_{\natural}=A^{2}-B^{2}\neq0,\qquad
T^{-1}=\frac{A-Bj}{A^{2}-B^{2}}=\frac{T^{\natural}}{\langle T\rangle_{\natural}} .
$$

*Proof.* In the idempotent coordinates $T=(A+B,A-B)$, the multiplication is the componentwise product, so $T$ is invertible with inverse the pair of the inverses exactly when both coordinates are nonzero, that is when $(A+B)(A-B)=A^{2}-B^{2}=\langle T\rangle_{\natural}\neq0$. The inverse is then $((A+B)^{-1},(A-B)^{-1})$, which corresponds to the element $\tfrac12\bigl((A+B)^{-1}+(A-B)^{-1}\bigr)+\tfrac12\bigl((A+B)^{-1}-(A-B)^{-1}\bigr)j=\frac{A-Bj}{A^{2}-B^{2}}$, and the verification is $T(A-Bj)=A^{2}-B^{2}$.

**Theorem (multiplicativity).** The reduced norm is multiplicative under the multiplication,
$$
\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\,\langle W\rangle_{\natural},
$$
and it is the determinant of the multiplication in the idempotent coordinates.

*Proof.* In the idempotent coordinates the determinant is $q_1q_2$ with $q_1=A+B$ and $q_2=A-B$, equal to $\langle T\rangle_{\natural}$; a determinant of a componentwise product is the product of the determinants, so $\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural}$. The multiplicativity and the reduction to the two coordinates are *The Four Products, Their Forms and Their Algebraic Norms*, §*The Multiplicative Norm*.

**Remark (two forms, two roles).** The reduced norm $\langle\cdot\rangle_{\natural}$ is the algebraic norm of the **general quaternionic bilinear product** and the criterion of the **multiplication**; the two roles coincide because the determinant of the multiplication is the product of the two idempotent coordinates, which is the diagonal of the quaternionic bilinear form. The multiplication's own algebraic norm $\langle\cdot\rangle$ and the criterion $\langle\cdot\rangle_{\natural}$ are different quadratic forms on the same space, and the next section states the failure of $\langle\cdot,\cdot\rangle$ on both counts.

## The Group of Units

**The group of units of the multiplication is the complement of the two punctured idempotent lines, $\{T:\langle T\rangle_{\natural}\neq0\}=\{q_1\neq0\text{ and }q_2\neq0\}$, and it is the set on which the reduced norm is nonzero.**

**Theorem (the group of units).** The group of units is
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\bigl\{T=A+Bj:A+B\neq0\ \text{and}\ A-B\neq0\bigr\}=\bigl\{T:\langle T\rangle_{\natural}\neq0\bigr\},
$$
and it is isomorphic to $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ by the component map $\varphi$.

*Proof.* The criterion is the theorem above; the component map sends $T$ to $(A+B,A-B)$ and the product to the componentwise product, so it restricts to an isomorphism of the unit group onto the pairs of nonzero complex numbers. The group is **abelian**, and its identity is $1$.

The unit group is a proper subset of the nonzero elements, and its complement — the zero divisors and $0$ — is the union of the two idempotent lines. Its structure as a real Lie group, its components and its exponential are *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*, below this article in this category; the forms that measure its elements are *The Forms of the General Plain Algebra of the Reduced Biquaternions*.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm of the multiplication does not decide invertibility: $\langle T\rangle=0$ does not force $T$ non-invertible, and $\langle T\rangle\neq0$ does not force $T$ invertible.**

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the multiplication that statement is **false in both directions**, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** Neither implication holds:
$$
\langle T\rangle=0\ \not\Longrightarrow\ T\ \text{non-invertible},\qquad
\langle T\rangle\neq0\ \not\Longrightarrow\ T\ \text{invertible}.
$$

*Proof.* For the first implication, the element $T=1+ij$, of coordinates $A=1$ and $\langle\cdot,\cdot\rangle=i$, has $\langle T\rangle=A^{2}+B^{2}=1+i^{2}=0$, and it is a unit: $\langle T\rangle_{\natural}=A^{2}-B^{2}=1-i^{2}=2\neq0$, with inverse $T^{-1}=\tfrac12(1-ij)$, since $(1+ij)(1-ij)=1-(ij)^{2}=2$. So a unit has vanishing algebraic norm. For the second implication, the element $T=1+j$ has $\langle T\rangle=1^{2}+1^{2}=2\neq0$, and it is a zero divisor, $(1+j)(1-j)=1-j^{2}=0$, hence non-invertible while its algebraic norm does not vanish.

**Remark (the two witnesses).** The two witnesses are the two halves of the failure. The element $T=1+ij$ is invertible with vanishing algebraic norm, so the algebraic norm is not necessary for invertibility; the element $T=1+j$ is non-invertible with non-vanishing algebraic norm, so it is not sufficient either. The vanishing set of $\langle\cdot\rangle$ is the complex quadric and the zero-divisor set is the union of the two idempotent lines; the two curves meet only at the origin, and that is the geometric form of the absence.

**Remark (what replaces the criterion).** The multiplication is not left without an invertibility theory: it is associative and unital, the criterion is the reduced norm $\langle T\rangle_{\natural}\neq0$, every element of the group of units has an inverse, and the zero divisors are characterised in *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*. What the article records is that this theory is **not** read from the algebraic norm of the multiplication, which is the one algebraic norm the multiplication carries; the criterion is carried by a different quadratic form, the reduced norm $\langle\cdot\rangle_{\natural}$.

## Summary

The general plain bilinear product carries one algebraic norm, the diagonal of its scalar-part form, the general plain bilinear algebraic norm
$$
\langle T\rangle=\mathrm{Sc}\bigl(TT\bigr)=A^{2}+B^{2},
$$
complex-valued, of Gram matrix $\operatorname{diag}(1,1)$ on the complex basis and $\operatorname{diag}(1,-1,1,-1)$ on the real basis, real signature $(2,2)$, with the complex quadric as its vanishing set; it is **not multiplicative**, the pair $T=\Pi_{1}$, $W=\Pi_{2}$ separating the two sides, $\langle \Pi_{1}\Pi_{2}\rangle=0$ against $\langle \Pi_{1}\rangle\langle \Pi_{2}\rangle=\tfrac14$, and it **does not decide invertibility**, the unit $T=1+ij$ having $\langle\cdot,\cdot\rangle=0$ and the zero divisor $T=1+j$ having $\langle\cdot,\cdot\rangle=2$. The article records the absence.

The multiplication is associative and unital, with the two-sided unit $1$ and a genuine group of units, and it has zero divisors, $\Pi_{1}\Pi_{2}=0$. Its invertibility is decided by the **reduced norm**
$$
\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B),
$$
which is multiplicative, $\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural}$, which is the determinant of the multiplication and the algebraic norm of the general quaternionic bilinear product, and which vanishes exactly on the zero divisors; the group of units is the complement of the two punctured idempotent lines,
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\{T:\langle T\rangle_{\natural}\neq0\}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$
with inverse $T^{-1}=\langle T\rangle_{\natural}^{-1}(A-Bj)$. The two forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are different quadratic forms on the same space; the algebra's own algebraic norm is $\langle\cdot\rangle$, and the criterion is $\langle\cdot\rangle_{\natural}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle T\rangle=A^{2}+B^{2}$ | the algebraic norm of the multiplication, complex, not multiplicative |
| $\langle T,W\rangle=AC+BD$ | the general plain bilinear form |
| $\langle T\rangle_{\natural}=A^{2}-B^{2}$ | the reduced norm, the invertibility criterion, multiplicative |
| $T^{-1}=\langle T\rangle_{\natural}^{-1}(A-Bj)$ | the inverse of a unit |
| $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | the group of units |
| $\{B=0\}$ | the complex quadric, the vanishing set of the algebraic norm |
| $\{N=0\}$ | the two idempotent lines, the zero divisors |
| $T=1+ij$ (unit, $\langle\cdot\rangle=0$), $T=1+j$ (zero divisor, $\langle\cdot\rangle=2$) | the two witnesses of the failure of the algebraic norm |

## Further Reading

- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), above this article in this category, for the four products, the four forms and the four algebraic norms, and for the multiplicativity of the reduced norm.
- *Introduction to the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the algebra, its unit and its zero divisors.
- *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the null cone and its structure.
- *Annihilators of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the annihilators of the zero divisors.
- *Norm and Invertibility in the Biquaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.md`), the non-commutative counterpart, for the same separation of the algebraic norm from the criterion.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Unit and the Inverse*, for the definitions used here.

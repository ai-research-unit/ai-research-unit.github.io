# __Norm and Invertibility in the Algebra of the Reduced Biquaternions__

## Introduction

This article studies the algebraic norm that the multiplication of the general plain algebra carries, and the invertibility of its elements. The **algebraic norm of the multiplication** is the diagonal of its scalar-part form, the general plain bilinear algebraic norm
$$
\langle Q_\pm\rangle=Q_+^{2}+Q_-^{2},
$$
complex-valued and indefinite, and it is **not multiplicative**. The invertibility is decided by a **different** quadratic form, the **reduced norm**
$$
\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_++Q_-)(Q_+-Q_-),
$$
which is the determinant of the multiplication, the reduced norm of the algebra and the algebraic norm of the general quaternionic bilinear product; an element is invertible exactly when $\langle Q_\pm\rangle_{\natural}\neq0$, with the group of units the complement of the two punctured idempotent lines.

The distinction is the subject of the article. The word *norm* is used in the corpus for the diagonal of a scalar-part form (*Conventions in Mathematics*, §*The Conjugations*), and the multiplication carries exactly one such diagonal, the plain bilinear algebraic norm $\langle\cdot\rangle$; but $\langle\cdot\rangle$ is **not** the invertibility criterion of the multiplication, and the criterion is carried by another form. The article records the algebraic norm of the multiplication and, separately, the criterion, and it states the **absence** of a criterion from the algebraic norm rather than a criterion that does not exist — the pattern of *Norm and Invertibility in the Biquaternion Algebra* of the biquaternion category.

**The results.** The multiplication carries one algebraic norm, the diagonal of its scalar-part form, $\langle Q_\pm\rangle=Q_+^{2}+Q_-^{2}$, complex-valued, indefinite of real signature $(2,2)$, of Gram matrix $\operatorname{diag}(1,-1,1,-1)$ on the real basis and $\operatorname{diag}(1,1)$ on the complex basis, with the complex quadric as its vanishing set. It is **not multiplicative**: $\langle Q_{\pm,1}Q_{\pm,2}\rangle\neq \langle Q_{\pm,1}\rangle\langle Q_{\pm,2}\rangle$ in general, the pair $Q_{\pm,1}=\Pi_+$, $Q_{\pm,2}=\Pi_-$ separating the two sides, $\langle \Pi_+\Pi_-\rangle=\langle 0\rangle=0$ against $\langle \Pi_+\rangle\langle \Pi_-\rangle=\tfrac14$. It does **not** decide invertibility: $\langle Q_\pm\rangle=0$ does not force $Q_\pm$ non-invertible and $\langle Q_\pm\rangle\neq0$ does not force $Q_\pm$ invertible. The criterion is the reduced norm $\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}$, which **is** multiplicative, $\langle Q_{\pm,1}Q_{\pm,2}\rangle_{\natural}=\langle Q_{\pm,1}\rangle_{\natural}\langle Q_{\pm,2}\rangle_{\natural}$, vanishes exactly on the zero divisors, and gives the group of units as the complement of the two punctured idempotent lines. Each section states its result first and then proves it.

**Boundaries.** The four products, the four forms and the four algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms*, above this article in this category; the reduced norm, its multiplicativity and its role as determinant are proved there, and they are used here as given. The algebra, its unit and its zero divisors are *Introduction to the Algebra of the Reduced Biquaternions*, above this article; the zero divisors and their geometry are *Zero Divisors of the Algebra of the Reduced Biquaternions*, below this article; the definitions of the unit, the inverse and the group of units are *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*. The structure of the group of units as a Lie group and its components are *The Group of Units of the Algebra of the Reduced Biquaternions*, below this article in this category.

## The Algebraic Norm of the Multiplication

**The multiplication carries exactly one algebraic norm, the diagonal of its scalar-part form, $\langle Q_\pm\rangle=Q_+^{2}+Q_-^{2}$; it is complex-valued and indefinite, and its vanishing set is the complex quadric.**

**Definition.** The **algebraic norm of the multiplication** is the diagonal of the scalar-part form of the multiplication,
$$
\langle Q_\pm\rangle=\mathrm{Sc}\bigl(Q_\pm Q_\pm\bigr)=Q_+^{2}+Q_-^{2},
$$
equivalently $\langle Q_\pm\rangle=\langle Q_\pm,Q_\pm\rangle$ for the general plain bilinear form
$$
\langle Q_{\pm,1},Q_{\pm,2}\rangle=\mathrm{Sc}(Q_{\pm,1}Q_{\pm,2})=Q_{1+}Q_{2+}+Q_{1-}Q_{2-}.
$$
The two arities of the letter are one object: with two arguments the form, with one argument its diagonal.

**Proposition (the values).** In the real coordinates $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$,
$$
\langle Q_\pm\rangle=q_+^{2}-q'^{2}_{+}+q_-^{2}-q'^{2}_{-}+2i(q_+q'_++q_-q'_-),
$$
so $\langle\cdot,\cdot\rangle$ is **complex-valued**, real exactly on the quadric $q_+q'_++q_-q'_-=0$, which contains the real subalgebra $\mathbb{R}\{1,j\}$ and its translate $i\mathbb{R}\{1,j\}$; it is **homogeneous of degree two**, $\langle \lambda Q_\pm\rangle=\lambda^{2}\langle Q_\pm\rangle$ for $\lambda\in\mathbb{C}$, with the form of the same letter as its polarisation, $\langle Q_{\pm,1}+Q_{\pm,2}\rangle-\langle Q_{\pm,1}\rangle-\langle Q_{\pm,2}\rangle=2B(Q_{\pm,1},Q_{\pm,2})$.

*Proof.* $Q_+^{2}=(q_+^{2}-q'^{2}_{+})+2iq_+q'_+$ and $Q_-^{2}=(q_-^{2}-q'^{2}_{-})+2iq_-q'_-$; adding gives the display. The reality set is where the imaginary part $2(q_+q'_++q_-q'_-)$ vanishes, the quadric $q_+q'_++q_-q'_-=0$ of real dimension three, which contains the two real two-planes named. The homogeneity and the polarisation are the homogeneity and the polarisation of a quadratic form.

**Theorem (the Gram matrix and the signature).** On the complex basis $1,j$ the Gram matrix of $\langle\cdot,\cdot\rangle$ is $G_{B}=\operatorname{diag}(1,1)$; on the real basis $1,i,j,ij$ it is $\operatorname{diag}(1,-1,1,-1)$; the form is non-degenerate and its real signature is $(2,2)$; its vanishing set is the **complex quadric** $\{\langle Q_\pm\rangle=0\}$.

*Proof.* $\langle 1,1\rangle=\langle j,j\rangle=1$ on the complex basis, since $j^{2}=1$; $\langle i,i\rangle=\mathrm{Sc}(i^{2})=-1$ and $\langle ij,ij\rangle=\mathrm{Sc}((ij)^{2})=-1$ on the real basis. The four diagonal entries being nonzero, the form is non-degenerate; two are positive and two negative, so the real signature is $(2,2)$. The vanishing set is the complex quadric, a complex cone, and it is **not** the zero-divisor cone of the algebra.

**Corollary (the norm of a product of two elements).** $\langle Q_\pm\rangle=Q_+^{2}+Q_-^{2}$ vanishes exactly on the two complex lines $\mathbb{C}(1+ij)$ and $\mathbb{C}(1-ij)$, whose real forms are the planes $\mathbb{R}\{1+ij,\,i-j\}$ and $\mathbb{R}\{1-ij,\,i+j\}$, and it is not a sign of anything about invertibility; the next section proves the absence.

## The Algebraic Norm Is Not Multiplicative

**The algebraic norm of the multiplication is not multiplicative: $\langle Q_{\pm,1}Q_{\pm,2}\rangle\neq \langle Q_{\pm,1}\rangle\langle Q_{\pm,2}\rangle$ in general, and the pair $Q_{\pm,1}=\Pi_+$, $Q_{\pm,2}=\Pi_-$ separates the two sides.**

**Proposition.** The algebraic norm of the multiplication is **not** multiplicative:
$$
\langle Q_{\pm,1}Q_{\pm,2}\rangle\neq \langle Q_{\pm,1}\rangle\,\langle Q_{\pm,2}\rangle\quad\text{in general.}
$$

*Proof.* In the idempotent coordinates the multiplication is componentwise, $Q_{\pm,1}=(Q_{1++},Q_{1--})$, $Q_{\pm,2}=(Q_{2++},Q_{2--})$, with $Q_{1++}=Q_{1+}+Q_{1-}$ and $Q_{1--}=Q_{1+}-Q_{1-}$; the algebraic norm is $\langle Q_{\pm,1}\rangle=Q_{1+}^{2}+Q_{1-}^{2}=\tfrac12(Q_{1++}^{2}+Q_{1--}^{2})$. The pair $Q_{\pm,1}=\Pi_+=(1,0)$ and $Q_{\pm,2}=\Pi_-=(0,1)$ gives $Q_{\pm,1}Q_{\pm,2}=0$, so $\langle Q_{\pm,1}Q_{\pm,2}\rangle=0$, while $\langle \Pi_+\rangle=\tfrac12(1+0)=\tfrac12$ and $\langle \Pi_-\rangle=\tfrac12(0+1)=\tfrac12$, and $\langle Q_{\pm,1}\rangle\langle Q_{\pm,2}\rangle=\tfrac14\neq0$. The two values differ, and multiplicativity fails.

**Remark (the multiplicative algebraic norm is another form).** Of the four algebraic norms of the space the multiplicative one is $\langle\cdot\rangle_{\natural}$, the algebraic norm of the general quaternionic bilinear product, $\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}$; it is a different quadratic form on the same space, and it is **not** the algebraic norm of the multiplication. The multiplication is the ordinary product of a commutative ring with zero divisors, and its algebraic norm $\langle\cdot\rangle$, complex-valued and indefinite of signature $(2,2)$, fails multiplicativity and **does not decide invertibility either**, as the next section states.

## The Algebra Is Associative and Unital

**The multiplication is associative and unital, with the two-sided unit $1$ and a genuine group of units, a proper subset of the nonzero elements because the product has zero divisors.**

The unit of the multiplication is $1$, two-sided and unique, and the product is associative, so the inverse of an element is unique when it exists and the invertible elements form the **group of units** of the multiplication, a genuine group (*Introduction to the Algebra of the Reduced Biquaternions*; *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space*, §*The Unit and the Inverse*).

The multiplication has zero divisors: $\Pi_+\Pi_-=0$ with $\Pi_+,\Pi_-$ nonzero. The algebra is therefore not a division algebra, and the group of units is a proper subset of $\mathbb{B}_{\mathrm{r}}\setminus\{0\}$. The zero divisors, their two lines and their geometry are *Zero Divisors of the Algebra of the Reduced Biquaternions*, and they are cited here, not read.

## The Reduced Norm and the Invertibility Criterion

**The invertibility of the multiplication is decided by the reduced norm $\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}$, the determinant of the multiplication and the algebraic norm of the general quaternionic bilinear product; an element is a unit exactly when $\langle Q_\pm\rangle_{\natural}\neq0$.**

**Theorem (the criterion).** For $Q_\pm=Q_++jQ_-$,
$$
Q_\pm\ \text{is invertible}\iff \langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}\neq0,\qquad
Q_\pm^{-1}=\frac{Q_+-jQ_-}{Q_+^{2}-Q_-^{2}}=\frac{Q_\pm^{\natural}}{\langle Q_\pm\rangle_{\natural}} .
$$

*Proof.* In the idempotent coordinates $Q_\pm=(Q_{++},Q_{--})$, the multiplication is the componentwise product, so $Q_\pm$ is invertible with inverse the pair of the inverses exactly when both coordinates are nonzero, that is when $(Q_++Q_-)(Q_+-Q_-)=Q_+^{2}-Q_-^{2}=\langle Q_\pm\rangle_{\natural}\neq0$. The inverse is then $((Q_++Q_-)^{-1},(Q_+-Q_-)^{-1})$, which corresponds to the element $\tfrac12\bigl((Q_++Q_-)^{-1}+(Q_+-Q_-)^{-1}\bigr)+\tfrac12\bigl((Q_++Q_-)^{-1}-(Q_+-Q_-)^{-1}\bigr)j=\frac{Q_+-jQ_-}{Q_+^{2}-Q_-^{2}}$, and the verification is $Q_\pm(Q_+-jQ_-)=Q_+^{2}-Q_-^{2}$.

**Theorem (multiplicativity).** The reduced norm is multiplicative under the multiplication,
$$
\langle Q_{\pm,1}Q_{\pm,2}\rangle_{\natural}=\langle Q_{\pm,1}\rangle_{\natural}\,\langle Q_{\pm,2}\rangle_{\natural},
$$
and it is the determinant of the multiplication in the idempotent coordinates.

*Proof.* In the idempotent coordinates the determinant is $Q_{++}Q_{--}$ with $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, equal to $\langle Q_\pm\rangle_{\natural}$; a determinant of a componentwise product is the product of the determinants, so $\langle Q_{\pm,1}Q_{\pm,2}\rangle_{\natural}=\langle Q_{\pm,1}\rangle_{\natural}\langle Q_{\pm,2}\rangle_{\natural}$. The multiplicativity and the reduction to the two coordinates are *The Four Products, Their Forms and Their Algebraic Norms*, §*The Multiplicative Norm*.

**Remark (two forms, two roles).** The reduced norm $\langle\cdot\rangle_{\natural}$ is the algebraic norm of the **general quaternionic bilinear product** and the criterion of the **multiplication**; the two roles coincide because the determinant of the multiplication is the product of the two idempotent coordinates, which is the diagonal of the quaternionic bilinear form. The multiplication's own algebraic norm $\langle\cdot\rangle$ and the criterion $\langle\cdot\rangle_{\natural}$ are different quadratic forms on the same space, and the next section states the failure of $\langle\cdot,\cdot\rangle$ on both counts.

## The Group of Units

**The group of units of the multiplication is the complement of the two punctured idempotent lines, $\{Q_\pm:\langle Q_\pm\rangle_{\natural}\neq0\}=\{Q_{++}\neq0\text{ and }Q_{--}\neq0\}$, and it is the set on which the reduced norm is nonzero.**

**Theorem (the group of units).** The group of units is
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\bigl\{Q_\pm=Q_++jQ_-:Q_++Q_-\neq0\ \text{and}\ Q_+-Q_-\neq0\bigr\}=\bigl\{Q_\pm:\langle Q_\pm\rangle_{\natural}\neq0\bigr\},
$$
and it is isomorphic to $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ by the component map $\varphi$.

*Proof.* The criterion is the theorem above; the component map sends $Q_\pm$ to $(Q_++Q_-,Q_+-Q_-)$ and the product to the componentwise product, so it restricts to an isomorphism of the unit group onto the pairs of nonzero complex numbers. The group is **abelian**, and its identity is $1$.

The unit group is a proper subset of the nonzero elements, and its complement — the zero divisors and $0$ — is the union of the two idempotent lines. Its structure as a real Lie group, its components and its exponential are *The Group of Units of the Algebra of the Reduced Biquaternions*, below this article in this category; the forms that measure its elements are *The Forms of the Algebra of the Reduced Biquaternions*.

## The Absence of a Criterion from the Algebraic Norm

**The algebraic norm of the multiplication does not decide invertibility: $\langle Q_\pm\rangle=0$ does not force $Q_\pm$ non-invertible, and $\langle Q_\pm\rangle\neq0$ does not force $Q_\pm$ invertible.**

The algebraic norm of a product would decide invertibility if the invertible elements were exactly the elements of non-vanishing algebraic norm. For the multiplication that statement is **false in both directions**, and the article records the absence rather than a criterion.

**Theorem (the algebraic norm does not decide invertibility).** Neither implication holds:
$$
\langle Q_\pm\rangle=0\ \not\Longrightarrow\ Q_\pm\ \text{non-invertible},\qquad
\langle Q_\pm\rangle\neq0\ \not\Longrightarrow\ Q_\pm\ \text{invertible}.
$$

*Proof.* For the first implication, the element $Q_\pm=1+ij$, of coordinates $Q_+=1$ and $Q_-=i$, has $\langle Q_\pm\rangle=Q_+^{2}+Q_-^{2}=1+i^{2}=0$, and it is a unit: $\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}=1-i^{2}=2\neq0$, with inverse $Q_\pm^{-1}=\tfrac12(1-ij)$, since $(1+ij)(1-ij)=1-(ij)^{2}=2$. So a unit has vanishing algebraic norm. For the second implication, the element $Q_\pm=1+j$ has $\langle Q_\pm\rangle=1^{2}+1^{2}=2\neq0$, and it is a zero divisor, $(1+j)(1-j)=1-j^{2}=0$, hence non-invertible while its algebraic norm does not vanish.

**Remark (the two witnesses).** The two witnesses are the two halves of the failure. The element $Q_\pm=1+ij$ is invertible with vanishing algebraic norm, so the algebraic norm is not necessary for invertibility; the element $Q_\pm=1+j$ is non-invertible with non-vanishing algebraic norm, so it is not sufficient either. The vanishing set of $\langle\cdot\rangle$ is the complex quadric and the zero-divisor set is the union of the two idempotent lines; the two curves meet only at the origin, and that is the geometric form of the absence.

**Remark (what replaces the criterion).** The multiplication is not left without an invertibility theory: it is associative and unital, the criterion is the reduced norm $\langle Q_\pm\rangle_{\natural}\neq0$, every element of the group of units has an inverse, and the zero divisors are characterised in *Zero Divisors of the Algebra of the Reduced Biquaternions*. What the article records is that this theory is **not** read from the algebraic norm of the multiplication, which is the one algebraic norm the multiplication carries; the criterion is carried by a different quadratic form, the reduced norm $\langle\cdot\rangle_{\natural}$.

## Summary

The general plain bilinear product carries one algebraic norm, the diagonal of its scalar-part form, the general plain bilinear algebraic norm
$$
\langle Q_\pm\rangle=\mathrm{Sc}\bigl(Q_\pm Q_\pm\bigr)=Q_+^{2}+Q_-^{2},
$$
complex-valued, of Gram matrix $\operatorname{diag}(1,1)$ on the complex basis and $\operatorname{diag}(1,-1,1,-1)$ on the real basis, real signature $(2,2)$, with the complex quadric as its vanishing set; it is **not multiplicative**, the pair $Q_{\pm,1}=\Pi_+$, $Q_{\pm,2}=\Pi_-$ separating the two sides, $\langle \Pi_+\Pi_-\rangle=0$ against $\langle \Pi_+\rangle\langle \Pi_-\rangle=\tfrac14$, and it **does not decide invertibility**, the unit $Q_\pm=1+ij$ having $\langle Q_\pm\rangle=0$ and the zero divisor $Q_\pm=1+j$ having $\langle Q_\pm\rangle=2$. The article records the absence.

The multiplication is associative and unital, with the two-sided unit $1$ and a genuine group of units, and it has zero divisors, $\Pi_+\Pi_-=0$. Its invertibility is decided by the **reduced norm**
$$
\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_++Q_-)(Q_+-Q_-),
$$
which is multiplicative, $\langle Q_{\pm,1}Q_{\pm,2}\rangle_{\natural}=\langle Q_{\pm,1}\rangle_{\natural}\langle Q_{\pm,2}\rangle_{\natural}$, which is the determinant of the multiplication and the algebraic norm of the general quaternionic bilinear product, and which vanishes exactly on the zero divisors; the group of units is the complement of the two punctured idempotent lines,
$$
\mathbb{B}_{\mathrm{r}}^{\times}=\{Q_\pm:\langle Q_\pm\rangle_{\natural}\neq0\}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$
with inverse $Q_\pm^{-1}=\langle Q_\pm\rangle_{\natural}^{-1}(Q_+-jQ_-)$. The two forms $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{\natural}$ are different bilinear forms on the same space; the algebra's own algebraic norm is $\langle\cdot\rangle$, and the criterion is $\langle\cdot\rangle_{\natural}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle Q_\pm\rangle=Q_+^{2}+Q_-^{2}$ | the algebraic norm of the multiplication, complex, not multiplicative |
| $\langle Q_{\pm,1},Q_{\pm,2}\rangle=Q_{1+}Q_{2+}+Q_{1-}Q_{2-}$ | the general plain bilinear form |
| $\langle Q_\pm\rangle_{\natural}=Q_+^{2}-Q_-^{2}$ | the reduced norm, the invertibility criterion, multiplicative |
| $Q_\pm^{-1}=\langle Q_\pm\rangle_{\natural}^{-1}(Q_+-jQ_-)$ | the inverse of a unit |
| $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | the group of units |
| $\{B=0\}$ | the complex quadric, the vanishing set of the algebraic norm |
| $\{N=0\}$ | the two idempotent lines, the zero divisors |
| $Q_\pm=1+ij$ (unit, $\langle Q_\pm\rangle=0$), $Q_\pm=1+j$ (zero divisor, $\langle Q_\pm\rangle=2$) | the two witnesses of the failure of the algebraic norm |

## Further Reading

- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), above this article in this category, for the four products, the four forms and the four algebraic norms, and for the multiplicativity of the reduced norm.
- *Introduction to the Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), above this article, for the algebra, its unit and its zero divisors.
- *Zero Divisors of the Algebra of the Reduced Biquaternions* (`articles_maths/zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the null cone and its structure.
- *Annihilators of the Algebra of the Reduced Biquaternions* (`articles_maths/annihilators-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), below this article, for the annihilators of the zero divisors.
- *Norm and Invertibility in the Biquaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-biquaternion-algebra.md`), the non-commutative counterpart, for the same separation of the algebraic norm from the criterion.
- *Definitions for the Study of the Algebraic Structures over the Biquaternioid $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), §*The Unit and the Inverse*, for the definitions used here.

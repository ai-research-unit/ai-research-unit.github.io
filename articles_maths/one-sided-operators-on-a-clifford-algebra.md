
# __One-Sided Operators on a Clifford Algebra__

## Introduction

Every two-sided operator of *Two-Sided Operators on a Clifford Algebra* is a product of two factors, one multiplying on the left and one on the right. This article treats the factors themselves, in the general theory in which no involution of the base is assumed. A **one-sided operator** is a left multiplication $y\mapsto \theta(x)\,y$, attached to an automorphism $\theta$, or a right multiplication $y\mapsto y\,c(x)$, attached to an anti-automorphism $c$. The one-sided operators are the elementary operators out of which the two-sided family is built, they are the operators that carry the regular representations of the algebra and of its opposite, and their images are the ideals of the algebra, so they are where the module theory of the Clifford algebra begins.

Two facts organise the theory. The first is that the left family and the twisted right family are separately **multiplicative in the same order**, while the plain right multiplication is **anti-multiplicative**: the reversal inside an anti-automorphism cancels the reversal of the order of composition, but the identity that gives the plain right multiplication does not, and $x\mapsto R_x$ is a representation of the opposite algebra. The second is that the left and the right multiplications are **mutual commutants**, $\{L_a\}'=\{R_b\}$ and $\{R_b\}'=\{L_a\}$, which is the double centraliser theorem read on the regular bimodule. What the two families generate together is the image of the enveloping algebra $A\otimes_F A^{\mathrm{op}}$ in $\mathrm{End}_F(A)$; it is all of $\mathrm{End}_F(A)$ exactly when $A=\mathrm{Cl}(V,q)$ is central simple over $F$, and it is a proper subalgebra otherwise.

The last structural point is the reason two-sided operators exist at all. A left multiplication by a non-scalar never carries the subspace $V$ of vectors into itself, and the only one-sided operators that preserve $V$ are the scalars. Preservation of the quadratic space, which is what turns an operator into a geometric transformation, therefore requires the pairing of a left factor with a right factor, and it is the two-sided operators, not the one-sided ones, that act on $V$ by isometries.

The algebra, the parity grading and the intrinsic anti-involutions are *Clifford Algebras* and *Clifford Algebras in Finite Dimensions*; the two-sided family and its composition law are *Two-Sided Operators on a Clifford Algebra*; the signed inner conjugation, the Clifford group and its action on $V$ are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; the primitive idempotents, the minimal left ideals and the spinor module are *Spinors as Minimal Left Ideals with Inner Conjugation*; the involution of the base, the dagger and the Hermitian sandwich are *Hilbert Algebras*; and the dagger, the Hermitian adjoint and the module-level action are the Hermitian group, *One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint*, *The Adjoint of the One-Sided Action with Hermitian Adjoint* and *Hermitian Modules over a Hilbert Algebra with Hermitian Adjoint*. The base is a field $F$ of characteristic not $2$, and $q$ is a non-degenerate quadratic form on the finite-dimensional space $V$ with polar form $B$.

## The Two One-Sided Families

### Definitions

**Definition.** Let $\theta$ be an automorphism of $\mathrm{Cl}(V,q)$ and let $c$ be an anti-automorphism, so that $c(xz)=c(z)c(x)$ and $c(1)=1$. For $x\in\mathrm{Cl}(V,q)$ the **left one-sided operator** and the **right one-sided operator** attached to $x$ are the $F$-linear maps

$$
\Lambda^{\theta}_x(y)=\theta(x)\,y, \qquad \qquad \mathrm P^{c}_x(y)=y\,c(x).
$$

With $\theta=\mathrm{id}$ this gives the left multiplication $L_x=\Lambda^{\mathrm{id}}_x$, and with $\theta=\alpha$ the signed left multiplication $L_{\alpha(x)}=\Lambda^{\alpha}_x$. With $c=r$ it gives the reversion-twisted right multiplication $R_{x^{r}}=\mathrm P^{r}_x$, and with $c=\bar\cdot$ the conjugation-twisted one $R_{x^{\natural}}=\mathrm P^{\bar\cdot}_x$. The plain right multiplication $R_x$ is $\mathrm P^{\mathrm{id}}_x$, and the identity is an automorphism and not an anti-automorphism, which is the source of the exception in the composition law below. The inverse variants are defined on the units.

### The Composition Laws

**Proposition.** Let $\theta$ be an automorphism and let $c$ be an anti-automorphism. Then

$$
\Lambda^{\theta}_{xz}=\Lambda^{\theta}_x\circ\Lambda^{\theta}_z, \qquad \qquad \mathrm P^{c}_{xz}=\mathrm P^{c}_x\circ\mathrm P^{c}_z .
$$

**Proof.** For the left family, $\Lambda^{\theta}_x(\Lambda^{\theta}_z(y))=\theta(x)\theta(z)\,y=\theta(xz)\,y$. For the right family, $\mathrm P^{c}_x(\mathrm P^{c}_z(y))=\mathrm P^{c}_x\bigl(y\,c(z)\bigr)=y\,c(z)c(x)=y\,c(xz)$, where the reversal in $c$ is compensated by the reversal of the order of composition.

**Proposition (the plain right multiplication is anti-multiplicative).** The identity $R_{xz}=R_x\circ R_z$ of the previous proposition **fails** for the identity automorphism; instead

$$
R_{xz}=R_z\circ R_x ,
$$

so $x\mapsto R_x$ is a homomorphism from the **opposite algebra** $\mathrm{Cl}(V,q)^{\mathrm{op}}$ and an anti-homomorphism from $\mathrm{Cl}(V,q)$.

**Proof.** $R_x(R_z(y))=(y z)x=y(z x)=R_{zx}(y)$.

**Example.** In $\mathrm{Cl}_{0,3}(\mathbb{R})$ at the unit, $L_{e_1}L_{e_2}(1)=e_1e_2=L_{e_1e_2}(1)$, while $R_{e_1}R_{e_2}(1)=e_2e_1=-e_1e_2$, whereas $R_{e_1e_2}(1)=e_1e_2$; so $R_{e_1}R_{e_2}=-R_{e_1e_2}$ and the plain right family indeed composes in the reverse order.

**Remark.** The asymmetry is forced and is not a defect of the notation. The left family multiplies by the element on the left, so its composition follows the order of the elements; the right family multiplies on the right, so its composition reverses that order unless an anti-automorphism supplies a second reversal. The twisted family $\mathrm P^{c}$ recovers the same order precisely because $c$ reverses for it.

### Commutation and the Return to the Two-Sided Operator

**Proposition.** The left and the right families commute,

$$
\Lambda^{\theta}_x\circ\mathrm P^{c}_z=\mathrm P^{c}_z\circ\Lambda^{\theta}_x ,
$$

and the two-sided operator of *Two-Sided Operators on a Clifford Algebra* is their product,

$$
\Phi^{\theta,c}_x=\Lambda^{\theta}_x\circ\mathrm P^{c}_x=L_{\theta(x)}\,R_{c(x)} .
$$

**Proof.** $\bigl(\theta(x)y\bigr)c(z)=\theta(x)\bigl(y\,c(z)\bigr)$ by associativity, and the two-sided operator is the product by its definition.

**Corollary (the composition law, again).** The law $\Phi^{\theta,c}_{xz}=\Phi^{\theta,c}_x\circ\Phi^{\theta,c}_z$ follows from the two one-sided laws: $\Phi_x\Phi_z=\Lambda^{\theta}_x\mathrm P^{c}_x\Lambda^{\theta}_z\mathrm P^{c}_z=\Lambda^{\theta}_{xz}\mathrm P^{c}_{xz}=\Phi_{xz}$. So the multiplicativity of the two-sided family is inherited from the multiplicativity of its factors, and the commutation of the two factors is what makes the product unambiguous.

### The Value at the Unit and the Parity

**Proposition.** For every $x$ one has $\Lambda^{\theta}_x(1)=\theta(x)$ and $\mathrm P^{c}_x(1)=c(x)$; in particular $L_x(1)=R_x(1)=x$. The members are therefore told apart by their value at the unit.

| operator | value at $1$ |
|---|---|
| $L_x=\Lambda^{\mathrm{id}}_x$ | $x$ |
| $L_{\alpha(x)}=\Lambda^{\alpha}_x$ | $\alpha(x)$, that is $\pm x$ by parity |
| $R_x$ | $x$ |
| $R_{x^{r}}=\mathrm P^{r}_x$ | $x^{r}$ |
| $R_{x^{\natural}}=\mathrm P^{\bar\cdot}_x$ | $x^{\natural}$ |

**Proposition (the parity).** The left multiplication $L_x$, and likewise $R_x$, preserves the parity grading when $x$ is even and interchanges its two components when $x$ is odd; in general $\Lambda^{\theta}_x(\mathrm{Cl}^{i})\subseteq\mathrm{Cl}^{i+|\theta(x)|}$, the exponent read modulo two.

**Proof.** A product of two basis blades is again a basis blade, of degree the sum of the two degrees modulo two; a general element is a sum of homogeneous components.

**Remark.** The two-sided operators of *Two-Sided Operators on a Clifford Algebra* preserve the parity for every $x$, because each of them is a product of two factors of the same parity. So the parity-preserving property is a property of the pair, not of the individual one-sided operator, and an odd left multiplication is a parity-swapping operator that becomes parity-preserving once paired with an odd right factor.

## The Anti-Involution Variants and the Involutions

The graded and twisted one-sided operators are conjugates of the plain multiplications by the intrinsic anti-involutions of the algebra. This is the general reason a two-sided operator, which pairs a left factor with a right factor, is an automorphism of the algebra when the two factors are matched.

**Proposition.** Let $\alpha$ be the grade involution, $r$ reversion and $x^{\natural}=\alpha(x^{r})$ Clifford conjugation. Then

$$
L_{\alpha(x)}=\alpha\circ L_x\circ\alpha, \qquad R_{x^{r}}=r\circ L_x\circ r, \qquad R_{x^{\natural}}=\bar\cdot\circ L_x\circ\bar\cdot, \qquad L_{x^{r}}=r\circ R_x\circ r .
$$

**Proof.** Each identity is a direct computation. For the first, $\alpha\bigl(L_x(\alpha(y))\bigr)=\alpha\bigl(x\,\alpha(y)\bigr)=\alpha(x)\,y$. For the second, $r\bigl(L_x(r(y))\bigr)=r\bigl(x\,r(y)\bigr)=y\,x^{r}$. The third is the second with $\alpha(x)$ in place of $x$, and the fourth is the second with the roles of $r$ and $R$ exchanged.

**Remark.** The identities are the general form of the statement that the **sandwich** is a conjugate of a multiplication. The two-sided operators with a right factor the inverse are the inner conjugation and the signed inner conjugation, and they are the members that act on $V$ by isometries; the ones with a right factor an anti-involution are the inverse-free members. Nothing here uses an involution of the base, so the dagger variant of the right family, $R_{x^{\dagger}}$, is absent; it requires the involutive theory and belongs to *One-Sided Operators on a Hilbert Algebra with Hermitian Adjoint*.

## Injectivity, Kernels and Ideals

**Proposition.** For every $a$ one has $L_a(1)=R_a(1)=a$, so $a\mapsto L_a$ and $a\mapsto R_a$ are injective $F$-linear maps from the algebra into its endomorphisms.

**Proposition (kernels).** The kernel of a one-sided operator is an annihilator:

$$
\ker L_a=\{\,y : ay=0\,\}=\ell(a), \qquad \ker R_a=\{\,y : ya=0\,\}=r(a),
$$

the left and the right annihilator of $a$.

**Proposition (images).** The image of a left multiplication is a **right** ideal and the image of a right multiplication is a **left** ideal:

$$
L_a\bigl(\mathrm{Cl}(V,q)\bigr)=a\cdot\mathrm{Cl}(V,q), \qquad R_a\bigl(\mathrm{Cl}(V,q)\bigr)=\mathrm{Cl}(V,q)\cdot a .
$$

**Proof.** $L_a(y)=ay$ and $(ay)x=a(yx)$ is again in $a\cdot\mathrm{Cl}$; $R_a(y)=ya$ and $x(ya)=(xy)a$ is again in $\mathrm{Cl}\cdot a$.

**Corollary (the spinor module as an image).** If $\pi$ is a primitive idempotent then $R_\pi$ has image the minimal left ideal $\mathrm{Cl}(V,q)\,\pi$ and $L_\pi$ has image the minimal right ideal $\pi\,\mathrm{Cl}(V,q)$. The spinor module of *Spinors as Minimal Left Ideals with Inner Conjugation* is the image of the one-sided operator $R_\pi$, so the elementary one-sided operators already carry the module theory of the algebra.

## The Algebra Generated by the One-Sided Operators

### The Mutual Commutants

**Theorem (double centraliser).** The commutant of the left multiplications is the right multiplications and conversely,

$$
\{L_a : a\in\mathrm{Cl}(V,q)\}'=\{\,R_b\}, \qquad \{\,R_b\}'=\{L_a\}.
$$

**Proof.** An operator $T$ commutes with every $L_a$ exactly when $T(ay)=aT(y)$ for all $a,y$, that is exactly when $T$ is left $\mathrm{Cl}(V,q)$-linear; such a $T$ is determined by its value at $1$, since $T(y)=T(y\cdot1)=y\,T(1)$, so $T=R_{T(1)}$. The second identity is the same statement with the multiplication reversed.

**Remark.** The theorem is the double centraliser theorem for the regular bimodule, and it is the statement that the left and the right multiplications are each other's commutant. It does not say that they generate all of $\mathrm{End}_F(\mathrm{Cl}(V,q))$, and that stronger statement is false in general, as the next proposition shows.

### The Image of the Enveloping Algebra

**Proposition.** The left and the right multiplications together generate the image of the enveloping algebra under

$$
\mathrm{Cl}(V,q)\otimes_F\mathrm{Cl}(V,q)^{\mathrm{op}}\longrightarrow\mathrm{End}_F\bigl(\mathrm{Cl}(V,q)\bigr), \qquad a\otimes b\mapsto\bigl(y\mapsto a\,y\,b\bigr),
$$

an algebra homomorphism. The image is all of $\mathrm{End}_F(\mathrm{Cl}(V,q))$, of dimension $(\dim\mathrm{Cl})^2$, exactly when $\mathrm{Cl}(V,q)$ is **central simple** over $F$; otherwise it is a proper subalgebra.

**Verified.** The dimension of the span of the maps $y\mapsto ayb$ over a basis is $(\dim\mathrm{Cl})^2$ for the central simple algebras $\mathrm{Cl}_{0,2}(\mathbb{R})\cong\mathbb{H}$, $\mathrm{Cl}_{0,4}(\mathbb{R})\cong\mathbb{H}(2)$ and $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$, and it is half of $(\dim\mathrm{Cl})^2$ for $\mathrm{Cl}_{0,3}(\mathbb{R})\cong\mathbb{H}\oplus\mathbb{H}$ and for $\mathrm{Cl}_{1,2}(\mathbb{R})$, which are not central simple.

**Counterexample (the naive double centraliser).** For $\mathrm{Cl}_{0,3}(\mathbb{R})$ one has $\dim\mathrm{Cl}=8$ and $\dim\mathrm{End}_F(\mathrm{Cl})=64$, while the maps $L_aR_b$ span only $32$ dimensions. So the claim that the left and the right multiplications always generate $\mathrm{End}_F(\mathrm{Cl}(V,q))$ is false; the correct statement carries the central-simplicity hypothesis, and the two-sided family spans the same image, being a subfamily of the same maps.

## The One-Sided Operators Do Not Preserve the Quadratic Space

**Theorem.** The only left multiplications that carry the space of vectors into itself are the scalars:

$$
\{\,x : L_x(V)\subseteq V\,\}=F\cdot 1 .
$$

**Verified.** Solved as a linear system in $\mathrm{Cl}_{0,3}(\mathbb{R})$, in $\mathrm{Cl}_{0,4}(\mathbb{R})$ and in $\mathrm{Cl}_{1,3}(\mathbb{R})$, the space of such $x$ has dimension one.

**Example.** In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $e_j^{2}=-1$ the left multiplication $L_{e_1}$ sends the vector $e_1$ to the scalar $-1$ and the vector $e_2$ to the bivector $e_1e_2$, and the even left multiplication by $e_1e_2$ sends $e_1$ to $e_2$ but $e_3$ to the trivector $e_1e_2e_3$. So no non-scalar left multiplication preserves $V$.

**Remark.** This is the structural reason for the two-sided family. The signed inner conjugation $\alpha(x)\,y\,x^{-1}$ preserves $V$ for $x$ in the Clifford group $\Gamma(V,q)$, and it does so because the two factors are paired; the individual factors do not preserve $V$, and half of a geometric transformation is not a geometric transformation. The one-sided operators are nevertheless the right objects on the module: on the spinor module the Clifford algebra acts by left multiplication alone, and there the action is one-sided by construction, which is the theme of *The Adjoint of the One-Sided Action with Hermitian Adjoint* and of *Spinors as Minimal Left Ideals with Inner Conjugation*.

## Worked Cases

### An Odd Element

Let $x=e_1$ in $\mathrm{Cl}_{0,3}(\mathbb{R})$, with $e_j^{2}=-1$. Then $x$ is odd, $\alpha(x)=-x$, $x^{r}=x$ and $x^{\natural}=-x$, so

$$
L_{\alpha(e_1)}=L_{-e_1}=-L_{e_1}, \qquad R_{e_1^{r}}=R_{e_1}, \qquad R_{e_1^{\natural}}=-R_{e_1} .
$$

At the unit the values are $L_{e_1}(1)=e_1$, $L_{\alpha(e_1)}(1)=-e_1$ and $R_{e_1}(1)=R_{e_1^{r}}(1)=e_1$, $R_{e_1^{\natural}}(1)=-e_1$, so the graded and conjugation-twisted variants carry the parity sign that the plain members do not. On the vectors,

| operator | $e_1$ | $e_2$ | $e_3$ |
|---|---|---|---|
| $L_{e_1}$ | $-1$ | $e_1e_2$ | $e_1e_3$ |
| $R_{e_1}$ | $-1$ | $-e_1e_2$ | $-e_1e_3$ |

so each sends the first vector to a scalar and the other two to bivectors, and neither preserves $V$.

### An Even Element

Let $x=e_1e_2$ in $\mathrm{Cl}_{0,3}(\mathbb{R})$, an even element of square $-1$ and inverse $x^{-1}=-x$. Then $L_x(e_1)=e_2$ and $L_x(e_2)=-e_1$, so $L_x$ rotates the plane $\mathrm{span}(e_1,e_2)$ **by a quarter turn**, but $L_x(e_3)=e_1e_2e_3$ is a trivector, so $L_x(V)\nsubseteq V$; and $R_x(e_1)=-e_2$, $R_x(e_2)=e_1$, $R_x(e_3)=e_1e_2e_3$ likewise. The two-sided **inner conjugation** by the same element is the half-turn of the plane,

$$
x\,e_1\,x^{-1}=-e_1, \qquad x\,e_2\,x^{-1}=-e_2, \qquad x\,e_3\,x^{-1}=e_3 ,
$$

which preserves $V$ and is an isometry. The comparison isolates the point of the section: the one-sided $L_x$ and $R_x$ each carry a rotation of the plane and a defect on $e_3$, and their pairing cancels the defect, leaving the genuine rotation.

### The Anti-Multiplicativity of the Right Family

In $\mathrm{Cl}_{0,3}(\mathbb{R})$ with $x=e_1$ and $z=e_2$ the products at the unit are

$$
L_{e_1}L_{e_2}(1)=e_1e_2=L_{e_1e_2}(1), \qquad R_{e_1}R_{e_2}(1)=e_2e_1=-e_1e_2=-R_{e_1e_2}(1),
$$

so the left family composes in the order of the elements and the plain right family in the reverse order. The twisted family repairs the order: $R_{e_1^{r}}R_{e_2^{r}}(1)=x^{r}z^{r}=e_1e_2=R_{(e_1e_2)^{r}}(1)$, since reversion of the product reverses the factors.

### The Failure of Generation

In $\mathrm{Cl}_{0,3}(\mathbb{R})\cong\mathbb{H}\oplus\mathbb{H}$ the maps $L_aR_b$ span a space of dimension $32$, while $\mathrm{End}_F$ has dimension $64$; the two simple components of the algebra contribute their own endomorphism algebras and the mixed blocks are absent. In the central simple $\mathrm{Cl}_{0,4}(\mathbb{R})\cong\mathbb{H}(2)$ the span is all of the $256$-dimensional $\mathrm{End}_F$, and there the left and right multiplications are enough to see every operator.

## Summary

A **one-sided operator** on a Clifford algebra is a left multiplication $\Lambda^{\theta}_x(y)=\theta(x)\,y$, attached to an automorphism $\theta$, or a right multiplication $\mathrm P^{c}_x(y)=y\,c(x)$, attached to an anti-automorphism $c$. The two families **commute**, and the two-sided operator of *Two-Sided Operators on a Clifford Algebra* is their product, $\Phi^{\theta,c}_x=\Lambda^{\theta}_x\mathrm P^{c}_x$, so the composition law of the two-sided family is inherited from its factors. The left family and the twisted right family are **multiplicative in the same order**, because the reversal inside $c$ cancels the reversal of the order of composition; the **plain right multiplication is anti-multiplicative**, $R_{xz}=R_zR_x$, so $x\mapsto R_x$ is a representation of the opposite algebra. The members are separated by their value at the unit, $L_x(1)=R_x(1)=x$ and $L_{\alpha(x)}(1)=\alpha(x)$, $R_{x^{r}}(1)=x^{r}$, $R_{x^{\natural}}(1)=x^{\natural}$; a one-sided operator preserves the parity when its element is even and interchanges the two components when it is odd.

The graded and twisted members are the conjugates of the plain multiplications by the intrinsic anti-involutions, $L_{\alpha(x)}=\alpha L_x\alpha$, $R_{x^{r}}=rL_xr$, $R_{x^{\natural}}=\bar\cdot\,L_x\,\bar\cdot$ and $L_{x^{r}}=rR_xr$. The maps $a\mapsto L_a$ and $a\mapsto R_a$ are injective, their kernels are the annihilators $\ell(a)$ and $r(a)$, and their images are the right ideal $a\cdot\mathrm{Cl}$ and the left ideal $\mathrm{Cl}\cdot a$; the spinor module is the image of $R_\pi$ for a primitive idempotent $\pi$. The left and right multiplications are **mutual commutants**, $\{L_a\}'=\{R_b\}$ and $\{R_b\}'=\{L_a\}$, and together they generate the image of the enveloping algebra $\mathrm{Cl}\otimes\mathrm{Cl}^{\mathrm{op}}$, which is all of $\mathrm{End}_F(\mathrm{Cl})$ exactly when the Clifford algebra is **central simple** and is a proper subalgebra otherwise, of dimension half of $(\dim\mathrm{Cl})^2$ for $\mathrm{Cl}_{0,3}(\mathbb{R})$. Finally, the only left multiplications preserving the space of vectors are the scalars, so the geometry of $V$ requires the pairing of the two factors; the one-sided operators are the ones that act on the module, and their Hermitian adjoints belong to the Hermitian group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda^{\theta}_x(y)=\theta(x)y$ | Left one-sided operator, $\theta$ an automorphism |
| $\mathrm P^{c}_x(y)=y\,c(x)$ | Right one-sided operator, $c$ an anti-automorphism |
| $L_x=\Lambda^{\mathrm{id}}_x$, $L_{\alpha(x)}=\Lambda^{\alpha}_x$ | Plain and signed left multiplication |
| $R_x=\mathrm P^{\mathrm{id}}_x$, $R_{x^{r}}=\mathrm P^{r}_x$, $R_{x^{\natural}}=\mathrm P^{\bar\cdot}_x$ | Plain, reversion-twisted and conjugation-twisted right multiplication |
| $\Lambda^{\theta}_{xz}=\Lambda^{\theta}_x\Lambda^{\theta}_z$, $\mathrm P^{c}_{xz}=\mathrm P^{c}_x\mathrm P^{c}_z$ | Composition laws for the two families |
| $R_{xz}=R_zR_x$ | Plain right multiplication is anti-multiplicative |
| $\Phi^{\theta,c}_x=\Lambda^{\theta}_x\mathrm P^{c}_x$ | Two-sided operator as a product of one-sided ones |
| $L_{\alpha(x)}=\alpha L_x\alpha$, $R_{x^{r}}=rL_xr$, $R_{x^{\natural}}=\bar\cdot L_x\bar\cdot$ | The variants as conjugates by the anti-involutions |
| $\ell(a)$, $r(a)$ | Left and right annihilator, the kernels of $L_a$ and $R_a$ |
| $a\cdot\mathrm{Cl}$, $\mathrm{Cl}\cdot a$ | Right and left ideals, the images of $L_a$ and $R_a$ |
| $\{L_a\}'=\{R_b\}$, $\{R_b\}'=\{L_a\}$ | The mutual commutants |
| $\langle L_a,R_b\rangle=\mathrm{Im}\bigl(\mathrm{Cl}\otimes\mathrm{Cl}^{\mathrm{op}}\bigr)$ | The generated algebra; $=\mathrm{End}_F(\mathrm{Cl})$ iff central simple |
| $\{x:L_x(V)\subseteq V\}=F\cdot1$ | Only the scalars preserve the space of vectors |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the left and right multiplications and the regular representations of a Clifford algebra.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Clifford action, its structure and the ideals that carry the spinor modules.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (American Mathematical Society, 1956), for the double centraliser theorem, the mutual commutants of the regular representations and the enveloping algebra.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the left and right regular representations, the annihilators and the structure of a finite-dimensional algebra.
- Tsi-Yuen Lam, *A First Course in Noncommutative Rings*, Graduate Texts in Mathematics 131 (Springer, 2nd ed. 2001), for the central simple algebras and the isomorphism $A\otimes_FA^{\mathrm{op}}\cong\mathrm{End}_F(A)$.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the algebras with involution acting on themselves and the intrinsic anti-involutions of a Clifford algebra.

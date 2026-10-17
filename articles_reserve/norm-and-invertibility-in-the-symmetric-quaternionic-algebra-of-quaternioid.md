# __Norm and Invertibility in the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic product pairs two elements and returns a scalar: $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_t$. Read on the diagonal, the same object is the **quaternion form**, $\tilde p\star\tilde p=N(\tilde p)e_t$, and this article reads the block through the three notions that the diagonal controls: the **algebraic norm**, the **unit** and the **inverse**. The block answers the last two with an absence. The element $e_t$ multiplies by the scalar part alone, so the block has no unit, no one-sided unit and no inverse, and the group of units disappears with them. What the block does own is the form. The non-isotropic class, which over $\mathbb{R}$ is the whole punctured space, is exactly the group of units of the plain product, with the inverse of the plain product; the inverses belong to the parent, and the block reads them on its diagonal.

**Boundaries.** The product and its scalar law are *Introduction to the Symmetric Quaternionic Algebra of Quaternions*; the zero divisors are *Zero Divisors of the Symmetric Quaternionic Algebra*; the roots of a central value are *Square Roots of a General Element in the Symmetric Quaternionic Algebra*; the general definitions of a unit and of an inverse are *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*; the parent's norm and inverse criterion, which the block reads on its diagonal, are *Norm and Invertibility in the General Plain Algebra*.

**Conventions.** The algebra is $\mathbb{H}$ over $\mathbb{R}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ and $\vec e_x\vec e_y=\vec e_z$; an element is $\tilde q=q_te_t+\vec q$. The **quaternion conjugation** is $\tilde q^{\natural}=q_te_t-\vec q$; the bar is the identity, the star coincides with the natural sign ${}^{\natural}$. The **quaternion form** is $N(\tilde p,\tilde q)=p_0q_t+\vec p\cdot\vec q=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$, the **plain form** is $B(\tilde p,\tilde q)=p_0q_t-\vec p\cdot\vec q=\mathrm{Sc}(\tilde p\tilde q)$, and the **symmetric quaternionic product** is $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_t$. The centre is $\mathbb{R}e_t$ and the vector subspace is $\mathrm{Vect}(\mathbb{H})=\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$.

## The General Definitions

The vocabulary is fixed once in *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space*, and the block only answers it.

**Definition (unit).** An element $e$ is a **left unit** of a real-bilinear rule when $e x=x$ for every $x$, a **right unit** when $x e=x$ for every $x$, and a **two-sided unit** or **unit** when both.

**Definition (inverse and units).** When the rule has a two-sided unit $e$, the **inverse** of $x$ is the element $y$ with $xy=e=yx$, and $x$ is **invertible**, or a **unit**, when it has one. Without a two-sided unit the word inverse is not used, and the group of units is not defined.

**Definition (algebraic norm).** The **algebraic norm** of the block is the coefficient of its diagonal, the scalar $N(\tilde x)$ with $\tilde x\star\tilde x=N(\tilde x)e_t$; equivalently, it is the diagonal of the scalar-part form of the product.

The two definitions of the algebra are quoted, and the rest of the article is their reading on the block.

## The Algebraic Norm of the Block

**Proposition (the norm is the diagonal).** For every $\tilde x$ the square of the block is the central element

$$
\tilde x\star\tilde x=N(\tilde x)e_t,\qquad N(\tilde x)=x_0^{2}+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|^{2},
$$

so the algebraic norm of the block is the definite quaternion form $N$.

*Proof.* The product is $\tilde x\star\tilde x=N(\tilde x,\tilde x)e_t$ by the governing formula of *Introduction to the Symmetric Quaternionic Algebra of Quaternions*, and $N(\tilde x,\tilde x)=x_0^{2}+(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)=N(\tilde x)$.

**Theorem (the algebraic norm is the multiplicative form of the plain product).** The algebraic norm of the block is the quaternion norm of the algebra,

$$
\tilde q\tilde q^{\natural}=N(\tilde q)e_t,\qquad N(\tilde q)=\mathrm{Sc}\bigl(\tilde q\tilde q^{\natural}\bigr)=\mathrm{Sc}\bigl(\tilde q^{\natural}\tilde q\bigr),
$$

so it is the coefficient of the quaternion algebraic norm $N_Q$ of the general quaternionic product; it is multiplicative for the **plain** product, $N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$; and the product of the block is the polarisation read on the central line,

$$
\tilde p\star\tilde q=\tfrac12\bigl(N(\tilde p+\tilde q)-N(\tilde p)-N(\tilde q)\bigr)e_t .
$$

The form is positive definite, of Gram matrix $I_4$, of rank $4$, with radical $\{0\}$.

*Proof.* The identity $\tilde q\tilde q^{\natural}=N(\tilde q)e_t$, the multiplicativity and the inverse criterion are *Norm and Invertibility in the General Plain Algebra*, where the quaternion norm is owned, and the identification with the quaternion algebraic norm $N_Q$ is *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space*; the polarisation is the expansion of $\tilde p\star\tilde p=N(\tilde p)e_t$ at $\tilde p+\tilde q$ by bilinearity; and the Gram matrix and the definiteness are *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra*, where $N(e_\mu,e_\nu)=\delta_{\mu\nu}$ and $N(\tilde x)=x_0^{2}+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|^{2}$ is a sum of four squares vanishing only at the origin.

**Theorem (the norm is not multiplicative for the block).** For the product of the block the norm is the square of the coefficient,

$$
N(\tilde p\star\tilde q)=N(\tilde p,\tilde q)^{2},
$$

which differs in general from $N(\tilde p)N(\tilde q)$. At the witness $(\tilde p,\tilde q)=(\vec e_x,\vec e_y)$ the first is $0$, because $N(\vec e_x,\vec e_y)=0$, while the second is $1$.

*Proof.* $\tilde p\star\tilde q=N(\tilde p,\tilde q)e_t$, and the norm of a central element is the square of its coefficient, $N(ae_t)=a^{2}N(e_t)=a^{2}$; hence $N(\tilde p\star\tilde q)=N(\tilde p,\tilde q)^{2}$. At the basis pair, $\vec e_x\star \vec e_y=N(\vec e_x,\vec e_y)e_t=0$, so its norm is $0$, while $N(\vec e_x)=N(\vec e_y)=1$.

**Corollary (the block owns the form, not its multiplicativity).** The block carries the definite form whose vanishing decides its classes, and the multiplicativity of that form belongs to the plain product and not to the block. The two statements are not in conflict: the same quadratic form is multiplicative for one product and quadratic in the coefficient for the other, and the difference is exactly the collapse of the product onto the scalar line.

## The Absence of a Unit

**Theorem (there is no unit).** The block has no left unit, no right unit and no two-sided unit.

*Proof.* Let $\tilde u$ be a left unit, so that $\tilde u\star\tilde q=\tilde q$ for every $\tilde q$. At $\tilde q=e_t$ this reads $\tilde u\star e_t=N(\tilde u,e_t)e_t=u_te_t=e_t$, hence $u_t=1$. At $\tilde q=\vec e_x$ it reads $\tilde u\star \vec e_x=N(\tilde u,\vec e_x)e_t=u_xe_t=\vec e_x$, impossible because $u_xe_t$ is a multiple of $e_t$ and $\vec e_x$ is not. So there is no left unit. The same computation with the roles exchanged, using $\tilde q\star\tilde u=\tilde q$ and the commutativity of the block, excludes a right unit. A two-sided unit would be in particular a left unit, so there is none.

**Remark (the unit of the central line).** The element $e_t$ is a two-sided unit of the scalar line alone: for every real $\lambda$, $e_t\star(\lambda e_t)=\lambda e_t=(\lambda e_t)\star e_t$. It fails on every noncentral element, $e_t\star \vec e_x=N(e_t,\vec e_x)e_t=0\neq \vec e_x$, and this single evaluation is the whole failure: the block is the symmetric quaternionic structure, whose values are central, so its left multiplication by $e_t$ is the scalar-part projection and not the identity.

**Corollary (no inverse, no group of units).** Since the block has no two-sided unit, the inverse is not defined for it: no element is invertible, there is no group of units, and the block is not a division algebra, the definition requiring both a two-sided unit and the absence of zero divisors, neither of which the block has. Every statement about inverses in this block is a statement about the plain product, read below.

**Remark (the equation $\tilde A\star\tilde X=e_t$).** The equation $\tilde A\star\tilde X=e_t$ reads $N(\tilde A,\tilde X)=1$, a scalar equation in four unknowns. For $\tilde A\neq0$ it is **solvable**: the solution set is the affine hyperplane $\{\tilde X:N(\tilde A,\tilde X)=1\}$ of real dimension three, and $\tilde X=\tilde A/N(\tilde A)$ is one solution, because $N(\tilde A,\tilde A/N(\tilde A))=N(\tilde A)/N(\tilde A)=1$. For $\tilde A=0$ it has no solution, the left side being $0$. The solvability of this equation says only that $e_t$ lies in the image of the product, the image being the whole scalar line; it does not say that $\tilde X$ is an inverse, because no inverse is defined without a unit. The failure of invertibility is the absence of the unit, and not the unsolvability of the equation.

## The Non-Isotropic Class

**Definition.** The **non-isotropic class** of the block is the complement of the isotropic set,

$$
\{\tilde p:N(\tilde p)\neq0\}.
$$

**Theorem (the non-isotropic class is the punctured space and the group of units of the parent).** Over $\mathbb{R}$ the form is definite, so the non-isotropic class is the whole punctured space

$$
\{\tilde p:N(\tilde p)\neq0\}=\mathbb{H}\setminus\{0\},
$$

and it is exactly the group of units of the plain product, with the inverse of the plain product

$$
\tilde p^{-1}=\frac{\tilde p^{\natural}}{N(\tilde p)},\qquad
\tilde p\,\tilde p^{-1}=e_t=\tilde p^{-1}\tilde p .
$$

*Proof.* The form is positive definite, so $N(\tilde p)>0$ for every $\tilde p\neq0$, and $N(\tilde p)=0$ only at $\tilde p=0$; this gives the first display. The plain product is the quaternion multiplication, a division algebra, so every nonzero element is invertible with the displayed inverse, and $N(\tilde p^{-1})=1/N(\tilde p)$. The multiplicativity $N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$ makes the non-isotropic class closed under the plain product and stable under the plain inverse, so it is a group, the group of units of the parent.

**Remark (the block has no invertibility of its own).** The inverse written above is the inverse of the plain product; the block has no inverse. The role the group of units plays in a unital block is played here by the non-isotropic class, and the class is the unit group of the parent: the block owns the form whose vanishing defines the complement, and the group itself lives one level down, in the algebra from which the block is symmetrised. The passage from the plain product to its symmetric part therefore preserves the form and loses the multiplication, and with the multiplication it loses the unit and the inverses.

**Corollary (the isotropic class).** The complementary isotropic class is the origin alone,

$$
\{\tilde p:N(\tilde p)=0\}=\{0\},
$$

which is not a nilpotent, the nilpotents being the nonzero pure elements of *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*, and which is the sole square-zero element of the block.

## The Conjugation

**Proposition (the single conjugation).** Over $\mathbb{R}$ the three conjugations of the complex chapter collapse to one. The natural conjugation ${}^{\natural}$ is the only nontrivial one, the star coincides with it and the bar is the identity. The natural conjugation is an algebra automorphism of the plain product and preserves the form,

$$
N(\tilde p^{\natural})=N(\tilde p),\qquad N(\tilde p^{\natural},\tilde q^{\natural})=N(\tilde p,\tilde q),
$$

and it is an automorphism of the block as well, since the block's values are central,

$$
\tilde p^{\natural}\star\tilde q^{\natural}=N(\tilde p,\tilde q)e_t=\tilde p\star\tilde q .
$$

*Proof.* The collapse of the conjugations is the convention of the real chapter; the natural conjugation reverses the sign of the vector part, so it fixes $p_0$, fixes $|\vec p|^{2}$, and preserves the dot product; the last display is the governing formula applied to the conjugated arguments, whose coefficient is unchanged.

## Summary

The symmetric quaternionic block reads its algebraic norm on its diagonal: the norm is the quaternion form $N(\tilde x)=x_0^{2}+|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z|^{2}$, positive definite of Gram matrix $I_4$ and radical $\{0\}$, and it is the same form that the plain product carries as its multiplicative norm, $N(\tilde p\tilde q)=N(\tilde p)N(\tilde q)$. For the block the form is not multiplicative, $N(\tilde p\star\tilde q)=N(\tilde p,\tilde q)^{2}$, with the witness $(\vec e_x,\vec e_y)$ giving $0$ against $1$. The block has no unit, no one-sided unit, no inverse and no group of units; the element $e_t$ is a unit of the central line alone, and the equation $\tilde A\star\tilde X=e_t$ is solvable for $\tilde A\neq0$ without producing an inverse. The non-isotropic class is the whole punctured space, which is exactly the group of units of the plain product with the inverse $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$, and the isotropic class is the origin alone.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N(\tilde p,\tilde q)=p_0q_t+\vec p\cdot\vec q$ | the quaternion form, the coefficient of the product |
| $\tilde p\star\tilde p=N(\tilde p)e_t$ | the diagonal, the algebraic norm of the block |
| $N(\tilde p)=p_0^{2}+|\vec p|^{2}$ | the definite norm, Gram matrix $I_4$, radical $\{0\}$ |
| $N(\tilde p\star\tilde q)=N(\tilde p,\tilde q)^{2}$ | the norm of a block product; not multiplicative |
| unit, inverse | absent; $e_t$ is a unit of the central line alone |
| $\{\tilde p:N(\tilde p)\neq0\}=\mathbb{H}\setminus\{0\}$ | the non-isotropic class, the unit group of the plain product |
| $\tilde p^{-1}=\tilde p^{\natural}/N(\tilde p)$ | the inverse of the plain product |
| $\{\tilde p:N(\tilde p)=0\}=\{0\}$ | the isotropic class |

## Further Reading

- *Norm and Invertibility in the Quaternion Algebra* (`articles_maths/norm-and-invertibility-in-the-quaternion-algebra.md`), for the parent's norm $N(\tilde q)=\tilde q\tilde q^{\natural}$ and its inverse criterion, which the block reads on its diagonal
- *The 2 Algebraic Norms over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/the-2-algebraic-norms-over-the-quaternioid-r-space.md`), for the plain algebraic norm $N_P(\tilde p)=\tilde p^{2}$ and the quaternion algebraic norm $N_Q(\tilde p)=\tilde p^{\natural}\tilde p$, the block's diagonal being the coefficient of $N_Q$
- *The Quaternioid Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternioid-form-as-a-product-on-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the Gram matrix, the definiteness and the polarisation of the coefficient
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the maximal zero-divisor set that contrasts with the trivial isotropic class
- *Square Roots of a General Element in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra-of-quaternioid.md`), for the level sets of the diagonal
- *Definitions for the Study of the Algebraic Structures over the Quaternioid $\mathbb{R}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-quaternioid-r-space.md`), for the definitions of the unit, the inverse and the radical
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the unit, the inverse and the group of units of an algebra.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the norm form of the quaternions and its multiplicativity.

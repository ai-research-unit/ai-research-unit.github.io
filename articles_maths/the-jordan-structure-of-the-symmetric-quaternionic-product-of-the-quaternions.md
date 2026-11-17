# __The Jordan Structure of the Symmetric Quaternionic Product of the Quaternions__

## Introduction

The symmetrisation of the quaternionic product is
$$
\tilde q_1\bullet_{\natural}\tilde q_2=\tfrac12\bigl(\tilde q_1^{\natural}\tilde q_2+\tilde q_2^{\natural}\tilde q_1\bigr)=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t ,
$$
a commutative product with a one-dimensional image. It is as close to a scalar product as an algebra can be, and for that very reason it is as far from a Jordan algebra: it has no unit, its multiplication operators are rank one, and it fails the Jordan identity by a defect of one dimension. The failure is not an accident of the quaternions; it is the exact statement that the vector subspace multiplies into the scalar line.

The article is the real mirror of [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html): the symmetrisation, the closed form, the absent unit, the identity $L_{\tilde X}^2=X_0L_{\tilde X}$, the failure of the Jordan identity and its closed defect, the cone of squares, the Peirce theory, the operators, and the radical and the isotropic set, which are trivial here because the form is definite and are not trivial in the biquaternion block.

The parent is [The General Quaternionic Bilinear Product of the Quaternions](the-general-quaternionic-bilinear-product-of-the-quaternions.html); the product read as a form is the symmetrisation of the quaternionic form, whose matrix is $I_4$, cited and not restated.

## The Symmetrisation

**Definition.** The **symmetric quaternionic bilinear product** is
$$
\tilde q_1\bullet_{\natural}\tilde q_2=\tfrac12\bigl(\tilde q_1^{\natural}\tilde q_2+\tilde q_2^{\natural}\tilde q_1\bigr).
$$

**Theorem (the product is a scalar form).** For all $\tilde q_1,\tilde q_2$,
$$
\boxed{\;\tilde q_1\bullet_{\natural}\tilde q_2=\bigl(q_{1t}q_{2t}+(\vec q_1,\vec q_2)\bigr)e_t=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t\;}
$$

*Proof.* In the quaternionic product the scalar row $q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ is symmetric and the vector part $q_{1t}\vec q_2-q_{2t}\vec q_1-\vec q_1\times\vec q_2$ is antisymmetric; the half-sum keeps the scalar row and cancels the vector part. Verified exactly on the sixteen pairs of the basis and on general elements.

**Corollary (the elementary properties).** The product is commutative; its image is the centre $\mathbb{R}e_t$; it is central, in the sense that every value is a scalar multiple of $e_t$; and it has no unit.

*Proof.* Commutativity and the image are the display. For the unit, $\tilde u\bullet_{\natural}\tilde q=\langle\tilde u,\tilde q\rangle_{\natural}e_t$ equals $\tilde q$ for all $\tilde q$ only if every $\tilde q$ is central, which is false; at $\tilde q=\vec e_x$ the condition reads $\tilde u_xe_t=\vec e_x$. Both linear systems were solved: there is no identity on either side, and the least-squares residual is $1$, computed on the coefficient basis.

**Remark (the product is the form).** The trace form of the algebra is $\tau(\tilde q_1,\tilde q_2)=\mathrm{Sc}(\tilde q_1\bullet_{\natural}\tilde q_2)=\langle\tilde q_1,\tilde q_2\rangle_{\natural}$, which is the form that defines the product. The algebra is therefore self-dual in the strong sense: the product is recovered from the form by $\tilde q_1\bullet_{\natural}\tilde q_2=\tau(\tilde q_1,\tilde q_2)e_t$, and no information is lost in passing from one to the other. Every statement of this article is a statement about $N$ and about the line $\mathbb{R}e_t$.

## The Jordan Identity

**Theorem (the identity fails).** There are $\tilde q_1,\tilde q_2$ with
$$
\tilde q_1^2\bullet_{\natural}\bigl(\tilde q_2\bullet_{\natural}\tilde q_1\bigr)\neq\bigl(\tilde q_1^2\bullet_{\natural}\tilde q_2\bigr)\bullet_{\natural}\tilde q_1 .
$$

*Proof.* Take $\tilde q_1=\tilde q_2=\vec e_x$. Then $\tilde q_1^2=N(\vec e_x)e_t=e_t$, and the left side is $e_t\bullet_{\natural}(\vec e_x\bullet_{\natural}\vec e_x)=e_t\bullet_{\natural}e_t=e_t$, while the right side is $(e_t\bullet_{\natural}\vec e_x)\bullet_{\natural}\vec e_x=0\bullet_{\natural}\vec e_x=0$. Computed exactly.

**Proposition (the defect in closed form).** For all $\tilde q_1,\tilde q_2$,
$$
\boxed{\;D(\tilde q_1,\tilde q_2)=\tilde q_1^2\bullet_{\natural}\bigl(\tilde q_2\bullet_{\natural}\tilde q_1\bigr)-\bigl(\tilde q_1^2\bullet_{\natural}\tilde q_2\bigr)\bullet_{\natural}\tilde q_1=N(\tilde q_1)(\vec q_1,\vec q_2)e_t\;}
$$

*Proof.* Write $N=N(\tilde q_1)$. Then $\tilde q_1^2=Ne_t$, and the left side is $Ne_t\bullet_{\natural}\bigl(\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t\bigr)=N\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t$, using $\langle e_t,e_t\rangle_{\natural}=1$. The right side is $\bigl(NQ_{2t}e_t\bigr)\bullet_{\natural}\tilde q_1=NQ_{2t}Q_{1t}e_t$. The difference is $N\bigl(\langle\tilde q_1,\tilde q_2\rangle_{\natural}-Q_{1t}Q_{2t}\bigr)e_t=N(\vec q_1,\vec q_2)e_t$. Verified on general elements.

**Corollary (the defect is one-dimensional).** The image of $D$ is the scalar line, spanned by $e_t$, and the defect vanishes exactly on the pairs with $N(\tilde q_1)=0$ or $\vec q_2\perp\vec q_1$.

*Proof.* Every value is a multiple of $e_t$, and the value at $(\vec e_x,\vec e_x)$ is $e_t$. The vanishing set is the zero set of the product of the two factors, and both factors are computed in the display.

**Remark (the witnesses).** The defect at $(\vec e_x,\vec e_x)$ is $e_t$; at $(\vec e_x,\vec e_y)$ it is $0$, so orthogonal vector parts give no failure; at $(\vec e_x+\vec e_y,\vec e_x+\vec e_y)$ it is $4e_t$; at $(\vec e_x,\tfrac12(\vec e_x+\vec e_y))$ it is $\tfrac12e_t$. The values are the four of the biquaternion article, and the arithmetic is the same because the four witnesses have real coefficients.

**Remark (why the conjugation destroys what associativity gives).** The standard proof of the Jordan identity in a special Jordan algebra reassociates inside an associative algebra. Here there is no such algebra on the space: the product is the symmetrisation of the quaternionic product, which is not associative, and the conjugation in the first slot does not survive the reassociation. **The symmetric half of an associative product is a Jordan algebra; the symmetric half of a product twisted by an involution is not.** The scalar-valuedness is the visible form of the loss: a product whose values all lie on one line has no room to record the associativity of a three-factor word.

## The Cone of Squares

**Proposition (the square is the norm).** For every $\tilde q$,
$$
\tilde q\bullet_{\natural}\tilde q=N(\tilde q)e_t ,
$$
so the image of the diagonal is the ray $\mathbb{R}_{\geq0}e_t$ and the square carries no information but the modulus.

*Proof.* The diagonal of the closed form, or directly $\tilde q^{\natural}\tilde q=N(\tilde q)$. The norm is positive definite, so its values on the diagonal are non-negative.

**Remark (the cone of squares is a ray).** The cone generated by the squares is the closed ray $\mathbb{R}_{\geq0}e_t$, which is a cone with empty interior, not generating, and not a cone of a formally real algebra of degree two. The comparison with the other symmetrisation is exact: there the cone of squares is the whole space, and here it is a ray, so neither algebra carries an order and the two fail for opposite reasons, one by excess and one by default.

**Remark (the powers).** The powers agree up to the third, $\tilde q^2=N(\tilde q)e_t$ and $\tilde q^3=N(\tilde q)q_te_t$; at the fourth they do not: the bracketing $(\tilde q\bullet_{\natural}\tilde q)\bullet_{\natural}(\tilde q\bullet_{\natural}\tilde q)$ gives $N(\tilde q)^2e_t$ while the four others give $N(\tilde q)q_t^2e_t$, and the spread is $N(\tilde q)\lvert\vec q\rvert^2e_t$. The algebra is not power associative, and the first ambiguous power is the fourth. It is neither a Jordan algebra nor an associative algebra: it is a symmetric bilinear form carried on a line, and nothing more.

## The Peirce Theory

**Proposition (the idempotents).** The idempotents are $0$ and $e_t$.

*Proof.* $\tilde\Pi\bullet_{\natural}\tilde\Pi=N(\tilde\Pi)e_t=\tilde\Pi$ forces $\tilde\Pi=\lambda e_t$ with $\lambda^2=\lambda$. Verified by solving the quadratic conditions in the coefficient basis.

**Theorem (the Peirce spaces and the failed rule).** At $\tilde\Pi=e_t$ the multiplication operator has the eigenvalues $1,0,0,0$, with
$$
J_1(e_t)=\mathbb{R}e_t,\qquad J_0(e_t)=\mathbb{R}\vec e_x\oplus\mathbb{R}\vec e_y\oplus\mathbb{R}\vec e_z=\mathbb{R}^3 ,
$$
and the Peirce rules hold except the one that a Peirce space must be closed under its own product:
$$
J_1\bullet_{\natural}J_1\subset J_1,\qquad J_1\bullet_{\natural}J_0=0,\qquad J_0\bullet_{\natural}J_0\subset J_1 .
$$

*Proof.* $L(e_t)\tilde q=\langle e_t,\tilde q\rangle_{\natural}e_t=q_te_t$ is the projection onto the scalar line, whose spectrum is $1,0,0,0$. The three rules are the values of the form on the three pairs of spaces: $e_t$ with itself gives $e_t$, $e_t$ with a vector gives $0$, and two vectors give $\delta_{xy}e_t$. Verified on the basis.

**Remark (the failed rule is the failed identity).** The third inclusion violates the standard rule $J_0\bullet J_0\subset J_0$, and it is exactly the failure of the Jordan identity: an algebra whose Peirce spaces multiply as prescribed satisfies the identity, and the defect $N(\tilde q_1)(\vec q_1,\vec q_2)e_t$ is the deviation read on the pair $(J_0,J_0)$. The two facts are one fact, as they were in the biquaternion block, where the same defect is computed for the same reason.

**Remark (the calculus does not open).** With only two idempotents, the Peirce decomposition has two lines and no off-diagonal space, and there is no Peirce basis, no ladder of mixed units, and no spectral decomposition. The biquaternion block has a four-parameter family of rank-one idempotents and a full calculus; the real case has the trivial family, and it is the triviality that makes the algebra a form rather than a Jordan algebra.

## The Operators

**Definition.** $L(\tilde q_1)\tilde q_2=\tilde q_1\bullet_{\natural}\tilde q_2$ and $U(\tilde q_1)=2L(\tilde q_1)^2-L(\tilde q_1\bullet_{\natural}\tilde q_1)$.

**Theorem (the rank-one law).** For every $\tilde X$ and every $\tilde Y$,
$$
L_{\tilde X}\tilde Y=X_0\tilde Y_0e_t+X_0\bigl(\vec X,\vec Y\bigr)e_t ,\qquad
L_{\tilde X}^2=X_0L_{\tilde X},\qquad
L_{e_t}\tilde Y=Y_0e_t .
$$

*Proof.* $L_{\tilde X}\tilde Y=\langle\tilde X,\tilde Y\rangle_{\natural}e_t$, whose scalar coefficient is $X_0Y_0+(\vec X,\vec Y)$; hence $L_{\tilde X}^2\tilde Y=X_0\langle\tilde X,\tilde Y\rangle_{\natural}e_t=X_0L_{\tilde X}\tilde Y$. At $\tilde X=e_t$ the coefficient is $Y_0$. Verified in the coefficient basis, with a deviation of zero.

**Corollary (the minimal polynomial).** Every multiplication operator satisfies $L_{\tilde X}\bigl(L_{\tilde X}-X_0I\bigr)=0$, has rank one for $\tilde X\neq0$, and is nilpotent of order two when $X_0=0$.

*Proof.* The identity is the rank-one law rearranged. The image is contained in $\mathbb{R}e_t$ and is not zero for $\tilde X\neq0$, so the rank is one; and $L_{\tilde X}^2=X_0L_{\tilde X}=0$ when the scalar part vanishes.

**Proposition (the quadratic representation).** For all $\tilde X,\tilde Y$,
$$
U(\tilde X)\tilde Y=\bigl(2X_0\langle\tilde X,\tilde Y\rangle_{\natural}-N(\tilde X)Y_0\bigr)e_t .
$$

*Proof.* $2L_{\tilde X}^2\tilde Y=2X_0\langle\tilde X,\tilde Y\rangle_{\natural}e_t$ by the rank-one law, and $L_{\tilde X\bullet_{\natural}\tilde X}\tilde Y=L_{N(\tilde X)e_t}\tilde Y=N(\tilde X)Y_0e_t$. Verified on general elements.

**Remark (the unit seen through the operators).** At $\tilde X=e_t$ the quadratic representation is $U(e_t)\tilde Y=Y_0e_t=L_{e_t}\tilde Y$, which is the projection and not the identity. In a unital Jordan algebra $U(e_t)$ is the identity, and here it is the projection onto the scalar line: this is the operator form of the absent unit, and it is the reason the quadratic identity holds in the degenerate form $U(e_t)^2=U(e_t)$ rather than $U(e_t)=I$.

**Remark (the derivations).** The derivations of the algebra are the maps $\tilde q\mapsto2\,\vec w\times\vec q$ extended by zero on the real line, and they form a three-dimensional $\mathfrak{so}(3)$: the computation on the $16$ entries of $D$ gives a solution space of dimension three. Every derivation kills $e_t$, because $D(e_t)=D(e_t\bullet_{\natural}e_t)=2e_t\bullet_{\natural}De_t=2De_t$, and on the vector subspace it is anti-self-adjoint for the definite form. The algebra therefore has the same derivation algebra as the symmetric plain product, and it is the only structure the two symmetrisations share.

## The Radical and the Isotropic Set

**Proposition (the trace form is definite).** The trace form is $\tau=\langle\cdot,\cdot\rangle_{\natural}$, positive definite, of Gram matrix $I_4$; its radical is $\{0\}$ and its isotropic set is $\{0\}$.

*Proof.* The Gram matrix is read on the basis, where $\tau(e_t,e_t)=1$ and $\tau(\vec e_k,\vec e_k)=1$ with all mixed entries zero, and a positive definite form has no isotropic vector. The computation was made on the basis and on random elements.

**Remark (the contrast with the biquaternion block).** In the biquaternion block the same construction gives a form of inertia $(4,0)$ over $\mathbb{C}$, hence a form with a non-trivial isotropic cone over $\mathbb{C}$: the cone $t^2+\lvert\vec s\rvert^2=0$ has complex dimension three, and the algebra has a rich isotropic structure, with nilpotents, zero divisors and an isotropic plane. Over $\mathbb{R}$ the cone is the origin alone, the radical is zero for a trivial reason, and the isotropic structure of the quaternionic algebra is empty. **The definiteness is not a detail: it is the whole difference between a form and a form with a cone.**

**Remark (the radical is not the defect).** The radical of the trace form is zero and the Jordan defect is not: the two notions are independent, and the example shows it in the smallest possible way. A nondegenerate form does not make an algebra a Jordan algebra, and a Jordan algebra does not need a nondegenerate form: the other symmetrisation has a form of inertia $(1,3)$ and defect zero.

## The Place among the Two

| | $\bullet$ | $\bullet_{\natural}$ |
|---|---|---|
| image, dimension | $4$ | $1$ |
| unit | $e_t$ | none |
| commutative | yes | yes |
| Jordan identity | yes | no |
| defect | $0$ | $1$ |
| idempotents | $0,e_t$ | $0,e_t$ |
| spectrum of $L(e_t)$ | $1,1,1,1$ | $1,0,0,0$ |
| cone of squares | $\mathbb{H}$ | $\mathbb{R}_{\geq0}e_t$ |
| trace form | $(1,3)$, isotropic cone of dimension $3$ | $(4,0)$, isotropic set $\{0\}$ |
| radical | $0$ | $0$ |
| derivations | $\mathfrak{so}(3)$ | $\mathfrak{so}(3)$ |

**Remark (the two failures, which are opposite).** The column of $\bullet$ fails formal reality by excess: its cone of squares is the whole space, so no order survives. The column of $\bullet_{\natural}$ fails it by default: its cone of squares is a ray, so no order exists to begin with. Neither algebra supports the spectral theory, and the reasons are dual. What the two columns share is the idempotent class, the two derivations, and the absence of a Peirce calculus; what separates them is everything else.

## Summary

The symmetric quaternionic product is
$$
\tilde q_1\bullet_{\natural}\tilde q_2=\bigl(q_{1t}q_{2t}+(\vec q_1,\vec q_2)\bigr)e_t=\langle\tilde q_1,\tilde q_2\rangle_{\natural}e_t ,
$$
commutative, central, scalar valued, with a one-dimensional image and no unit on either side; $L_{e_t}$ is the projection $\tilde q\mapsto q_te_t$.

It fails the Jordan identity, with the one-dimensional defect $N(\tilde q_1)(\vec q_1,\vec q_2)e_t$, and the witnesses are $(\vec e_x,\vec e_x)$ giving $e_t$ and $(\vec e_x,\vec e_y)$ giving $0$. The defect is the deviation of the Peirce rule $J_0\bullet_{\natural}J_0\subset J_0$.

Its square is $N(\tilde q)e_t$, so the cone of squares is the ray $\mathbb{R}_{\geq0}e_t$; the idempotents are $0$ and $e_t$; the Peirce decomposition is two lines with no off-diagonal space; and the multiplication operators satisfy $L_{\tilde X}^2=X_0L_{\tilde X}$ with rank one.

The trace form is the quaternion form, positive definite, with radical $\{0\}$ and isotropic set $\{0\}$: the degenerate isotropic structure of the biquaternion block has no real analogue. The algebra is a symmetric bilinear form carried on a line, and its Jordan failure and its trivial isotropy are the two faces of the same definiteness.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra |
| $\tilde q=q_te_t+\vec q$ | the element, its scalar part and its vector part |
| $\tilde q_1\bullet_{\natural}\tilde q_2$ | the symmetric quaternionic product |
| $\langle\cdot,\cdot\rangle_{\natural}$ | its value, $q_{1t}q_{2t}+(\vec q_1,\vec q_2)$ |
| $N(\tilde q)$ | the quaternion norm |
| $L_{\tilde X}$, $U(\tilde X)$ | the multiplication operator and the quadratic representation |
| $J_\lambda(\tilde\Pi)$ | the Peirce space of the idempotent $\tilde\Pi$ |
| $D$ | the Jordan defect |

## Further Reading

- [The General Quaternionic Bilinear Product of the Quaternions](the-general-quaternionic-bilinear-product-of-the-quaternions.html), for the parent product.
- [The Jordan Structure of the Symmetric Plain Product of the Quaternions](the-jordan-structure-of-the-symmetric-plain-product-of-the-quaternions.html), for the other symmetrisation, which satisfies the identity.
- [The Jordan Structure of the Symmetric Quaternionic Product](the-jordan-structure-of-the-symmetric-quaternionic-product.html), for the biquaternion counterpart and its isotropic structure.
- [The Lie Structure of the Antisymmetric Quaternionic Product of the Quaternions](the-lie-structure-of-the-antisymmetric-quaternionic-product-of-the-quaternions.html), for the other half of the same parent.

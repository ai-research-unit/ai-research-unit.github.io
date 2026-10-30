# __$M_2(\mathbb{C})$ Model : The Sandwich__

## Introduction

The action of a biquaternion on the algebra is the sandwich

$$
\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$

In the matrix model it is the congruence $X\mapsto MXM^{\dagger}$. On the anti-Hermitian half the congruence is a Lorentz transformation; on the Hermitian half it is a congruence of a real quadratic form, and Sylvester's law of inertia governs it. The same formula does both, and the two readings differ only by the factor $i$ that exchanges the halves.

This article develops the sandwich in the matrix model. It is the matrix form of *The Polar Decomposition and Remarkable Subspaces*, §*The Action on the Two Halves* and §*Which Subspaces the Sandwich Preserves*, and the $2\times2$ counterpart of *$M_4(\mathbb{C})$ Model : The Sandwich*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The sandwich is $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$, and its matrix is $\Theta_M(X)=MXM^{\dagger}$. The two sectors are $\mathbb{M}_+$, the Hermitian matrices, and $\mathbb{M}_-$, the anti-Hermitian matrices. The quaternionic norm is $N=\det M$. The modulus is $r=|\det M|^{1/2}$.

**Boundaries.** The sandwich as an operator, its kernel and its image are *Operators of the Polar Word: The Common Framework*; the polar decomposition of the element is *The Polar Decomposition of a Biquaternion*; the action on the subspaces is *The Polar Decomposition and Remarkable Subspaces*; the matrix polar decomposition is *$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*.

## The Congruence

**Proposition.** For invertible $M$ and any $X$,

$$
\Theta_M(X)=MXM^{\dagger}
$$

is the image of the sandwich $\Theta_{\tilde Q}(\tilde X)$ under $\mathsf{M}_2$. It is complex linear in $X$ and invertible. It is not an algebra automorphism in general: the identity

$$
\Theta_M(XY)=\Theta_M(X)\,\Theta_M(Y)
$$

holds exactly when $M$ is $*$-unitary, because the two sides differ by the factor $M^{\dagger}M$.

*Proof.* The map is the composite of left multiplication by $M$, right multiplication by $M^{\dagger}$, and the identification of the two; it is the image of the algebra sandwich, which is a linear isomorphism because $\tilde Q$ is a unit. The matrix identities follow from the algebra identities.

**The two halves are preserved.** If $X^{\dagger}=X$ then

$$
(MXM^{\dagger})^{\dagger}=MX^{\dagger}M^{\dagger}=MXM^{\dagger},
$$

so the Hermitian half is preserved. If $X^{\dagger}=-X$ then the image is anti-Hermitian, so the anti-Hermitian half is preserved. The two statements are the matrix form of the fact that the sandwich preserves both sectors for every invertible element.

**The null cone is preserved.** Taking determinants,

$$
\det(MXM^{\dagger})=|\det M|^2\det X,
$$

so the zero set of the determinant is preserved. In the algebra, $N(\Theta_Q(X))=|N(Q)|^2N(X)$, and the zero divisors are mapped to zero divisors.

**The other four subspaces are not preserved in general.** The centre, the vector subspace, the quaternion subspace and the anti-quaternion subspace are preserved exactly when $Q$ is a central multiple of a real unit quaternion, by *The Polar Decomposition and Remarkable Subspaces*, §*Which Subspaces the Sandwich Preserves*. A general sandwich moves a traceless matrix to a matrix with nonzero trace, and a quaternion matrix to one that is not quaternion.

## The Anti-Hermitian Half as Four-Vectors

**The four-vector.** An anti-Hermitian matrix is written

$$
X=i(a\mathrm I_2+\vec b\cdot\sigma),
\qquad a\in\mathbb{R},\quad\vec b\in\mathbb{R}^3,
$$

where $\vec b\cdot\sigma=b_1\sigma_1+b_2\sigma_2+b_3\sigma_3$. Its determinant is

$$
\det X=-(a)^2+\lvert\vec b\rvert^2,
$$

the Lorentzian quadratic form of signature $(3,1)$. The three matrices $i\sigma_1,i\sigma_2,i\sigma_3$ and $i\mathrm I_2$ are a basis of the real space of anti-Hermitian matrices, and the determinant is the Minkowski form on that space.

**The unit-norm action.** Let $U$ be of unit norm, so $|\det U|=1$. Then

$$
\det(UXU^{\dagger})=\det X,
$$

and the map $X\mapsto UXU^{\dagger}$ is a linear isometry of the four-dimensional real space. It preserves the cone $\det X=0$. The group $SL_2(\mathbb{C})$ is connected, the map is continuous, and its kernel is $\{\pm\mathrm I_2\}$; both groups have real dimension six. The image is therefore the identity component of the Lorentz group:

$$
SL_2(\mathbb{C})\longrightarrow SO^{+}(1,3),\qquad U\longmapsto\Theta_U,
$$

a twofold cover.

**The two factors.** A unit-norm element factors as $U=U_{\mathrm b}U_{\mathrm r}$ with $U_{\mathrm b}$ Hermitian positive of determinant one and $U_{\mathrm r}\in SU(2)$. The sandwich factorises:

$$
\Theta_U=\Theta_{U_{\mathrm b}}\circ\Theta_{U_{\mathrm r}}.
$$

The rotor acts by rotating $\vec b$ and fixing $a$; the boost acts by a hyperbolic transformation mixing $a$ and the component of $\vec b$ along its axis, and fixing the orthogonal component. The two actions are the rotation and the boost of the Lorentz group, and their product is a general proper orthochronous transformation.

**The general element.** For $M=r\zeta U$ with $U$ of unit norm,

$$
\Theta_M=r^2\,\Theta_U,
$$

because the central scalars commute and $\zeta\bar\zeta=1$. The image is a conformal transformation: a Lorentz transformation composed with the dilation of ratio $r^2$. On the four-dimensional space of anti-Hermitian matrices the determinant of $\Theta_M$ is $r^8$, and the image of the unit group is the conformal group $CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3)$.

## The Hermitian Half as a Congruence

**The congruence.** For Hermitian $X$ and invertible $M$, the matrix $MXM^{\dagger}$ is Hermitian. It is a congruence of $X$ by $M$, not a similarity: the two factors are $M$ and $M^{\dagger}$, not $M$ and $M^{-1}$.

**Sylvester's law.** A congruence by an invertible matrix preserves the rank, the inertia and the signature of a Hermitian form. Hence $\Theta_M$ preserves the rank, the inertia and the causal type of $X$: a positive definite matrix stays positive definite, a matrix of signature $(1,3)$ stays of signature $(1,3)$, and a null matrix stays null. The statement is the matrix form of the fact that the sandwich preserves the two sectors and their cones.

**The determinant scaling.** From the congruence,

$$
\det(MXM^{\dagger})=|\det M|^2\det X=r^4\det X,
$$

because $|\det M|=r^2$. The determinant is not preserved; it is scaled by the fourth power of the modulus. The sign of the determinant is preserved, so the two cones of positive and negative determinant are each preserved. The factor $r^4$ is the reason the Hermitian half carries a conformal density rather than an invariant form.

**The Minkowski reading.** Writing $X=a\mathrm I_2+\vec b\cdot\sigma$ with $a,b$ real, the determinant is $a^2-\lvert\vec b\rvert^2$, of signature $(1,3)$. The congruence is a linear transformation of the four-dimensional space preserving the form up to the factor $r^4$; after rescaling by $r^{-1}$ it is a Lorentz transformation. The Hermitian and anti-Hermitian readings are the same Lorentz action composed with the multiplication by $i$.

**The positivity cone.** The positive semidefinite matrices form a cone inside the Hermitian half. The congruence preserves it, because $MXM^{\dagger}$ is positive semidefinite whenever $X$ is and $M$ is invertible. Its boundary is the null cone of the determinant, and the cone is the positivity cone of the Hermitian form.

## The Two Halves Are One Action

**The central $i$.** Multiplication by $i$ exchanges the two halves:

$$
i\mathbb{M}_+=\mathbb{M}_-,\qquad i\mathbb{M}_-=\mathbb{M}_+.
$$

It is an anti-isometry of the determinants:

$$
\det(iX)=-\det X,
$$

and it intertwines the two readings of $\Theta$:

$$
\Theta_M(iX)=i\,\Theta_M(X),
$$

because $i$ is central. The sandwich commutes with the exchange, and the two halves are the same action in the two real forms.

**The anti-isometry.** The map $X\mapsto iX$ from $\mathbb{M}_+$ to $\mathbb{M}_-$ reverses the sign of the determinant and preserves the null cone. It is therefore an anti-isometry, not an isometry: the two sectors are anti-isometric and not isomorphic. The statement is the matrix form of the relation between the informational and material forms.

**The common null cone.** The null cone of $\mathbb{M}_+$ and the null cone of $\mathbb{M}_-$ are exchanged by $i$, and their images under $\Theta_M$ are the same set. The sandwich preserves the common null cone, and the two readings of the action agree on it.

**The infinitesimal picture.** Differentiating the sandwich at the identity gives the Lie algebra action

$$
X\longmapsto [\mathcal R,X]+\{\mathcal H,X\},
$$

with $\mathcal R$ the rotor generator and $\mathcal H$ the boost generator. The commutator is the rotation and the anticommutator the boost; the two are the infinitesimal forms of the two factors of the sandwich. The statement is developed in *The Polar Decomposition and Remarkable Subspaces*, §*The Infinitesimal Split*.

**Faithfulness.** The infinitesimal action is faithful. If $[\mathcal R,X]+\{\mathcal H,X\}=0$ for every traceless $X$, evaluate at $X=\mathrm I_2$: the commutator vanishes and the anticommutator is $2\mathcal H$, so $\mathcal H=0$. Then $[\mathcal R,X]=0$ for every traceless $X$, and the centre of $\mathfrak{sl}_2(\mathbb{C})$ is zero, so $\mathcal R=0$. The kernel $\{\pm\mathrm I_2\}$ of the global action has collapsed to the origin, as it must for a local isomorphism.

## Which Subspaces the Sandwich Preserves

**The general rule.** Every sandwich preserves the two halves and the null cone. It preserves the other four remarkable subspaces exactly when the element is a central multiple of a real unit quaternion.

**The centre.** A central element $\lambda e_t$ is sent to $\lambda QQ^{*}$. This is central exactly when $QQ^{*}$ is central, which happens for the central multiples of the real unit quaternions and not in general. For a $*$-unitary $Q$, $QQ^{*}=e_t$ and the centre is fixed pointwise.

**The vector subspace.** A traceless matrix is sent to a matrix whose trace is $\operatorname{Tr}(MXM^{\dagger})$, which need not vanish. The vector subspace is preserved exactly when the sandwich is a similarity of the trace form, that is when $M$ is a central multiple of a real unit quaternion.

**The quaternion and anti-quaternion subspaces.** The condition $X=\epsilon\bar X\epsilon^{-1}$ is not preserved by a general congruence; it is preserved when $M$ commutes with the conjugate-linear structure, which is the same condition.

**The table.** The four non-sector subspaces are preserved by the sandwich of a central multiple of a real unit quaternion, and by no other element. The two sectors are preserved by every invertible element. The statement is the matrix form of the table of *The Polar Decomposition and Remarkable Subspaces*, §*Which Subspaces the Sandwich Preserves*.

## Summary

The sandwich $\Theta_Q(X)=QXQ^{*}$ is the matrix congruence $MXM^{\dagger}$. It preserves the Hermitian and anti-Hermitian halves and the null cone. On the anti-Hermitian half, a unit-norm element acts by a proper orthochronous Lorentz transformation, and the map $SL_2\to SO^{+}(1,3)$ is a twofold cover; a general element adds the dilation $r^2$, and the image is $CO^{+}(1,3)$. On the Hermitian half the congruence preserves rank, inertia and causal type by Sylvester's law, and scales the determinant by $r^4$. The central $i$ exchanges the two halves and reverses the determinant, so the two readings are anti-isometric. The other four subspaces are preserved exactly by central multiples of real unit quaternions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_Q(X)=QXQ^{*}$ | the sandwich |
| $\Theta_M(X)=MXM^{\dagger}$ | its matrix form |
| $r=|\det M|^{1/2}$ | the modulus, the dilation ratio |
| $SL_2\to SO^{+}(1,3)$ | the Lorentz action on the anti-Hermitian half |
| $CO^{+}(1,3)$ | the conformal image of the unit group |
| $r^4$ | the determinant scaling on the Hermitian half |

## Further Reading

- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the action on the subspaces
- [Operators of the Polar Word: The Common Framework](operators-of-the-polar-word-the-common-framework.html), for the sandwich as an operator
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html), for the factors
- [$M_2(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix](m2c-representation-the-polar-decomposition-of-a-matrix.html), for the matrix factors
- [$M_2(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions](m2c-model-the-six-subspaces-as-matrix-conditions.html), for the subspaces
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz group
- [Quadratic Forms and Polarisation](quadratic-forms-and-polarisation.html), for the congruence

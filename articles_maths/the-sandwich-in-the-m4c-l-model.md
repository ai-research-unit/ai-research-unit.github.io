# __$M_4(\mathbb{C})$ Model : The Sandwich__

## Introduction

The action of a biquaternion on the algebra is the sandwich
$$
\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}.
$$
In the regular model it is the congruence $X\mapsto MXM^{\dagger}$ on $4\times4$ matrices. On the anti-Hermitian half the congruence is a Lorentz transformation on a four-dimensional real subspace; on the Hermitian half it is a congruence of a real quadratic form, governed by Sylvester's law of inertia. The two readings differ by the central factor $i$ that exchanges the halves.

This article develops the sandwich in the regular model. It is the $4\times4$ counterpart of *$M_2(\mathbb{C})$ Model : The Sandwich*.

**Conventions.** The algebra and the model are those of *$M_4(\mathbb{C})$ Model : The Product, the Trace and the Determinant*. The sandwich is $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$, and its matrix is $\Theta_M(X)=MXM^{\dagger}$. The two sectors are $\mathbb{M}_+$, the Hermitian elements, and $\mathbb{M}_-$, the anti-Hermitian elements. The norm is $N=\langle\tilde Q\rangle_{\natural}$, and $\det M=N^2$. Write $r=\lvert N\rvert^{1/2}=\lvert\det M\rvert^{1/4}$.

**Boundaries.** The sandwich as an operator is *Operators of the Polar Word: The Common Framework*; the polar decomposition is *$M_4(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix*; the action on the subspaces is *The Polar Decomposition and Remarkable Subspaces*; the $2\times2$ version is *$M_2(\mathbb{C})$ Model : The Sandwich*. The sixteen basis matrices are *$M_4(\mathbb{C})$ Representation : The Two-Sided Operators on the Biquaternion Algebra*.

**Frame.** Unless a basis is named, matrices are written in the coefficient basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$. The canonical frame of *Conventions in Mathematics*, §*The Matrix Models*, is the Peirce frame reached by the change $S$ of *The Product, the Trace and the Determinant*: $S^{-1}\mathsf M_4^{L}(\tilde Q)S=I_2\otimes\mathsf M_2(\tilde Q)$.

## The Congruence

**Proposition.** For invertible $M$ and any $X$,
$$
\Theta_M(X)=MXM^{\dagger}
$$
is the image of the sandwich $\Theta_{\tilde Q}(\tilde X)$ under $\mathsf{M}_4^{L}$. It is complex linear in $X$ and invertible. It is not an algebra automorphism in general: the identity
$$
\Theta_M(XY)=\Theta_M(X)\,\Theta_M(Y)
$$
holds exactly when $M$ is a scalar multiple of a $*$-unitary matrix, because the two sides differ by the factor $M^{\dagger}M$.

*Proof.* The map is the composite of left multiplication by $M$, right multiplication by $M^{\dagger}$, and the identification of the two; it is the image of the algebra sandwich, which is a linear isomorphism because $\tilde Q$ is a unit. The matrix identities follow from the algebra identities. $\square$

**The two halves are preserved.** If $X^{\dagger}=X$, then
$$
(MXM^{\dagger})^{\dagger}=MX^{\dagger}M^{\dagger}=MXM^{\dagger},
$$
so the Hermitian half is preserved. If $X^{\dagger}=-X$, then the image is anti-Hermitian, so the anti-Hermitian half is preserved. The two statements are the matrix form of the fact that the sandwich preserves both sectors for every invertible element.

**The null cone is preserved.** Taking determinants,
$$
\det(MXM^{\dagger})=\lvert\det M\rvert^2\det X=\lvert N\rvert^4\det X,
$$
so the zero set of the determinant is preserved. In the algebra,
$$
N(\Theta_Q(X))=\lvert N(Q)\rvert^2N(X),
$$
and the zero divisors are mapped to zero divisors.

## The Anti-Hermitian Half as Four-Vectors

**The four-vector.** An anti-Hermitian element is written
$$
X=i a e_t+\vec b\cdot\vec e,
\qquad a\in\mathbb{R},\quad\vec b\in\mathbb{R}^3,
$$
with $\vec b\cdot\vec e=b_1\vec e_1+b_2\vec e_2+b_3\vec e_3$. Its norm is
$$
N(X)=-a^2+\lvert\vec b\rvert^2,
$$
the Lorentzian quadratic form of signature $(3,1)$. The four elements $i e_t,\vec e_1,\vec e_2,\vec e_3$ are a real basis of the anti-Hermitian subspace, and the norm is the Minkowski form on that space.

**The regular matrix reading.** In the regular model $X$ becomes a $4\times4$ anti-Hermitian matrix, and its determinant is
$$
\det X=N(X)^2=(-a^2+\lvert\vec b\rvert^2)^2,
$$
the square of the Minkowski form. The four-dimensional real subspace is the image of the anti-Hermitian elements; on it the congruence acts as a Lorentz transformation, while on the full sixteen-dimensional space it preserves the quartic determinant.

**The unit-norm action.** Let $\lvert N(Q)\rvert=1$, so $\lvert\det M\rvert=1$. Then
$$
\det(MXM^{\dagger})=\det X,
$$
and the map $X\mapsto MXM^{\dagger}$ is a linear isometry of the four-dimensional real subspace. It preserves the cone $N(X)=0$. The group $SL_2(\mathbb{C})$ is connected, the map is continuous, and its kernel is $\{\pm\mathrm I_4\}$; both groups have real dimension six. The image is the identity component of the Lorentz group:
$$
SL_2(\mathbb{C})\longrightarrow SO^{+}(1,3),\qquad Q\longmapsto\Theta_Q,
$$
a twofold cover.

**The two factors.** A unit-norm element factors as $Q=H_bU_r$ with $H_b$ Hermitian positive of norm one and $U_r$ a rotor. The sandwich factorises:
$$
\Theta_Q=\Theta_{H_b}\circ\Theta_{U_r}.
$$
The rotor acts by rotating $\vec b$ and fixing $a$; the boost acts by a hyperbolic transformation mixing $a$ and the component of $\vec b$ along its axis, and fixing the orthogonal component. The two actions are the rotation and the boost of the Lorentz group, and their product is a general proper orthochronous transformation.

**The general element.** For $M=r\zeta\mathsf{M}_4^{L}(U)$ with $\lvert N(U)\rvert=1$,
$$
\Theta_M=r^2\,\Theta_U,
$$
because the central scalars commute and $\zeta\bar\zeta=1$. The image is a conformal transformation: a Lorentz transformation composed with the dilation of ratio $r^2$ on the matrix, $r^4$ on the norm and $r^8$ on the $4\times4$ determinant. The image of the unit group is the conformal group $CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3)$.

## The Hermitian Half as a Congruence

**The congruence.** For Hermitian $X$ and invertible $M$, the matrix $MXM^{\dagger}$ is Hermitian. It is a congruence of $X$ by $M$, not a similarity: the two factors are $M$ and $M^{\dagger}$, not $M$ and $M^{-1}$.

**Sylvester's law.** A congruence by an invertible matrix preserves the rank, the inertia and the signature of a Hermitian form. Hence $\Theta_M$ preserves the rank, the inertia and the causal type of $X$: a positive definite matrix stays positive definite, a matrix of signature $(1,3)$ stays of signature $(1,3)$, and a null matrix stays null.

**The determinant scaling.** From the congruence,
$$
\det(MXM^{\dagger})=\lvert\det M\rvert^2\det X=\lvert N\rvert^4\det X=r^8\det X,
$$
because $\lvert\det M\rvert=\lvert N\rvert^2=r^4$. The determinant is not preserved; it is scaled by the eighth power of the modulus $r$. The sign of the determinant is preserved, so the two cones of positive and negative determinant are each preserved.

**The Minkowski reading.** On the four-dimensional Hermitian subspace, write $X=a e_t+i\vec b\cdot\vec e$ with $a,b$ real; the norm is
$$
N(X)=a^2-\lvert\vec b\rvert^2,
$$
of signature $(1,3)$. The congruence is a linear transformation of the four-dimensional space preserving the form up to the factor $r^4$; after rescaling by $r^{-2}$ it is a Lorentz transformation. The Hermitian and anti-Hermitian readings are the same Lorentz action composed with the multiplication by $i$.

**The positivity cone.** The positive semidefinite matrices form a cone inside the Hermitian half. The congruence preserves it, because $MXM^{\dagger}$ is positive semidefinite whenever $X$ is and $M$ is invertible. Its boundary is the null cone of the determinant, and the cone is the positivity cone of the Hermitian form.

## The Two Halves Are One Action

**Multiplication by $i$.** The central element $i$ commutes with every element, and multiplication by $i$ exchanges the Hermitian and anti-Hermitian halves:
$$
X\in\mathbb{M}_+\iff iX\in\mathbb{M}_-.
$$
The sandwich commutes with this exchange, because $i$ is central. The two halves are therefore one action read in two real forms, and the Lorentz transformation on the anti-Hermitian half is the same as the congruence on the Hermitian half composed with the exchange.

**The invariant form.** The determinant is the invariant of the congruence up to the conformal factor. On the four-dimensional subspaces it is the square of the Minkowski form; on the full sixteen-dimensional space it is the quartic invariant. The two readings have the same conformal group and the same causal structure.

**The kernel and the image.** The kernel of the action on the anti-Hermitian subspace is $\{\pm\mathrm I_4\}$, the same as in the $2\times2$ model. The image is the proper orthochronous Lorentz group for the unit-norm elements, and the conformal group for the general elements.

## Which Subspaces the Sandwich Preserves

**The general rule.** Every sandwich preserves the two halves and the null cone. It preserves the other four remarkable subspaces exactly when the element is a central multiple of a real unit quaternion.

**The centre.** A central element $\lambda e_t$ is sent to $\lambda QQ^{*}$. This is central exactly when $QQ^{*}$ is central, which happens for the central multiples of the real unit quaternions and not in general. For a $*$-unitary $Q$, $QQ^{*}=e_t$ and the centre is fixed pointwise.

**The vector subspace.** A traceless matrix is sent to a matrix whose trace is $\operatorname{Tr}(MXM^{\dagger})$, which need not vanish. The vector subspace is preserved exactly when the sandwich is a similarity of the trace form, that is when $M$ is a central multiple of a real unit quaternion.

**The quaternion and anti-quaternion subspaces.** The condition $X=\epsilon\bar X\epsilon^{-1}$ is not preserved by a general congruence; it is preserved when $M$ commutes with the conjugate-linear structure, which is the same condition.

**The table.** The four non-sector subspaces are preserved by the sandwich of a central multiple of a real unit quaternion, and by no other element. The two sectors are preserved by every invertible element. The statement is the matrix form of the table of *The Polar Decomposition and Remarkable Subspaces*, §*Which Subspaces the Sandwich Preserves*.

## Summary

The sandwich is the congruence $X\mapsto MXM^{\dagger}$ on the regular matrices. It preserves the Hermitian and anti-Hermitian halves and the null cone. On the four-dimensional anti-Hermitian subspace it is a Lorentz transformation; on the four-dimensional Hermitian subspace it is a congruence preserving inertia. The determinant scales by $\lvert\det M\rvert^2=\lvert N\rvert^4=r^8$, and the algebra norm scales by $r^4$. The unit-norm group acts as $SO^{+}(1,3)$ through a twofold cover, and the general unit group acts conformally.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Theta_M(X)=MXM^{\dagger}$ | the congruence |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and anti-Hermitian halves |
| $N(X)=-a^2+\lvert\vec b\rvert^2$ | the Minkowski form on the anti-Hermitian subspace |
| $\det(MXM^{\dagger})=\lvert N\rvert^4\det X$ | the determinant scaling |
| $r=\lvert N\rvert^{1/2}$ | the modulus |
| $SO^{+}(1,3)$ | the proper orthochronous Lorentz group |

## Further Reading

- [$M_4(\mathbb{C})$ Representation : The Polar Decomposition of a Matrix](m4c-representation-the-polar-decomposition-of-a-matrix.html), for the factors
- [$M_4(\mathbb{C})$ Model : The Six Subspaces as Matrix Conditions](m4c-model-the-six-subspaces-as-matrix-conditions.html), for the subspaces
- [$M_2(\mathbb{C})$ Model : The Sandwich](the-sandwich-in-the-m2c-model.html), for the $2\times2$ version
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), for the action on the subspaces
- [Operators of the Polar Word: The Common Framework](operators-of-the-polar-word-the-common-framework.html), for the operator

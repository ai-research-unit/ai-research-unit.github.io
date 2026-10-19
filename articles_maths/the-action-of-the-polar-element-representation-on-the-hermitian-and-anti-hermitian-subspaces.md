# __The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces__

## Introduction

The polar element representation writes an element off the null cone as a product of four factors. The present article asks what that element does to the algebra by the **sandwich**, and answers on the two real subspaces separately. The answer has a simple form. The sandwich preserves both subspaces. For an element off the null cone, on each subspace it is a positive scale times a proper orthochronous Lorentz transformation. The central phase is not a factor of the action. The boost and the rotor are the two factors of the Lorentz part. The two restrictions are intertwined by the central $i$, which is an anti-isometry.

The **sandwich** of an invertible $\tilde Q$ is $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$. It is $\mathbb{C}$-linear, and it preserves both subspaces, since $\tilde Q_1\in\mathbb{M}_\pm$ gives $(\tilde Q\tilde Q_1\tilde Q^{*})^{*}=\pm\tilde Q\tilde Q_1\tilde Q^{*}$. In the polar word it factorises as $\Theta_{\tilde Q}=r^2\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}}$. Stability here refers to the sandwich, not to multiplication: a nonzero central multiplier preserves each of $\mathbb{M}_\pm$ only when it is real, so multiplying by $\exp(i\alpha)$ does not preserve either subspace for $\alpha\neq0$. The sandwich by $\exp(i\alpha)$ is the identity, because $\exp(i\alpha)^{*}=\exp(-i\alpha)$ and the phase is central; that is why the phase lies in the kernel. These facts are used throughout.

The article treats the anti-Hermitian subspace $\mathbb{M}_-$ first, because it is the four-vector sector on which the Lorentz action is read directly. It then treats the Hermitian subspace $\mathbb{M}_+$, where the same action is a congruence on Hermitian matrices. It closes with the comparison of the two actions.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, $\vec e_x\vec e_y=\vec e_z$, and central imaginary $i$, $i^2=-1$. A generic element is $\tilde Q=Q_te_t+\vec Q$, with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and complex coefficients. The quaternion conjugation is $\tilde Q^{\natural}=Q_te_t-\vec Q$, the coefficientwise conjugation is $\overline{\tilde Q}=\overline{Q_t}e_t+\overline{\vec Q}$, and the Hermitian conjugation is $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$. The two subspaces are

$$
\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\},
$$

with $\mathbb{M}_+$ the Hermitian and $\mathbb{M}_-$ the anti-Hermitian one. The norm of the polar series is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^2$, and the domain of the polar word is $\langle\tilde Q\rangle_{\natural}\neq0$. The matrix model is $\mathsf M_2:\mathbb{B}\to\mathsf M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear, it satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

**The polar word** is

$$
\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

with $r>0$, $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, a Hermitian positive unit-norm boost $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$, and a unit real quaternion rotor $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$. The scale and the phase are central. The unitary factor of the Cartan pairing is $U=\exp(i\alpha)\tilde u_{\mathrm r}$, and its sandwich is $\Theta_U=\Theta_{\tilde u_{\mathrm r}}$, because the phase is central. The norm-one factor is $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$; it is not unitary unless the boost is trivial. The two norm-one factors are written with the glyph of the identity, $\tilde U_{\mathrm b}$ and $\tilde u_{\mathrm r}$, and never with the generic glyph $\tilde Q$. The **norm-one group** is $\mathbb{B}^{\times}_1=\{\tilde U:\langle\tilde U\rangle_{\natural}=1\}$, isomorphic to $SL(2,\mathbb{C})$. The **unitary group** is $\mathrm{U}(\mathbb{B})=\{\tilde U:\tilde U^{*}\tilde U=e_t\}$, isomorphic to $\mathrm{U}(2)$. The two groups are different: the boost is norm-one but not unitary, the phase is unitary but has norm $e^{2i\alpha}$, and only the rotor is both. This distinction is used throughout.

**The physical interpretation** is recorded where it clarifies the algebra, and is labelled as such. The mathematics does not depend on it.

## The Action on the Anti-Hermitian Subspace $\mathbb{M}_-$

### The Sector and Its Form

An element of $\mathbb{M}_-$ has an imaginary scalar part and a real vector part,

$$
\mathbb{M}_-\ni\tilde Q_-=i a\,e_t+\vec b,\qquad a\in\mathbb{R},\qquad \vec b=b_x\vec e_x+b_y\vec e_y+b_z\vec e_z,\quad b_k\in\mathbb{R}.
$$

Its norm is the Minkowski quadratic form

$$
\langle\tilde Q_-\rangle_{\natural}=-a^2+\lvert\vec b\rvert^2,
$$

of signature $(3,1)$: three positive space directions and one negative time direction. The polarisation is

$$
g_-(\tilde Q_-,\tilde Q_-')=-aa'+\vec b\cdot\vec b',
$$

and its matrix in the coordinates $(a,b_x,b_y,b_z)$ is $G_-=\operatorname{diag}(-1,1,1,1)$. The matrix image is anti-Hermitian,

$$
\mathsf M_2(\tilde Q_-)=i\bigl(aI_2-\vec b\cdot\boldsymbol\sigma\bigr),
$$

with eigenvalues $i(a\pm\lvert\vec b\rvert)$ and determinant $\langle\tilde Q_-\rangle_{\natural}$. The physical interpretation reads $a=ct$ and $\vec b=\vec x$; the four-vectors of relativistic physics are the elements of this sector. The mathematics below uses only the algebra.

### The Norm-One Action Is a Lorentz Transformation

Let $\tilde U\in\mathbb{B}^{\times}_1$ be norm-one. The matrix image $\mathsf M_2(\tilde U)$ has determinant $\langle\tilde U\rangle_{\natural}=1$, so it lies in $SL(2,\mathbb{C})$. For $\tilde Q_-\in\mathbb{M}_-$,

$$
\mathsf M_2\bigl(\Theta_{\tilde U}(\tilde Q_-)\bigr)=\mathsf M_2(\tilde U)\,\mathsf M_2(\tilde Q_-)\,\mathsf M_2(\tilde U)^{\dagger}.
$$

Taking determinants and using $\det\mathsf M_2(\tilde Q_-)=\langle\tilde Q_-\rangle_{\natural}$,

$$
\langle\Theta_{\tilde U}(\tilde Q_-)\rangle_{\natural}
=\lvert\det\mathsf M_2(\tilde U)\rvert^2\,\langle\tilde Q_-\rangle_{\natural}
=\langle\tilde Q_-\rangle_{\natural}.
$$

The action preserves the quadratic form. It is therefore a Lorentz transformation of $\mathbb{M}_-$. The map $\tilde U\mapsto\Theta_{\tilde U}$ is a continuous homomorphism from the connected group $SL(2,\mathbb{C})$ into $O(1,3)$, so its image lies in the identity component $SO^+(1,3)$: the transformation is proper and orthochronous. The kernel is $\{\pm e_t\}$, and both groups have real dimension six, so the image is the whole of $SO^+(1,3)$. This is the standard double cover of the Lorentz group, read in the algebra.

### The Boost

The boost is the Hermitian positive unit-norm element

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\tfrac{\psi}{2}\,e_t+i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b},
\qquad \psi\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1.
$$

It is Hermitian, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, and positive, with matrix eigenvalues $\exp(\pm\psi/2)$. Its square is the Hermitian element $\exp(i\psi\vec u_{\mathrm b})=\cosh\psi+i\sinh\psi\,\vec u_{\mathrm b}$, and the sandwich deposits the full rapidity $\psi$ although the exponent carries the half $\psi/2$.

Write the vector part of $\tilde Q_-$ as $\vec b=b_\parallel\vec u_{\mathrm b}+\vec b_\perp$, with $\vec b_\perp$ orthogonal to the axis. The parallel part commutes with $\tilde U_{\mathrm b}$; the transverse part anticommutes with the imaginary vector $i\vec u_{\mathrm b}$, so its cross terms cancel and it is fixed. A direct computation gives

$$
a'=a\cosh\psi-b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi-a\sinh\psi,\qquad
\vec b_\perp'=\vec b_\perp.
$$

In the coordinates $(a,b_x,b_y,b_z)$ the boost is the $4\times4$ matrix

$$
B_-(\psi,\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\psi & -\sinh\psi\,\vec u_{\mathrm b}^{\,T}\\
-\sinh\psi\,\vec u_{\mathrm b} & I_3+(\cosh\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix}.
$$

The off-diagonal signs are negative. The matrix satisfies $B_-^{T}G_-B_-=G_-$, with $G_-=\operatorname{diag}(-1,1,1,1)$, and $\det B_-=1$. It is the standard Lorentz boost in the passive convention, with the time coordinate $a$ and the spatial coordinates $\vec b$.

### The Rotor

The rotor is the unit real quaternion

$$
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r},
\qquad \theta\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1.
$$

It is unitary as well as norm-one, $\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{-1}$, so its sandwich is an algebra automorphism. On $\mathbb{M}_-$ it fixes the time direction $ie_t$ and rotates the vector part,

$$
\Theta_{\tilde u_{\mathrm r}}(i a+\vec b)=i a+R(\theta,\vec u_{\mathrm r})\,\vec b,
$$

where $R$ is the spatial rotation of angle $\theta$ about $\vec u_{\mathrm r}$, with the Rodrigues matrix

$$
R(\theta,\vec u_{\mathrm r})=I_3+\sin\theta\,[\vec u_{\mathrm r}]_\times+(1-\cos\theta)\,[\vec u_{\mathrm r}]_\times^2,
$$

and $[\vec u_{\mathrm r}]_\times$ the cross-product matrix. The element carries the half-angle $\theta/2$; the action rotates by the full angle $\theta$.

### The General Norm-One Element

A general norm-one element is the product of a boost and a rotor,

$$
\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}.
$$

The sandwich composes in the same order,

$$
\Theta_{\tilde U_{\mathrm L}}=\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}},
$$

so the rotation acts first and the boost second. The order is part of the polar data and is not interchangeable: the boost and the rotor do not commute. In the coordinates $(a,\vec b)$ the action is

$$
\Lambda_-(\psi,\theta)=B_-(\psi,\vec u_{\mathrm b})\operatorname{diag}(1,R(\theta,\vec u_{\mathrm r})),
$$

with $\operatorname{diag}(1,R)$ the block-diagonal matrix that fixes $a$ and applies $R$ to $\vec b$. The matrix $\Lambda_-$ lies in $SO^+(1,3)$.

### The Conformal Factor

For a general element $\tilde Q=\rho\tilde U_{\mathrm L}$ the action is

$$
\Theta_{\tilde Q}=r^2\,\Lambda_-,
$$

where $\Lambda_-$ is the Lorentz transformation above. The map is a **linear conformal transformation** of $\mathbb{M}_-$: it multiplies the quadratic form by $r^4$ and lengths by $r^2$. Its $4\times4$ determinant is $r^8$, since $\det\Lambda_-=1$. The image of the full group $\mathbb{B}^\times$ is therefore

$$
CO^+(1,3)=\mathbb{R}_{>0}\cdot SO^+(1,3),
$$

the linear conformal group, of real dimension seven. This is not the full conformal group of Minkowski space: the translations and the special conformal transformations are not sandwiches by an element.

### The Null Cone and the Celestial Sphere

The null cone is the zero set of the quadratic form,

$$
\mathcal N_-=\{\tilde Q_-\in\mathbb{M}_-:\langle\tilde Q_-\rangle_{\natural}=0\}
=\{\tilde Q_-=i a+\vec b:a^2=\lvert\vec b\rvert^2\}.
$$

It is preserved by the action, because the form is multiplied by the positive factor $r^4$. The future cone is the component $a=\lvert\vec b\rvert>0$.

The projective future cone is the celestial sphere. For a future-null element, write $a=\lvert\vec b\rvert$ and form the Hermitian matrix

$$
A=aI_2-\vec b\cdot\boldsymbol\sigma.
$$

Its eigenvalues are $0$ and $2a$, so it is positive semidefinite of rank one and has the form $A=\xi\xi^{\dagger}$ for a spinor $\xi\in\mathbb{C}^2$, defined up to a phase. Under the norm-one action,

$$
A\longmapsto \mathsf M_2(\tilde U)\,A\,\mathsf M_2(\tilde U)^{\dagger},
$$

so the spinor transforms linearly, $\xi\mapsto\mathsf M_2(\tilde U)\xi$. The ratio $z=\xi_1/\xi_0$ is a point of $\mathbb{C}P^1$, and the action on it is the Möbius action of $SL(2,\mathbb{C})$. In the lift through $\mathsf M_2(\tilde Q)$ the spinor is multiplied by $\rho=r\exp(i\alpha)$; the phase part is pure gauge, and the scale changes only the norm of $\xi$. Neither changes $z$. The celestial sphere therefore sees only the norm-one factor $\tilde U_{\mathrm L}$, through $PSL(2,\mathbb{C})\cong SO^+(1,3)$. This is the projective form of the statement that the phase is in the kernel and the scale is a dilation.

## The Action on the Hermitian Subspace $\mathbb{M}_+$

### The Sector and Its Form

An element of $\mathbb{M}_+$ has a real scalar part and an imaginary vector part,

$$
\mathbb{M}_+\ni\tilde Q_+=a\,e_t+i\vec b,\qquad a\in\mathbb{R},\qquad \vec b\in\mathbb{R}^3.
$$

Its norm is

$$
\langle\tilde Q_+\rangle_{\natural}=a^2-\lvert\vec b\rvert^2,
$$

of signature $(1,3)$: one positive scalar direction and three negative vector directions. The polarisation is

$$
g_+(\tilde Q_+,\tilde Q_+')=aa'-\vec b\cdot\vec b',
$$

with matrix $G_+=\operatorname{diag}(1,-1,-1,-1)=-G_-$. The matrix image is Hermitian,

$$
\mathsf M_2(\tilde Q_+)=aI_2+\vec b\cdot\boldsymbol\sigma,
$$

with trace $2a$, determinant $\langle\tilde Q_+\rangle_{\natural}$, and eigenvalues $a\pm\lvert\vec b\rvert$. The trace is twice the scalar coordinate, and the determinant is the norm. The physical interpretation reads $\tilde Q_+$ as a Hermitian observable and $a$ as its weight; the mathematics uses only the algebra.

### The Congruence

For an invertible $\tilde Q$ and $\tilde Q_+\in\mathbb{M}_+$,

$$
\mathsf M_2\bigl(\Theta_{\tilde Q}(\tilde Q_+)\bigr)
=\mathsf M_2(\tilde Q)\,\mathsf M_2(\tilde Q_+)\,\mathsf M_2(\tilde Q)^{\dagger}.
$$

The action is therefore a **congruence** of the Hermitian matrix by the invertible matrix $\mathsf M_2(\tilde Q)$. Sylvester's law of inertia applies: the numbers of positive, negative and zero eigenvalues are preserved. The rank is preserved, and the sign of the determinant is preserved. The determinant itself scales by

$$
\det\mathsf M_2\bigl(\Theta_{\tilde Q}(\tilde Q_+)\bigr)
=\lvert\det\mathsf M_2(\tilde Q)\rvert^2\det\mathsf M_2(\tilde Q_+)
=r^4\,\langle\tilde Q_+\rangle_{\natural},
$$

because $\lvert\det\mathsf M_2(\tilde Q)\rvert=\lvert\langle\tilde Q\rangle_{\natural}\rvert=r^2$. The null cone and the causal type are preserved. The action is an isometry of the bilinear form exactly when $r=1$; in that case its $4\times4$ matrix lies in $SO^+(1,3)$.

The congruence is by a positive matrix for the boost or the scale, and by a unitary matrix for the phase or the rotor. The two cases have different invariants; the boost and the rotor are treated in the next two subsections.

### The Boost

The boost $\tilde U_{\mathrm b}$ is Hermitian positive, so its matrix $S=\mathsf M_2(\tilde U_{\mathrm b})$ is Hermitian positive definite. Its action on $\mathbb{M}_+$ is the congruence

$$
\tilde Q_+\longmapsto S\,\tilde Q_+\,S.
$$

The same decomposition along and transverse to the axis as in $\mathbb{M}_-$ gives

$$
a'=a\cosh\psi+b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi+a\sinh\psi,\qquad
\vec b_\perp'=\vec b_\perp.
$$

The signs of the cross terms are positive, opposite to the anti-Hermitian sector. In the coordinates $(a,b_x,b_y,b_z)$ the boost is

$$
B_+(\psi,\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\psi & \sinh\psi\,\vec u_{\mathrm b}^{\,T}\\
\sinh\psi\,\vec u_{\mathrm b} & I_3+(\cosh\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

with $B_+^{T}G_+B_+=G_+$ and $\det B_+=1$. The two matrices are inverse to each other,

$$
B_-(\psi,\vec u_{\mathrm b})=B_+(\psi,\vec u_{\mathrm b})^{-1},
$$

in the coordinates carried by the two sectors. The element is the same; the inverse is a property of the coordinate identification, not a second boost.

The boost does not preserve the trace. Acting alone, it changes the trace to

$$
2\bigl(a\cosh\psi+b_\parallel\sinh\psi\bigr),
$$

which differs from $2a$ whenever $b_\parallel\neq0$. In the full word the rotor acts first and rotates the vector part, the boost then uses the rotated parallel component, and the scale multiplies the result by $r^2$. What the boost preserves is the inertia, hence the sign of the determinant and the causal type. In particular, on the timelike cone $a^2>\lvert\vec b\rvert^2$ it preserves the sign of $a$, so it preserves the time orientation. The trace is not an invariant of the action.

### The Rotor

The rotor is unitary, so its matrix $U_{\mathrm r}=\mathsf M_2(\tilde u_{\mathrm r})$ is unitary. Its action is the unitary conjugation

$$
\mathsf M_2(\tilde Q_+)\longmapsto U_{\mathrm r}\,\mathsf M_2(\tilde Q_+)\,U_{\mathrm r}^{\dagger}.
$$

Unitary conjugation preserves the trace and the eigenvalues, and therefore preserves the determinant and the inertia. On the coordinates it fixes $a$ and rotates the vector part,

$$
\Theta_{\tilde u_{\mathrm r}}(a+i\vec b)=a+i\,R(\theta,\vec u_{\mathrm r})\,\vec b,
$$

with the same rotation matrix $R$ as in $\mathbb{M}_-$. The rotor is the only factor that is both norm-one and unitary, and its action is the nontrivial automorphism of the algebra. It is the compact part of the Lorentz transformation.

### The General Norm-One Element

The general norm-one element $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ acts by

$$
\Lambda_+(\psi,\theta)=B_+(\psi,\vec u_{\mathrm b})\operatorname{diag}(1,R(\theta,\vec u_{\mathrm r})),
$$

and the general element by $\Theta_{\tilde Q}=r^2\Lambda_+$. $\Lambda_+$ lies in $SO^+(1,3)$; the matrix of the general action is $r^2\Lambda_+$, with determinant $r^8$. The rotation acts first and the boost second, as on $\mathbb{M}_-$.

### The Cone, the Rank, and the Causal Type

The null cone of $\mathbb{M}_+$ is

$$
\mathcal N_+=\{\tilde Q_+\in\mathbb{M}_+:a^2=\lvert\vec b\rvert^2\}.
$$

On the future part $a=\lvert\vec b\rvert>0$ the matrix $\mathsf M_2(\tilde Q_+)=aI_2+\vec b\cdot\boldsymbol\sigma$ is positive semidefinite of rank one. It is the same rank-one condition as on $\mathbb{M}_-$, read through the two matrix images $i(aI_2-\vec b\cdot\boldsymbol\sigma)$ and $aI_2+\vec b\cdot\boldsymbol\sigma$. The congruence preserves rank and positivity, so it preserves the cone and its positive part. The future rank-one cone is the set of pure states of the informational reading; the future light cone is the set of null four-vectors of the material reading. They are the same algebraic cone, seen through the two sectors.

The causal type is the sign pattern of the eigenvalues $a\pm\lvert\vec b\rvert$: both positive for $a>\lvert\vec b\rvert$, both negative for $a<-\lvert\vec b\rvert$, of opposite signs for $\lvert a\rvert<\lvert\vec b\rvert$, and one zero on the cone. The congruence preserves this pattern. The eigenvalues themselves are not simply scaled by the action; the invariant statement is the inertia, not the spectrum.

### What Is Invariant and What Is Not

Three statements must be kept apart. The **determinant** of the matrix image scales by $r^4$. The **inertia** is invariant under every invertible sandwich. The **trace** is invariant under the sandwich by the phase and by the rotor, multiplied by $r^2$ under the scale, and changed by the boost. In particular, the trace is not an invariant of the full action, and the eigenvalues of the transformed matrix are not simply the original eigenvalues multiplied by $r^2$; the boost changes them. The invariant object is the pair of the determinant scaling and the inertia; the polar factorisation separates the scaling from the Lorentz transformation that preserves the inertia.

## The Comparison of the Two Actions

### The Intertwining by $i$

The central $i$ commutes with every element, so for every $\tilde Q$ and every $\tilde Q_+\in\mathbb{M}_+$,

$$
\Theta_{\tilde Q}(i\tilde Q_+)=i\,\Theta_{\tilde Q}(\tilde Q_+).
$$

Since $i\mathbb{M}_+=\mathbb{M}_-$, multiplication by $i$ is a real-linear isomorphism of the two four-dimensional spaces that intertwines the two restrictions. The two representations are **equivalent**.

The equivalence is not an isometry. The norm is multiplicative and $i$ is central, so

$$
\langle i\tilde Q_+\rangle_{\natural}=i^2\langle\tilde Q_+\rangle_{\natural}
=-\langle\tilde Q_+\rangle_{\natural}.
$$

The intertwiner reverses the sign of the invariant quadratic form. In the coordinates $(a,\vec b)$ multiplication by $i$ sends $a+i\vec b$ to $ia-\vec b$, which is the spatial reflection

$$
D=\operatorname{diag}(1,-1,-1,-1).
$$

The two forms are opposite, $G_-=-G_+$. The coordinate identification $y_-=Dy_+$ pulls $G_-$ back to $D\,G_-\,D=-G_+$, which is the anti-isometry in coordinates.

### The Two Matrices

The intertwining gives the relation between the two $4\times4$ matrices. For the boost,

$$
B_-=D\,B_+\,D=B_+^{-1},
$$

and for the full norm-one action,

$$
\Lambda_-=D\,\Lambda_+\,D.
$$

The rotor matrix is the same $R$ in both sectors, the scale is the same $r^2$ in both, and the phase acts as the identity in both. The difference between the two actions is therefore entirely in the boost: in the coordinates carried by the sectors, the matrix of the same boost on $\mathbb{M}_+$ is the inverse of its matrix on $\mathbb{M}_-$. The opposite signs of the cross terms are the visible sign of this inverse relation.

The relation $B_-=B_+^{-1}$ is a statement about matrices in the two coordinate systems, not a statement that the physical boost is inverted. The coordinates $(a,\vec b)$ are read in the two sectors with different meanings: $a$ is the time coordinate on $\mathbb{M}_-$ and the scalar coordinate on $\mathbb{M}_+$. The element $\tilde U_{\mathrm b}$ is the same, and the Lorentz transformation it induces on each sector is the same up to the coordinate reflection $D$.

### The Common Cone and the Sign of the Form

The two null cones are the same set of coordinates,

$$
a^2=\lvert\vec b\rvert^2,
$$

because the two quadratic forms differ only by the sign. The two sectors share the cone and the time axis; they differ in the sign of the form at every point off the cone. On $\mathbb{M}_-$ the form is $-a^2+\lvert\vec b\rvert^2$; on $\mathbb{M}_+$ it is $a^2-\lvert\vec b\rvert^2$. A point that is timelike for the interval has $g_-<0$ and $g_+>0$; a point that is spacelike for the interval has $g_->0$ and $g_+<0$. The causal type is therefore the same in the two sectors, while the sign of the form is opposite. The intertwiner $i$ reverses the sign of the form but preserves the causal type. The common cone carries one projective celestial sphere, one spinor construction, and one Möbius action; the two sectors read it through their matrix images $i(aI_2-\vec b\cdot\boldsymbol\sigma)$ and $aI_2+\vec b\cdot\boldsymbol\sigma$.

### The Kernels, the Image, and the Equivalence

The kernel of the action on the algebra is the central circle $\mathrm{U}(1)$: if $\Theta_{\tilde Q}=\mathrm{id}$, then $\tilde Q\tilde Q^{*}=e_t$ by taking $\tilde Q_1=e_t$, so $\tilde Q$ is unitary; and $\tilde Q\tilde Q_1=\tilde Q_1\tilde Q$ for every $\tilde Q_1$, so $\tilde Q$ is central, $\tilde Q=\lambda e_t$, and $|\lambda|=1$. On the norm-one group the kernel is $\{\pm e_t\}$; on the unitary group it is the whole central circle. The image of the full group $\mathbb{B}^\times$ is $CO^+(1,3)$, the image of the norm-one group is $SO^+(1,3)$, and the image of the unitary group is $SO(3)$.

The two restrictions are equivalent as real representations, through $i$, but they are not isometric: the intertwiner reverses the invariant form. They are therefore the same representation with opposite quadratic structures. This is the precise sense in which $\mathbb{M}_-$ and $\mathbb{M}_+$ are two readings of one action. The polar word of a given element is unique. The action cannot distinguish $\tilde Q$ from $-\tilde Q$, whose words differ only by the sign of the rotor, nor any central phase from $e_t$; the kernel is the exact measure of the difference between the element and its action.

### The Polar Decomposition of the Action

The results assemble into one statement. For every $\tilde Q$ off the null cone, the sandwich on each of the two subspaces is

$$
\Theta_{\tilde Q}=r^2\,\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}},
$$

an inner automorphism by the rotor, a positive congruence by the boost, and a dilation by $r^2$, in that order. The phase is in the kernel. The boost is the non-compact, symmetric-space factor; the rotor is the compact, automorphism factor; the scale is the dilation; the phase is the gauge. On $\mathbb{M}_-$ the Lorentz factor is read as a proper orthochronous Lorentz transformation; on $\mathbb{M}_+$ it is read as the congruence on Hermitian matrices. The two readings are intertwined by $i$, which is an anti-isometry. This is the polar element representation acting on the two subspaces.

The differential at the identity separates the two kinds of factor. For a rotor direction $X=\tfrac12\vec u_{\mathrm r}$, real and pure, the one-parameter action is

$$
\Theta_{\exp(\epsilon X)}(\tilde Q_1)=\tilde Q_1+\epsilon\,[X,\tilde Q_1]+O(\epsilon^2),
$$

a commutator. For a boost direction $H=\tfrac{i}{2}\vec u_{\mathrm b}$, imaginary and pure, it is

$$
\Theta_{\exp(\epsilon H)}(\tilde Q_1)=\tilde Q_1+\epsilon\,\{H,\tilde Q_1\}+O(\epsilon^2),
$$

an anticommutator. The central phase direction $ie_t$ gives zero. The commutator and the anticommutator both preserve $\mathbb{M}_\pm$, and they are the two summands of the Cartan decomposition of $\mathfrak{sl}(2,\mathbb{C})=\mathfrak{su}(2)\oplus\mathfrak{p}$. The action therefore reproduces, at the infinitesimal level, the Cartan decomposition that the Cartan pairing records at the level of the element.

## Summary

The sandwich $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ preserves both subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$, with no unit-norm hypothesis. For $\tilde Q$ off the null cone it is, on each subspace, a positive scale $r^2$ times a proper orthochronous Lorentz transformation; for a norm-one $\tilde Q$ the scale is one. The polar word $\tilde Q=r\exp(i\alpha)\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ gives the factorization $\Theta_{\tilde Q}=r^2\Theta_{\tilde U_{\mathrm b}}\Theta_{\tilde u_{\mathrm r}}$: the phase acts trivially, the scale is a dilation by $r^2$, the boost is a positive congruence, and the rotor is an inner automorphism. On $\mathbb{M}_-$ the boost and rotor give the standard Lorentz action, with the formulas $a'=a\cosh\psi-b_\parallel\sinh\psi$ and $b_\parallel'=b_\parallel\cosh\psi-a\sinh\psi$; the null cone is preserved and its projective form is the celestial sphere with the Möbius action. On $\mathbb{M}_+$ the same factors give the congruence $a'=a\cosh\psi+b_\parallel\sinh\psi$, $b_\parallel'=b_\parallel\cosh\psi+a\sinh\psi$ on Hermitian matrices; the determinant scales by $r^4$, the inertia is preserved, and the trace is not an invariant under the boost. The two actions are intertwined by $i$, which is an anti-isometry: the two invariant forms are opposite, and the two $4\times4$ matrices satisfy $B_-=B_+^{-1}=DB_+D$. The kernel is $\mathrm{U}(1)$ on the full group $\mathbb{B}^\times$ and $\{\pm e_t\}$ on the norm-one group; the image is $CO^+(1,3)$. The two restrictions are equivalent but not isometric, and the polar word is the unique separation of the dilation, the boost and the rotation that the action performs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde Q_-=ia e_t+\vec b$ | the coordinates of an element of $\mathbb{M}_-$ |
| $\tilde Q_+=a e_t+i\vec b$ | the coordinates of an element of $\mathbb{M}_+$ |
| $\Theta_{\tilde Q}(\tilde Q_1)=\tilde Q\tilde Q_1\tilde Q^{*}$ | the sandwich, the action of $\tilde Q$ on the algebra |
| $r$, $\exp(i\alpha)$ | the positive scale and the central phase of the polar word |
| $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | the Hermitian positive unit-norm boost |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $\tilde U_{\mathrm L}=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the norm-one Lorentz element |
| $U=\exp(i\alpha)\tilde u_{\mathrm r}$ | the unitary factor of the Cartan pairing |
| $\rho=r\exp(i\alpha)$ | the complex modulus, $\tilde Q=\rho\tilde U_{\mathrm L}$ |
| $\mathbb{B}^{\times}_1$ | the norm-one group, isomorphic to $SL(2,\mathbb{C})$ |
| $\mathrm{U}(\mathbb{B})$ | the unitary group, isomorphic to $\mathrm{U}(2)$ |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | the biquaternion norm |
| $g_\pm$ | the polarisation of the norm on $\mathbb{M}_\pm$ |
| $G_+=\operatorname{diag}(1,-1,-1,-1)$, $G_-=-G_+$ | the matrices of the two forms |
| $B_\pm$ | the $4\times4$ boost matrices on the two sectors |
| $D=\operatorname{diag}(1,-1,-1,-1)=G_+$ | the coordinate reflection, $B_-=DB_+D=B_+^{-1}$ |
| $R(\theta,\vec u_{\mathrm r})$ | the spatial rotation matrix of the rotor |
| $\Lambda_\pm=B_\pm\operatorname{diag}(1,R)$ | the $4\times4$ matrices of the norm-one action |
| $CO^+(1,3)=\mathbb{R}_{>0}\cdot SO^+(1,3)$ | the linear conformal group, the image of the action |
| $\mathcal N_\pm$ | the null cones of the two sectors |

## Further Reading

- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the four factors, the modulus, the exponential trichotomy and the domain.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the Hermitian positive and unitary factors, the equation $\tilde Q\tilde Q^{*}=H^2$, and the Cartan decomposition of the exponents.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`) and *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_maths/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the two partial pairings of the four factors.
- *Hermitian and Skew-Hermitian Elements* (`articles_maths/hermitian-and-skew-hermitian-elements.md`), for the involutive split $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ and the two sectors.
- *The Unitary Group of the Biquaternion Algebra* (`articles_maths/the-unitary-group-of-the-biquaternion-algebra.md`), for $\mathrm{U}(\mathbb{B})\cong\mathrm{U}(2)$ and its relation to the norm-one group.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the double cover $SL(2,\mathbb{C})\to SO^+(1,3)$ and the physical boost and rotation.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector* (`articles_physics/the-anti-hermitian-subspace-m-as-the-material-sector.md`), for the four-vector reading, the interval and the light cone.
- *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector* (`articles_physics/the-hermitian-subspace-m-plus-as-the-informational-sector.md`), for the Hermitian observables, the trace and the positive cone.
- *The Polar Element Representation and Remarkable Subspaces* (`articles_maths/the-polar-element-representation-and-remarkable-subspaces.md`), for the four exponents read against the six remarkable subspaces.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* (2020), DOI 10.1007/s00006-020-1048-y, for the polar decomposition of a complexified quaternion.

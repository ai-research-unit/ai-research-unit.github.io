
# __Curves and Surfaces in the Biquaternion Moving Frame__

## Introduction

The local differential geometry of a curve or a surface in three-dimensional Euclidean space is the geometry of a **moving frame**: an orthonormal frame $(v_1,v_2,v_3)$ is attached to each point of the object, and the infinitesimal displacement of the frame along the object is the whole data. For a curve the two invariants, the curvature and the torsion, are the two coefficients of that displacement; for a surface the two invariants, the Gaussian and the mean curvature, are the determinant and the trace of the second fundamental form, which is the part of the displacement that leaves the tangent plane.

A frame is a point of the rotation group $SO(3)$, and the infinitesimal displacements of a frame form the Lie algebra $\mathfrak{so}(3)$, which is the space of 2-vectors of $\mathbb{R}^3$. The biquaternion algebra $\mathbb{B}$ carries both objects with no further structure: its real-quaternion part contains the double cover of $SO(3)$, and its grade-two part **is** $\mathfrak{so}(3)$ in three dimensions. A whole frame is therefore the single element $r$, its infinitesimal displacement along the object is the single $\mathbb{B}$-valued one-form $\mathrm d\iota=2r^{\dagger}\mathrm dr$, and the frame equations of Frenet for a curve and of Darboux for a surface are the three components of the single equation $\mathrm dv_k=r\,\mathrm D v_k\,r^{\dagger}$.

This article records that construction. It gives the algebra in the three grades the frame uses, the moving frame and its connection one-form, the Frenet frame and the two invariants of a curve, the frame of a surface with the two fundamental forms and the Gaussian and mean curvatures, the Darboux frame along a curve on a surface, the integrability conditions the frame must satisfy, and the three distinguished families of curves on a surface — the curvature lines, the asymptotic lines and the geodesics. Two worked examples are carried through, a circular helix and a sphere.

The article is the classical local theory, in three dimensions, in the biquaternion calculus. The **Riemannian theory** of curvature, of the Levi-Civita connection and of the geodesic equation on a manifold of any dimension is *Curvature and Geodesics* and *Riemannian Geometry*, and is assumed; nothing of it is re-derived. The **algebra** is *Biquaternion Algebra*, and the reading of the four components as four Clifford grades is *The Clifford Structure of the Biquaternion Algebra*; the exterior and interior products of multivectors are *The Geometric Product and the Grade Decomposition*, the associativity and graded commutativity of the wedge are *The Exterior Algebra*, and the rotors and the sandwich action are *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation* and *Biquaternion Rotations and Lorentz Transformations*. The **vector derivative** of the algebra, the identity $\nabla^2=\Delta$ and the classical integral theorems written as one theorem are *Geometric Calculus and the Vector Derivative*, and the corresponding statements are not repeated here. Nothing owned by those entries is re-derived.

## The Three Grades of the Algebra

### The Subspaces the Frame Uses

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, the central scalar imaginary $i$, and the quaternion units of square $-e_0$, $e_k^2=-e_0$, so that the Clifford generators are

$$
\gamma_k=ie_k,\qquad \gamma_k^2=+e_0,\qquad \gamma_j\gamma_k=-\gamma_k\gamma_j\quad(j\neq k),
$$

by *The Clifford Structure of the Biquaternion Algebra*. Write $\mathbb{G}_1=\mathrm{span}_{\mathbb{R}}\{\gamma_1,\gamma_2,\gamma_3\}$ for the **grade-one subspace** and $\mathbb{G}_2=\mathrm{span}_{\mathbb{R}}\{e_1,e_2,e_3\}$ for the **grade-two subspace**; the real scalars are $\mathbb{G}_0=\mathbb{R}e_0$ and the pseudoscalar line is $\mathbb{G}_3=\mathbb{R}i$.

| Grade | Subspace | Basis | Role here |
|---|---|---|---|
| $0$ | $\mathbb{G}_0=\mathbb{R}e_0$ | $e_0$ | scalar invariants |
| $1$ | $\mathbb{G}_1$ | $\gamma_1,\gamma_2,\gamma_3$, square $+e_0$ | points, frame vectors |
| $2$ | $\mathbb{G}_2$ | $e_1,e_2,e_3$, square $-e_0$ | the rotation algebra $\mathfrak{so}(3)$, the connection |
| $3$ | $\mathbb{G}_3=\mathbb{R}i$ | $i$ | the determinant invariant of a curve |

The **grade-one** objects are the Euclidean vectors: a point of the space is the element $x=x_1\gamma_1+x_2\gamma_2+x_3\gamma_3$, and the Euclidean scalar product and squared length are read from the algebra,

$$
x\cdot y=\tfrac12(xy+yx),\qquad |x|^2=x\cdot x=x^2 .
$$

which is positive definite on $\mathbb{G}_1$ and is the distance this geometry is built on.

### The Cross Product and the Exterior Product

**Definition.** For $a,b\in\mathbb{G}_1$ the **exterior product** and the **interior product** are

$$
a\wedge b=-\tfrac12\bigl(ab-ba\bigr),\qquad a\cdot b=\tfrac12\bigl(ab+ba\bigr),
$$

so that $ab=a\cdot b-a\wedge b$. The exterior product is the **cross product as a 2-vector**: with $[v]:=v_1e_1+v_2e_2+v_3e_3$ the grade-two element of coefficient vector $v$,

$$
a\wedge b=[a\times b],\qquad (a\wedge b)^2=-|a\times b|^2 ,
$$

whose second identity is the statement that a grade-two element of coefficient vector $v$ has square $-|v|^2$, so $[v]$ is invertible for $v\neq0$ with $[v]^{-1}=-[v]/|v|^2$.

**Proof.** Expand $ab=\sum_{j,k}a_jb_k\gamma_j\gamma_k$ in the basis of the generators, using $\gamma_j^2=e_0$ and $\gamma_j\gamma_k=-\gamma_k\gamma_j$: the diagonal terms collect to $a\cdot b$ and the off-diagonal ones to $-\sum_{j<k}(a_jb_k-a_kb_j)\gamma_j\gamma_k$, and $\gamma_1\gamma_2=-e_3$, $\gamma_2\gamma_3=-e_1$, $\gamma_3\gamma_1=-e_2$, so the off-diagonal sum is $-[a\times b]$. The square is $[v]^2=-(v_1^2+v_2^2+v_3^2)e_0$, since the quaternion units anticommute.

**Remark (the sign, and the clash with the outer product).** The sign in $a\wedge b=-\tfrac12(ab-ba)$ is the convention of the source of the construction and is kept throughout this article, because every formula below is transcribed in it. It is **the negative** of two other conventions of the corpus: the *outer product* of *Biquaternion Algebra*, $p\wedge q=\tfrac12(pq-qp)=V(p)\times V(q)$, and the Clifford outer product $u\wedge w=\langle uw\rangle_{k+l}$ of *The Geometric Product and the Grade Decomposition*. On pairs of grade-one elements the three differ by the sign $-1$, and the identity $a\wedge b=[a\times b]$ above is read in this article's sign; on pairs of grade-two elements the commutator $\tfrac12(\cdot-\cdot)$ is the cross product of the coefficient vectors in every one of them, and no sign is at stake. The glyph $\wedge$ therefore means *this article's* exterior product throughout, and a reader coming from *Biquaternion Algebra* must flip the sign of a wedge of two grade-one elements and of nothing else.

**The associativity.** The exterior product is associative and graded-commutative, $(a\wedge b)\wedge c=a\wedge(b\wedge c)$ and $A_p\wedge B_q=(-1)^{pq}B_q\wedge A_p$ on homogeneous elements, which is the exterior algebra of the grade-one subspace, read inside $\mathbb{B}$ and owned by *The Exterior Algebra*. Two cases are used below. First, a grade-one element with a grade-two element raises the grade by one and produces the pseudoscalar,

$$
a\wedge[v]=(a\cdot v)\,i ,
$$

the **scalar triple product**: for $v=b\times c$ it is $a\wedge b\wedge c=(a\cdot(b\times c))i$. Second, the wedge of two grade-two elements stays in grade two and is the cross product of the coefficient vectors, $\iota\wedge\iota'=V(\iota)\times V(\iota')$ for $\iota,\iota'\in\mathbb{G}_2$, because the commutator of two quaternion imaginaries is twice their cross product, which is the outer product identity of *Biquaternion Algebra*.

### The Frames of a Rotor

**Definition.** Let $\mathbb{H}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,e_1,e_2,e_3\}$ be the real quaternion subspace and let $r\in\mathbb{H}_{\mathbb{B}}$ have $r^{\dagger}r=e_0$, where $^{\dagger}$ is the Hermitian conjugation of the algebra, which on real quaternions is the quaternion conjugation. The **frame of $r$** is

$$
v_k=r\,\gamma_k\,r^{\dagger},\qquad k=1,2,3 .
$$

**Theorem.** The frame is an orthonormal frame of $\mathbb{G}_1$ with the same orientation as $\gamma_1,\gamma_2,\gamma_3$, every orthonormal direct frame of $\mathbb{G}_1$ is the frame of exactly two rotors $r$ and $-r$, and the frame depends only on the class of $r$ in $\mathbb{H}^\times_1/\{\pm e_0\}$, which is $SO(3)$.

**Proof.** The sandwich by a unit real quaternion preserves $\mathbb{G}_1$, its scalar products and its orientation, because it is the orthogonal map $\mathrm{Ad}^{\alpha}_r$ restricted to $\mathbb{G}_1$ and $\mathrm{Ad}^{\alpha}$ is an algebra automorphism fixing the scalars; the orthonormality of $v_1,v_2,v_3$ is then that of $\gamma_1,\gamma_2,\gamma_3$. The converse and the two-to-one cover are *Biquaternion Rotations and Lorentz Transformations*.

## The Moving Frame and Its Connection

### The Connection One-Form

**Definition.** Let the frame depend on one or two parameters and let $\mathrm d$ be the exterior derivative in those parameters. The **affine connection one-form** of the frame is the $\mathbb{G}_2$-valued one-form

$$
\mathrm d\iota:=2\,r^{\dagger}\,\mathrm dr ,
$$

and the **covariant differential** of the frame vector is the $\mathbb{G}_1$-valued one-form

$$
\mathrm D v_k:=\tfrac12\bigl(\mathrm d\iota\,\gamma_k-\gamma_k\,\mathrm d\iota\bigr).
$$

**Theorem (the frame equation).** $\mathrm dv_k=r\,(\mathrm D v_k)\,r^{\dagger}$, and the connection one-form is pure grade two, $\mathrm d\iota\in\mathbb{G}_2\otimes\Omega^1$, with no scalar or pseudoscalar part.

**Proof.** Differentiate $v_k=r\gamma_kr^{\dagger}$ and use $\mathrm dr^{\dagger}=-r^{\dagger}\,\mathrm dr\,r^{\dagger}$, which is the differential of $r^{\dagger}r=e_0$. This gives $\mathrm dv_k=\tfrac12r(\mathrm d\iota\,\gamma_k-\gamma_k\,\mathrm d\iota)r^{\dagger}$, the displayed equation. For the purity, $\mathrm d\iota=2r^{\dagger}\mathrm dr$ and $r$ a real quaternion, so that $r^{\dagger}\mathrm dr$ is a product of two elements of the real quaternion subspace, which is the even part $\mathbb{H}_{\mathbb{B}}=\mathbb{G}_0\oplus\mathbb{G}_2$ of the grade decomposition; the scalar part of $r^{\dagger}\mathrm dr$ vanishes because $r^{\dagger}\mathrm dr=-\mathrm dr^{\dagger}r$, which is the differential of $r^{\dagger}r=e_0$. So $\mathrm d\iota\in\mathbb{G}_2\otimes\Omega^1$, as claimed.

**Definition.** Write the connection in the basis of $\mathbb{G}_2$ and its components in the basis of the parameters,

$$
\mathrm d\iota=\iota_1e_1+\iota_2e_2+\iota_3e_3 ,
$$

where each $\iota_j$ is a real one-form.

**Theorem (the components of the covariant differential).**

$$
\mathrm D v_1=\iota_3\,\gamma_2-\iota_2\,\gamma_3,\qquad
\mathrm D v_2=\iota_1\,\gamma_3-\iota_3\,\gamma_1,\qquad
\mathrm D v_3=\iota_2\,\gamma_1-\iota_1\,\gamma_2 .
$$

**Proof.** Expand $\tfrac12(\mathrm d\iota\gamma_k-\gamma_k\mathrm d\iota)$ with $\mathrm d\iota=\sum_j\iota_je_j$ and the multiplication rules $e_j\gamma_k=i\,e_je_k$ of the basis; the coefficient of $\gamma_m$ in $\mathrm D v_k$ is $\varepsilon_{jkm}\iota_j$, which is the displayed triple by the antisymmetry of $\varepsilon$.

### The Interpretation

The three components have a name and a meaning. $\iota_1$ is the rate at which the frame turns about $v_1$ — the component that couples $v_2$ and $v_3$ — $\iota_2$ is the rate at which it turns about $v_2$ and $\iota_3$ the rate about $v_3$; the passage above shows that turning about $v_k$ moves the other two vectors into one another. Equivalently, $\mathrm d\iota=\iota_1e_1+\iota_2e_2+\iota_3e_3$ is the angular velocity one-form of the frame, and if the parameters are the time, then $\iota_j/\mathrm dt$ are the components of the angular velocity vector in the frame.

The frame determines the rotor only up to the sign, since $r$ and $-r$ give the same frame, and no other freedom is present: a frame is the same thing as a point of $SO(3)$. On a surface a coarser freedom is at work, because the requirement is only that the third vector be the normal and the first two span the tangent plane: if $r$ is a frame of the surface then so is $r\exp(\tfrac12\Phi e_3)$ for any real function $\Phi(u,v)$, since the generator $e_3$ of that rotor leaves $v_3$ fixed and rotates $v_1$ and $v_2$ into one another by the angle $\Phi$. The normal, the first fundamental form and the two curvatures are unchanged, while the connection and the decomposition of the second fundamental form are not, and this is the freedom by which the second fundamental form is diagonalised in the section on the curvature lines.

## Curves: The Frenet Frame

### The Frame of a Curve

Let the curve be $x(t)$, a smooth $\mathbb{G}_1$-valued function of a parameter $t$, and let $s$ be the arc length, $\mathrm ds=|\mathrm dx|$. The displacement of the point is a grade-one element, and read in the frame it has three components,

$$
\mathrm dx=\omega_1v_1+\omega_2v_2+\omega_3v_3 .
$$

**Definition.** The **Frenet frame** of the curve is the frame with

$$
\mathrm dx=\mathrm ds\,v_1 ,\qquad \iota_2=0 ,
$$

that is, the first frame vector is the unit tangent and the connection has no component coupling $v_1$ and $v_3$.

**Theorem.** The Frenet frame exists at every point at which the curvature does not vanish, is unique, and its vectors are the tangent, the principal normal and the binormal,

$$
v_1=\frac{\mathrm dx}{\mathrm ds},\qquad
v_2=\frac{1}{\rho}\frac{\mathrm Dv_1}{\mathrm ds},\qquad
v_3=v_1\times v_2 ,
$$

where $\rho$ is the curvature below.

**Proof.** The condition $\mathrm dx=\mathrm ds\,v_1$ fixes $v_1$; the condition $\iota_2=0$ makes $\mathrm Dv_1=\iota_3\gamma_2$ purely along $v_2$ by the components above, so $v_2$ is the direction of $\mathrm Dv_1$ and $v_3$ completes the direct frame. The existence of $v_2$ needs $\mathrm Dv_1\neq0$, that is a non-vanishing curvature; the uniqueness is that of the direct frame determined by its first two vectors.

### The Frenet Equations

**Theorem (Frenet).** With $\iota_1=\tau\,\mathrm ds$ and $\iota_3=\rho\,\mathrm ds$, the connection of the Frenet frame is

$$
\mathrm d\iota_F=\tau\,\mathrm ds\,e_1+\rho\,\mathrm ds\,e_3 ,
$$

and the frame equations are

$$
\mathrm Dv_1=\rho\,\mathrm ds\,v_2,\qquad
\mathrm Dv_2=-\rho\,\mathrm ds\,v_1+\tau\,\mathrm ds\,v_3,\qquad
\mathrm Dv_3=-\tau\,\mathrm ds\,v_2 ,
$$

so that $\rho$ and $\tau$ are the **curvature** and the **torsion** of the curve.

**Proof.** Put $\iota_2=0$ in the components of the covariant differential: $\mathrm Dv_1=\iota_3\gamma_2$, $\mathrm Dv_2=\iota_1\gamma_3-\iota_3\gamma_1$, $\mathrm Dv_3=-\iota_1\gamma_2$. Along the curve the only parameter is $s$, so each component is a real multiple of $\mathrm ds$, and the coefficients of those multiples are *defined* to be $\rho$ and $\tau$.

**Corollary (the two degenerate cases).** If $\rho=0$ on an interval the curve is the straight line through the point in the direction $v_1$, and $\mathrm d\iota_F=0$ there. If $\tau=0$ on an interval the curve lies in the plane spanned by $v_1$ and $v_2$, the **osculating plane**, and $\mathrm d\iota_F$ has no component along $e_1$.

**Proof.** $\rho=0$ makes $\mathrm Dv_1=0$, so the tangent is constant along the interval, which is a line. $\tau=0$ makes $\mathrm Dv_3=0$, so the binormal is constant, and the curve, whose tangent is always orthogonal to a fixed vector, lies in a fixed plane.

### The Invariants from the Derivatives

**Theorem.** Let $\dot x,\ddot x,\dddot x$ be the first three derivatives of the curve with respect to any parameter, and let $|\alpha|$ denote the Euclidean modulus of a grade-two element, $|\alpha|^2=-\alpha^2$. Then

$$
\rho=\frac{|\dot x\wedge\ddot x|}{|\dot x|^3},\qquad
\tau=i\,\frac{\langle\dot x\,\ddot x\,\dddot x\rangle_3}{\bigl(\dot x\wedge\ddot x\bigr)^2},
$$

equivalently, with $\alpha=\dot x\wedge\ddot x\in\mathbb{G}_2$, $\beta=\dot x\wedge\ddot x\wedge\dddot x=\Delta_\beta\,i\in\mathbb{G}_3$ and $\Delta_\beta=\dot x\cdot(\ddot x\times\dddot x)$ the determinant,

$$
\rho=\frac{|\alpha|}{|\dot x|^3},\qquad
\tau=\frac{\Delta_\beta}{|\dot x\times\ddot x|^2},
$$

so that the pair $(\rho,\tau)$ is the complete set of invariants of the curve under the direct isometries, and the parameters $s,\rho,\tau$ determine the curve up to a direct isometry.

**Proof.** With the prime denoting $\mathrm d/\mathrm ds$, the frame gives $\alpha=x'\wedge x''=\rho\,(v_1\wedge v_2)$ and $\beta=\rho^2\tau\,i$: the first from $x''=\rho v_2$ and the second from the third derivative computed from the Frenet equations. Squaring the first, $(v_1\wedge v_2)^2=-|v_1\times v_2|^2=-1$ because $v_1,v_2$ are orthonormal, so $\alpha^2=-\rho^2$ and $|\alpha|=\rho$. For the torsion, $\beta=\Delta_\beta\,i$ with $\Delta_\beta$ the determinant, so $i\beta=i\Delta_\beta\,i=-\Delta_\beta$ and $\tau=i\beta/\alpha^2=\Delta_\beta/|\alpha|^2$ after the substitution $\alpha^2=-|\alpha|^2$. The two display formulas in a general parameter $t$ follow by the chain rule, the powers of $\mathrm ds/\mathrm dt$ cancelling in $\tau$ because the trivector carries the sixth and the square of the 2-vector the fourth and the second. The determination of the curve by $s,\rho,\tau$ is the classical theorem of the local theory, proved by the existence and uniqueness of a solution of the Frenet system; that system is a system of ordinary differential equations and belongs to *Ordinary Differential Equations*.

### Example: The Circular Helix

**Example.** Let $x(t)=2\cos t\,\gamma_1+2\sin t\,\gamma_2+t\,\gamma_3$. Then $|\dot x|^2=5$, and

$$
\dot x\wedge\ddot x=2\sin t\,e_1-2\cos t\,e_2+4e_3,\qquad
(\dot x\wedge\ddot x)^2=-20,\qquad
\dot x\wedge\ddot x\wedge\dddot x=4i ,
$$

so that $\rho=2/5$ and $\tau=1/5$. The Frenet frame is

$$
v_1=\frac{1}{\sqrt5}\bigl(-2\sin t\,\gamma_1+2\cos t\,\gamma_2+\gamma_3\bigr),\qquad
v_2=-\cos t\,\gamma_1-\sin t\,\gamma_2,\qquad
v_3=v_1\times v_2 ,
$$

and the osculating plane at the point of parameter $t$ is the plane of the points $X$ with

$$
(X-x)\wedge\frac{\mathrm dx}{\mathrm ds}\wedge\frac{\mathrm d^2x}{\mathrm ds^2}=0 ,
$$

the binormal being $v_3=(\sin t\,\gamma_1-\cos t\,\gamma_2+2\gamma_3)/\sqrt5$ and the equation of the plane, $X\cdot v_3=x\cdot v_3$, being $2t-2X_3+X_2\cos t-X_1\sin t=0$. The two invariants are constant, as they must be for a curve that is a screw motion of a point, and they agree with the classical values $\rho=a/(a^2+b^2)$ and $\tau=b/(a^2+b^2)$ of a helix of radius $a=2$ and rise $2\pi b$ with $b=1$.

**Proof.** The three displayed identities are the direct computation from $\dot x=(-2\sin t,2\cos t,1)$, $\ddot x=(-2\cos t,-2\sin t,0)$, $\dddot x=(2\sin t,-2\cos t,0)$ with the cross product and the definitions of the exterior product; the square is $(\dot x\wedge\ddot x)^2=-(4\sin^2t+4\cos^2t+16)=-20$; the trivector is $\dot x\wedge\ddot x\wedge\dddot x=(\dot x\cdot(\ddot x\times\dddot x))i=4i$; and the invariants follow from the formulas of the preceding subsection, and agree with the classical helix values $a/(a^2+b^2)=2/5$ and $b/(a^2+b^2)=1/5$.

## Surfaces: The Frame, the Two Forms and the Curvatures

### The Frame of a Surface

Let the surface be $x(u,v)$, a smooth $\mathbb{G}_1$-valued function of two parameters, with $x_u\times x_v\neq0$. Define the frame by

$$
v_1=\frac{x_u}{|x_u|},\qquad v_3=\frac{x_u\times x_v}{|x_u\times x_v|},\qquad v_2=v_3\times v_1 ,
$$

so that $v_3$ is the unit normal and $(v_1,v_2,v_3)$ is a direct orthonormal frame with $v_1,v_2$ tangent. The frame is $v_k=r\gamma_kr^{\dagger}$ for the rotor $r$ of the next subsection, and its connection is written in the components of the basis of the parameters,

$$
\iota_j=a_j\,\mathrm du+b_j\,\mathrm dv ,\qquad j=1,2,3 .
$$

**Definition.** The **coframe** of the surface is the pair of one-forms $\omega_1,\omega_2$ of the displacement of the point in the frame,

$$
\mathrm dx=\omega_1v_1+\omega_2v_2,\qquad
\omega_1=A_1\mathrm du+B_1\mathrm dv,\qquad \omega_2=A_2\mathrm du+B_2\mathrm dv ,
$$

with coefficients $A_1=x_u\cdot v_1$, $B_1=x_v\cdot v_1$, $A_2=x_u\cdot v_2$, $B_2=x_v\cdot v_2$, and the **first fundamental form** is

$$
\mathrm ds^2=\omega_1^2+\omega_2^2=E\,\mathrm du^2+2F\,\mathrm du\,\mathrm dv+G\,\mathrm dv^2 ,
$$

with $E=x_u\cdot x_u$, $F=x_u\cdot x_v$, $G=x_v\cdot x_v$, and $A_1B_2-A_2B_1=\sqrt{EG-F^2}$.

**Proof.** The displacement is tangential, so its normal component vanishes and the expansion has two terms; the coefficients are the scalar products of the coordinate derivatives with the frame vectors; and the first fundamental form is the squared length of $\mathrm dx$, which is $\omega_1^2+\omega_2^2$ because the frame is orthonormal. Expanding the two forms in the basis and comparing with $E,F,G$ gives the two matrices, whose determinants are equal.

### The Second Fundamental Form

**Definition.** The **second fundamental form** is

$$
\Pi:=-\,\mathrm Dv_3\cdot\mathrm dx=-\,\mathrm Dv_3\cdot(\omega_1v_1+\omega_2v_2),
$$

the scalar product of the covariant differential of the normal with the displacement.

**Theorem.** $\Pi$ is a symmetric bilinear form in the two directions, the differential of the normal has no component along the normal itself because $v_3$ has constant length, and

$$
\Pi=L_{11}\omega_1^2+L_{22}\omega_2^2+2L_{12}\omega_1\omega_2 ,
$$

the coefficients being the **second fundamental form in the frame**, the classical $L,M,N$ of the Gauss map,

$$
L_{11}=\frac{b_2A_2-b_1B_2}{\Delta_0},\qquad
L_{22}=\frac{a_2A_1-a_1B_1}{\Delta_0},\qquad
L_{12}=\frac{b_1B_1-b_2A_1}{\Delta_0},\qquad
\Delta_0=A_1B_2-A_2B_1 ,
$$

where $\iota_1=a_1\mathrm du+a_2\mathrm dv$ and $\iota_2=b_1\mathrm du+b_2\mathrm dv$ are the first two components of the connection.

**Proof.** Put $k=3$ in the components of the covariant differential: $\mathrm Dv_3=\iota_2\gamma_1-\iota_1\gamma_2$, a tangent vector, so the normal has no component along itself in $\mathrm dv_3$ and the tangent components are $b=b_1\mathrm du+b_2\mathrm dv$ along $v_1$ and $-a$ along $v_2$. With $\mathrm dx=\omega_1v_1+\omega_2v_2$, the interior product gives $\Pi=-\iota_2\omega_1+\iota_1\omega_2$. Setting $\iota_2=-L_{11}\omega_1-L_{12}\omega_2$ and $\iota_1=L_{21}\omega_1+L_{22}\omega_2$, which is what a symmetric $\Pi$ means, and solving the two linear systems for $L_{11},L_{12}$ and $L_{21},L_{22}$ gives the coefficients, and $L_{12}=L_{21}$ is the integrability condition of the next section.

### The Gaussian and the Mean Curvature

**Definition.** The **principal curvatures** are the two eigenvalues of the second fundamental form,

$$
K_1,K_2=\tfrac12\Bigl(L_{11}+L_{22}\mp\sqrt{(L_{11}-L_{22})^2+4L_{12}^2}\Bigr),
$$

and the **Gaussian curvature** and the **mean curvature** are

$$
K=K_1K_2=L_{11}L_{22}-L_{12}^2,\qquad
H=\tfrac12(K_1+K_2)=\tfrac12(L_{11}+L_{22}) .
$$

**Theorem (Gauss, the theorema egregium in the frame).** The Gaussian curvature is the ratio of the determinant of the exterior products of the connection's first two components to the determinant of the coframe,

$$
K=\frac{a_1b_2-a_2b_1}{A_1B_2-A_2B_1},
$$

and the mean curvature is

$$
H=\frac{-b_1B_2+b_2A_2+a_2A_1-a_1B_1}{2\,(A_1B_2-A_2B_1)} .
$$

Moreover, the third coefficient of the structure equation of the next section reads $K=(\partial_vc_1-\partial_uc_2)/(A_1B_2-A_2B_1)$, and the first two integrability conditions determine $c_1,c_2$ from the coframe alone, so that $K$ is a function of the first fundamental form and of nothing else.

**Proof.** The eigenvalues of a $2\times2$ symmetric matrix are the displayed ones, so the product is the determinant and half the sum the half-trace. For the formula in the connection, substitute the coefficients of the preceding theorem: expanding $(b_2A_2-b_1B_2)(a_2A_1-a_1B_1)-(b_1B_1-b_2A_1)(a_1B_2-a_2A_2)$ in the numerator of $L_{11}L_{22}-L_{12}^2$ cancels in pairs and leaves $\Delta_0\,(a_1b_2-a_2b_1)$, so $K=(a_1b_2-a_2b_1)/\Delta_0$. For the dependence on the metric alone, the structure equation of the next section has third coefficient $\partial_vc_1-\partial_uc_2=a_1b_2-a_2b_1$, so that $K$ is the same ratio with the derivatives of the $c$'s above the line, and the first two integrability conditions determine $c_1,c_2$ from the coframe alone with the non-vanishing determinant $\Delta_0$; hence $K$ is computable from the first fundamental form alone, which is Gauss's theorem. Its general Riemannian form is *Curvature and Geodesics*.

**Remark (the sign of the curvatures).** The convention is the one fixed by $\mathrm Dv_3=-K\,\mathrm dx$ in the frame, equivalently by the shape operator $S=-\mathrm dN$, which is the standard one: the mean curvature of the sphere of radius $r$ with the *outward* normal is $-1/r$ and its Gaussian curvature is $+1/r^2$. The Gaussian curvature is unchanged by the choice of normal, the mean curvature changes sign with it.

### The Darboux Frame Along a Curve on the Surface

**Definition.** Let a curve lie on the surface and let $v_1$ of the frame be its unit tangent. The frame is then the **Darboux frame**, and its three connection components are named

$$
\iota_1=\tau_r\,\mathrm ds,\qquad \iota_2=-\rho_n\,\mathrm ds,\qquad \iota_3=\rho_g\,\mathrm ds ,
$$

the **relative torsion**, the **normal curvature** and the **geodesic curvature** of the curve.

**Theorem.** In the Darboux frame the frame equations are

$$
\mathrm Dv_1=(\rho_gv_2+\rho_nv_3)\mathrm ds,\qquad
\mathrm Dv_2=(-\rho_gv_1+\tau_rv_3)\mathrm ds,\qquad
\mathrm Dv_3=(-\rho_nv_1-\tau_rv_2)\mathrm ds ,
$$

and if the Frenet frame of the same curve has invariants $\rho,\tau$ and the Frenet binormal makes the angle $\alpha$ with the surface normal, then

$$
\rho_n=-\rho\sin\alpha,\qquad \rho_g=\rho\cos\alpha,\qquad \tau_r=\tau+\frac{\mathrm d\alpha}{\mathrm ds} .
$$

**Proof.** Put the three components in the components of the covariant differential. For the second part, the two frames differ by a rotation in the tangent plane: the Frenet frame is obtained from the Darboux frame by the rotation of angle $\alpha$ about $v_1$, and the connection transforms accordingly; comparing the coefficients of $\gamma_3$ in $\mathrm Dv_1$ gives $\rho_n=-\rho\sin\alpha$ and those of $\gamma_2$ gives $\rho_g=\rho\cos\alpha$, while the coefficient of $\gamma_1$ in $\mathrm Dv_2$ gives $\tau_r=\tau+\mathrm d\alpha/\mathrm ds$.

### The Integrability of the Frame

A frame $r(u,v)$ is not arbitrary: the mixed second derivatives of the frame agree, and this is the one equation the connection must satisfy.

**Theorem (the structure equation).** The connection of a frame of a surface satisfies

$$
\frac{\partial\iota_1}{\partial v}-\frac{\partial\iota_2}{\partial u}=\iota_1\wedge\iota_2 ,
$$

where $\iota_1=\iota_1^u\mathrm du+\iota_1^v\mathrm dv$ and $\iota_2=\iota_2^u\mathrm du+\iota_2^v\mathrm dv$ are read as grade-two elements of coefficients $(a_1,b_1,c_1)$ and $(a_2,b_2,c_2)$, and the wedge of two grade-two elements is the cross product of their coefficients. In coefficients,

$$
\frac{\partial a_1}{\partial v}-\frac{\partial a_2}{\partial u}=b_1c_2-b_2c_1,\qquad
\frac{\partial b_1}{\partial v}-\frac{\partial b_2}{\partial u}=c_1a_2-c_2a_1,\qquad
\frac{\partial c_1}{\partial v}-\frac{\partial c_2}{\partial u}=a_1b_2-a_2b_1 .
$$

**Theorem (integrability of the point).** Let $\delta$ be the increment in $v$ and $\mathrm d$ the increment in $u$, so that $\delta\mathrm d=\mathrm d\delta$ on functions, and let $M=x$ be the point. The condition that the two mixed second differences of $M$ agree, $\delta(\mathrm DM)-\mathrm d(\delta M)=0$, is equivalent to

$$
\frac{\partial A_1}{\partial v}-\frac{\partial B_1}{\partial u}=-B_2c_1+A_2c_2,\qquad
\frac{\partial A_2}{\partial v}-\frac{\partial B_2}{\partial u}=B_1c_1-A_1c_2,\qquad
A_1b_2+B_2a_1=A_2a_2+B_1b_1 ,
$$

the first two of which determine the two coefficients $c_1,c_2$ of $\iota_3$ linearly from the coframe and the first two components of the connection, and the third of which is the symmetry $L_{12}=L_{21}$ of the second fundamental form.

**Proof.** The first statement is the equality of the mixed second derivatives of $r$, $\partial_v\partial_ur=\partial_u\partial_vr$, written with $\mathrm d\iota=2r^{\dagger}\mathrm dr$: expanding $\partial_v(2r^{\dagger}\partial_ur)-\partial_u(2r^{\dagger}\partial_vr)$ and using $r^{\dagger}r=e_0$ leaves the commutator $\tfrac12(\iota_1\iota_2-\iota_2\iota_1)$, whose three coefficients are the displayed ones. The second statement is the same computation with the frame equation: differentiating $\mathrm dM=r\,\mathrm DM\,r^{\dagger}$ and reading the result in the frame turns the trivial identity $\delta\mathrm dM=\mathrm d\delta M$ into three equations on the coefficients, two of which are linear in $c_1,c_2$ with the coframe and $\iota_1,\iota_2$ as data. The third equation is the symmetry condition on the second fundamental form of the preceding section, and it is the reason the same $L_{12}$ appears in the two systems.

**Remark (the two classical names).** The two theorems are the classical Gauss and Codazzi–Mainardi equations in this frame: the structure equation is the Gauss equation — it is the one that makes the Gaussian curvature depend on the metric alone — and the symmetry $L_{12}=L_{21}$ is the Codazzi–Mainardi equation. They are stated here as the integrability of one frame and not as a pair of tensor identities, which is the economy of the moving-frame method.

### The Three Distinguished Families of Curves on a Surface

**Theorem (curvature lines).** The second fundamental form is diagonal, $L_{12}=0$, in a frame rotated in the tangent plane through the angle $\Phi$ given by

$$
\tan 2\Phi=\frac{2L_{12}}{L_{11}-L_{22}} ,
$$

and the curves whose tangent direction has this property at every point are the **curvature lines**. The two families are orthogonal, unless the point is **umbilic**, $L_{11}=L_{22}$ and $L_{12}=0$, where every direction is a principal direction and the two families are not separated.

**Theorem (asymptotic lines).** The curves along which the normal curvature vanishes, $\rho_n=0$, are the **asymptotic lines**, and their directions are given by

$$
\rho_n=L_{22}\sin^2\Phi+L_{11}\cos^2\Phi+2\sin\Phi\cos\Phi\,L_{12}=0,
\qquad \tan\Phi=\frac{-L_{12}\pm\sqrt{L_{12}^2-L_{11}L_{22}}}{L_{22}} ,
$$

the two directions being real exactly when the Gaussian curvature is negative or the second fundamental form is degenerate; on the sphere, where the point is umbilic, there are none.

**Theorem (geodesics).** The curves along which the geodesic curvature vanishes, $\rho_g=0$, are the **geodesics**, and with $\iota_3=c_1\mathrm du+c_2\mathrm dv$ the condition is

$$
\iota_3+\mathrm d\Bigl(\arctan\frac{\omega_2}{\omega_1}\Bigr)=0 ,\qquad\text{that is}\qquad
c_1\mathrm du+c_2\mathrm dv+\mathrm d\arctan\frac{A_2\mathrm du+B_2\mathrm dv}{A_1\mathrm du+B_1\mathrm dv}=0 ,
$$

the second term being the differential of the angle of the curve with the first frame vector, which is the statement that the geodesic curvature is the rate of turn of the tangent in the *surface's* frame in excess of the turn forced by the connection.

**Proof.** For the curvature lines, substituting the rotated coefficients in $\Pi$ shows that the cross term vanishes exactly when $\tan2\Phi=2L_{12}/(L_{11}-L_{22})$, and at an umbilic all directions give the same value because $L_{12}=0$ and $L_{11}=L_{22}$. For the asymptotic lines, put $\rho_n=0$ in the normal curvature written in the direction angle $\Phi$ and divide by $\cos^2\Phi$, which gives a quadratic in $\tan\Phi$ whose discriminant is $4(L_{12}^2-L_{11}L_{22})$. For the geodesics, a curve whose unit tangent makes the angle $\Phi=\arctan(\omega_2/\omega_1)$ with the first frame vector turns in the surface at the rate $\mathrm d\Phi/\mathrm ds+\iota_3/\mathrm ds$, the first term being the turn of the tangent within the tangent plane and the second the connection's own turn about the normal; the geodesic curvature is that rate, and its vanishing is the displayed condition.

**Remark (the second form or the first).** The curvature lines and the asymptotic lines are distinguished by the **second** fundamental form — the directions that diagonalise it, and the directions in which it vanishes — while the geodesics are distinguished by the **first** alone, being the curves whose geodesic curvature, which is read from the connection and the metric, vanishes. This is why the two families through a non-umbilic point always exist, why a pair of asymptotic directions exists only where $K\le0$, and why a geodesic exists through every point in every direction.

### Example: The Sphere of Radius $r$

**Example.** Let $x(u,v)=r\sin u\cos v\,\gamma_1+r\sin u\sin v\,\gamma_2+r\cos u\,\gamma_3$, with $u=\theta$ the polar angle and $v=\phi$ the azimuth. Then $\omega_1=r\,\mathrm d\theta$, $\omega_2=r\sin\theta\,\mathrm d\phi$, and the frame of the two subsections above is

$$
v_1=\cos\theta\cos\phi\,\gamma_1+\cos\theta\sin\phi\,\gamma_2-\sin\theta\,\gamma_3,\qquad
v_2=-\sin\phi\,\gamma_1+\cos\phi\,\gamma_2,\qquad
v_3=\frac{x}{r},
$$

the rotor of the frame is $r=\exp(\tfrac12\phi\,e_3)\exp(\tfrac12\theta\,e_2)$ in the sense of the exponential series of the real quaternions, and the connection is

$$
\mathrm d\iota=2r^{\dagger}\mathrm dr=-\sin\theta\,\mathrm d\phi\,e_1+\mathrm d\theta\,e_2+\cos\theta\,\mathrm d\phi\,e_3 .
$$

Hence $a_1=0$, $a_2=-\sin\theta$, $b_1=1$, $b_2=0$, $c_1=0$, $c_2=\cos\theta$, and

$$
K=\frac{1}{r^2},\qquad H=-\frac{1}{r},
$$

the curvature constant and the surface umbilic at every point, and the latitude circle of polar angle $\theta_0$ has geodesic curvature $\rho_g=\cot\theta_0$, vanishing at the equator, which is the great circle.

**Proof.** The frame is the sandwich of the generators by the displayed rotor, which is the composition of a rotation of $\phi$ about $e_3$ and one of $\theta$ about the moved second axis; the connection is $2r^{\dagger}\mathrm dr$ expanded in the two parameters; the two curvatures follow from the formulas of the Gaussian and mean curvature with $\Delta_0=r^2\sin\theta$; the geodesic curvature is the third component of the connection along the curve, as in the geodesic theorem.

## Summary

A moving orthonormal frame in the three-dimensional Euclidean space is a rotor $r$ of the real quaternion subspace of $\mathbb{B}$, the frame is $v_k=r\gamma_kr^{\dagger}$, and the whole infinitesimal displacement of the frame is the single $\mathbb{G}_2$-valued one-form

$$
\mathrm d\iota=2r^{\dagger}\mathrm dr=\iota_1e_1+\iota_2e_2+\iota_3e_3,\qquad
\mathrm dv_k=r\,\mathrm Dv_k\,r^{\dagger},\qquad
\mathrm Dv_k=\tfrac12\bigl(\mathrm d\iota\,\gamma_k-\gamma_k\,\mathrm d\iota\bigr),
$$

with the three components $\mathrm Dv_1=\iota_3\gamma_2-\iota_2\gamma_3$, $\mathrm Dv_2=\iota_1\gamma_3-\iota_3\gamma_1$, $\mathrm Dv_3=\iota_2\gamma_1-\iota_1\gamma_2$.

For a **curve**, the Frenet frame is the frame with $\mathrm dx=\mathrm ds\,v_1$ and $\iota_2=0$; its connection is $\mathrm d\iota_F=\tau\,\mathrm ds\,e_1+\rho\,\mathrm ds\,e_3$, the frame equations being the Frenet equations, and the two invariants are read from the derivatives as $\rho=|\dot x\wedge\ddot x|/|\dot x|^3$ and $\tau=i\langle\dot x\ddot x\dddot x\rangle_3/(\dot x\wedge\ddot x)^2$ in the sign of the exterior product fixed here. The circular helix of curvature $2/5$ and torsion $1/5$ is the worked case.

For a **surface**, the frame has $v_3$ normal, the coframe $\omega_1,\omega_2$ gives the first fundamental form $\mathrm ds^2=\omega_1^2+\omega_2^2$, and the second fundamental form is $\Pi=-\mathrm Dv_3\cdot\mathrm dx=L_{11}\omega_1^2+2L_{12}\omega_1\omega_2+L_{22}\omega_2^2$, whose coefficients are the $a$'s and $b$'s of the connection. Its determinant and its half-trace are the Gaussian and the mean curvature, $K=L_{11}L_{22}-L_{12}^2$, $H=\tfrac12(L_{11}+L_{22})$, and the Gaussian curvature is the ratio of the determinants of the connection and of the coframe, $K=(a_1b_2-a_2b_1)/(A_1B_2-A_2B_1)$, a function of the first fundamental form alone: this is the theorema egregium in the moving frame.

Along a curve on the surface the frame is the Darboux frame, whose three components are the relative torsion, the normal curvature and the geodesic curvature, $\iota_1=\tau_r\mathrm ds$, $\iota_2=-\rho_n\mathrm ds$, $\iota_3=\rho_g\mathrm ds$, related to the Frenet invariants by $\rho_n=-\rho\sin\alpha$, $\rho_g=\rho\cos\alpha$ and $\tau_r=\tau+\mathrm d\alpha/\mathrm ds$. The frame is integrable exactly when the structure equation $\partial_v\iota_1-\partial_u\iota_2=\iota_1\wedge\iota_2$ and the symmetry $L_{12}=L_{21}$ hold, the Gauss and Codazzi–Mainardi equations of the classical theory. The curvature lines are the directions making the second fundamental form diagonal, $\tan2\Phi=2L_{12}/(L_{11}-L_{22})$; the asymptotic lines are the directions of vanishing normal curvature, real exactly where $K\le0$; and the geodesics are the curves whose geodesic curvature vanishes, $\iota_3+\mathrm d\arctan(\omega_2/\omega_1)=0$. On the sphere of radius $r$ the frame, the connection and the curvatures are computed explicitly, $K=1/r^2$ and $H=-1/r$, the surface is umbilic, and a latitude circle has geodesic curvature $\cot\theta_0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_0,e_1,e_2,e_3$ | Basis of $\mathbb{B}$, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary; the pseudoscalar |
| $\gamma_k=ie_k$, $\gamma_k^2=e_0$ | Generators of the grade-one subspace |
| $\mathbb{G}_1,\mathbb{G}_2,\mathbb{G}_3$ | Grades one, two and three |
| $\mathbb{H}_{\mathbb{B}}$ | Real quaternion subspace, $\mathbb{G}_0\oplus\mathbb{G}_2$ |
| $[v]$ | The grade-two element of coefficient vector $v$ |
| $a\wedge b=-\tfrac12(ab-ba)=[a\times b]$ | Exterior product, this article's sign |
| $a\cdot b=\tfrac12(ab+ba)$ | Interior product on $\mathbb{G}_1$ |
| $a\wedge[v]=(a\cdot v)i$ | Scalar triple product |
| $r$, $r^{\dagger}r=e_0$ | Rotor of the frame, $^{\dagger}$ Hermitian conjugation |
| $v_k=r\gamma_kr^{\dagger}$ | The moving frame |
| $\mathrm d\iota=2r^{\dagger}\mathrm dr=\iota_1e_1+\iota_2e_2+\iota_3e_3$ | Affine connection one-form |
| $\iota_1,\iota_2,\iota_3$ | Its three real one-form components |
| $\mathrm Dv_k=\tfrac12(\mathrm d\iota\gamma_k-\gamma_k\mathrm d\iota)$ | Covariant differential |
| $\mathrm dv_k=r(\mathrm Dv_k)r^{\dagger}$ | The frame equation |
| $s$, $\rho$, $\tau$ | Arc length, curvature, torsion |
| $\dot x,\ddot x,\dddot x$ | Derivatives in a parameter $t$ |
| $\Delta_\beta=\dot x\cdot(\ddot x\times\dddot x)$ | Determinant of three derivatives; $\beta=\Delta_\beta i$ |
| $v_1,v_2,v_3$ | Tangent, principal normal, binormal |
| $\iota_2=0$ | Characterisation of the Frenet frame |
| $\omega_1,\omega_2$ | Coframe of a surface, $\omega_1^2+\omega_2^2=\mathrm ds^2$ |
| $A_1,B_1,A_2,B_2$, $\Delta_0$ | Coefficients of the coframe and their determinant |
| $L_{11},L_{12},L_{22}$ | Second fundamental form in the frame |
| $\Pi=-\mathrm Dv_3\cdot\mathrm dx$ | Second fundamental form |
| $K=L_{11}L_{22}-L_{12}^2$, $H=\tfrac12(L_{11}+L_{22})$ | Gaussian and mean curvature |
| $K=(a_1b_2-a_2b_1)/(A_1B_2-A_2B_1)$ | Gauss, in the frame |
| $\tau_r,\rho_n,\rho_g$ | Relative torsion, normal curvature, geodesic curvature |
| $\alpha$ | Angle from the surface normal to the Frenet binormal |
| $\Phi$ | Angle of a direction in the tangent frame |
| $\tan2\Phi=2L_{12}/(L_{11}-L_{22})$ | Curvature lines |
| $\tan\Phi=(-L_{12}\pm\sqrt{L_{12}^2-L_{11}L_{22}})/L_{22}$ | Asymptotic lines |
| $\iota_3+\mathrm d\arctan(\omega_2/\omega_1)=0$ | Geodesics |

## Further Reading

- Patrick R. Girard, Patrick Clarysse, Romaric Pujol, Liang Wang and Philippe Delachartre, *Differential Geometry Revisited by Biquaternion Clifford Algebra*, in *Curves and Surfaces* (Lecture Notes in Computer Science 9213, Springer, 2015), 216–242, the source of the construction recorded here: the biquaternion calculus with its exterior product, the affine connection bivector, the Frenet and Darboux frames, the curvature lines, the asymptotic lines, the geodesics and the two worked examples.
- Patrick R. Girard, *Quaternions, Clifford Algebras and Relativistic Physics* (Birkhäuser, Basel, 2007), for the hyperquaternion algebras and the extension of the calculus to the four-dimensional pseudo-Euclidean case.
- Gaston Casanova, *L'algèbre vectorielle* (Presses Universitaires de France, Paris, 1976), for the interior and exterior products of multivectors and the classical vector-calculus identities they reproduce, in the form the source follows.
- John Snygg, *A New Approach to Differential Geometry using Clifford's Geometric Algebra* (Springer, New York, 2012), for the Clifford-algebra development of the same local theory, in the classical frame rather than the biquaternion one.
- Heinrich W. Guggenheimer, *Differential Geometry* (Dover, New York, 1976), for the classical local theory and its exercises.
- Manfredo P. do Carmo, *Differential Geometry of Curves and Surfaces* (Prentice-Hall, 1976), for the classical local theory of the Frenet frame, of the two fundamental forms and of the Gauss and Codazzi–Mainardi equations, against which the formulas of this article are read.
- Wilhelm Klingenberg, *A Course in Differential Geometry* (Springer, 1978), for the moving-frame method and the structure equations of a surface in the classical form.
- Élie Cartan, *Leçons sur la géométrie des espaces de Riemann* (Gauthier-Villars, Paris, 1928), for the method of moving frames and the connection forms as the general apparatus of which the construction here is the three-dimensional instance.

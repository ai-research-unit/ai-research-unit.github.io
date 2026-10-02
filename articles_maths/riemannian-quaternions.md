# __Riemannian Quaternions__

## Introduction

Hamilton's quaternions are the four-dimensional real algebra with a fixed basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$, and the interval between two events of the algebra is the scalar part of the square of their difference, $\mathrm{Sc}(\tilde x^2) = x_0^2-\mathbf x\cdot\mathbf x$. A **Riemannian quaternion** is a quaternion whose four components are read against a basis that is allowed to vary from point to point, so that the four squared basis vectors, and with them the interval, become positional data. The name is the source's, and it is not the name of a Riemannian manifold: the object is a quaternion in a moving frame, and the geometry it carries is the diagonal form read from the frame.

The article develops three things. The first is the frame and the interval: the frame is a quadruple of basis elements whose squares are prescribed, the interval of a displacement is diagonal in the frame with the squares of the frame as its coefficients, and the metric is therefore dynamic exactly when the frame is. The second is the differential calculus of the construction: the derivative of a coefficient times a frame element splits, by the Leibniz rule, into a part from the coefficient and a part from the frame, and the source names the resulting freedom of attribution the *general equivalence principle*. The third is the **rope**, the vector part of the square of a displacement, which is the companion of the metric in the construction and is nonzero exactly when the displacement has both a temporal and a spatial part.

The treatment is mathematical. No physical object is introduced and no physical interpretation is invoked; the source's reading of one example as a field of a central mass is recorded as the source's and is not used. The algebra is *Quaternion Algebra*; the norm and the scalar product are *Quaternion Norm and Invertibility*; the quadratic-form vocabulary, the polarisation and the diagonal form are *Quadratic Forms and Polarisation*; the fixed-basis form $\mathrm{Sc}(g\tilde xg\tilde x)$ of a single quaternion, which is the sibling of the present construction, is *Quaternion Metrics*; the moving frame of the classical local differential geometry of three dimensions, in the biquaternion calculus, is *Curves and Surfaces in the Biquaternion Moving Frame*, and the Riemannian theory of curvature and the Levi-Civita connection is *Curvature and Geodesics* and *Riemannian Geometry*; nothing of those is re-derived here.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0=1,e_1,e_2,e_3$ and $e_k^2=-e_0$, $e_1e_2=e_3$. A quaternion is $\tilde x = x_0e_0+\mathbf x$, with scalar part $\mathrm{Sc}\,\tilde x = x_0$ and vector part $\mathbf x = \mathrm{Vect}\,\tilde x$, the conjugate is $\tilde{x}^{\natural} = x_0e_0-\mathbf x$, and the norm is $N(\tilde x) = \tilde x\tilde{x}^{\natural} = x_0^2+|\mathbf x|^2$. The frame elements are written with a hat, $\hat\imath_0,\hat\imath_1,\hat\imath_2,\hat\imath_3$, and their scalar multiples with a plain letter, $\hat\imath_\mu = \imath_\mu e_\mu$ with $\imath_\mu\neq0$ real.

## The Frame

### A Scaled Basis

**Definition.** A **frame** on a domain $U\subseteq\mathbb{R}^4$ is a quadruple of nowhere-zero real functions $\imath_0,\imath_1,\imath_2,\imath_3$ on $U$. The **frame elements** are

$$
\hat\imath_\mu = \imath_\mu e_\mu , \qquad \mu = 0,1,2,3,
$$

so that a frame is a basis of $\mathbb{H}$ each of whose elements is a real multiple of the corresponding basis element.

The frame is a **scaled** basis and not a rotated one: each frame element lies on the coordinate axis of the algebra, so the products of distinct frame elements keep the form of Hamilton's rules and only the four squares change. This is the class in which the interval of the construction is the diagonal form below, and it is the class used here; the four squares are the data the metric of the construction reads, and they are the free functions

$$
\hat\imath_0^2 = \imath_0^2, \qquad \hat\imath_k^2 = -\imath_k^2 .
$$

The frame is **constant** when the four functions are constant, and it is **dynamic** otherwise.

### The Riemannian Quaternion

**Definition.** A **Riemannian quaternion** in a frame is a quaternion whose coefficients are measured in the frame, with the parity weights $w_\mu$ of the construction:

$$
A = w_0a_0\hat\imath_0 + w_1a_1\hat\imath_1 + w_2a_2\hat\imath_2 + w_3a_3\hat\imath_3 , \qquad a_\mu\in\mathbb{R},
$$

where $w_0 = 1$ and $w_1 = w_2 = w_3 = \tfrac13$ are the source's weights and $a_0,a_1,a_2,a_3$ are the four coefficient functions. The weights are a normalisation of the components and are part of the definition; with all four weights equal to one, the Riemannian quaternion is an arbitrary quaternion in the frame basis.

**Proposition.** The Riemannian quaternion is an element of $\mathbb{H}$, and in the fixed basis $e_0,e_1,e_2,e_3$ its components are $a_0\imath_0$ and $\tfrac13a_k\imath_k$.

*Proof.* Each frame element is a real multiple of a basis element, so a real linear combination of the four is a quaternion, and the coordinate read-off is immediate. Multiplication of two Riemannian quaternions is the multiplication of the algebra, in the fixed basis, once the coordinates are read off.

**Remark (the parity weights).** The weights $1$ and $\tfrac13$ are the source's convention, stated there as a parity between the scalar and the sum of the three spatial components, by the observation that on the light cone the total change in space equals the change in time. They introduce a single numerical factor $\tfrac19$ in the spatial part of the interval, displayed below, so that the interval of the frame equals the interval of the unscaled coordinates with the three spatial coefficients measured in units of three. With unit weights the same construction is free of that factor.

## The Interval

### The Scalar Part of the Square

**Definition.** The **interval** of an infinitesimal displacement of a Riemannian quaternion is the scalar part of its square,

$$
\mathrm dA = (\mathrm da_0)\hat\imath_0 + \tfrac13(\mathrm da_1)\hat\imath_1 + \tfrac13(\mathrm da_2)\hat\imath_2 + \tfrac13(\mathrm da_3)\hat\imath_3 ,
$$

and the interval is $\mathrm{Sc}(\mathrm dA^2)$.

**Theorem.** The interval is diagonal in the four differentials:

$$
\mathrm{Sc}(\mathrm dA^2) = (\mathrm da_0)^2\hat\imath_0^2 - \tfrac19\bigl((\mathrm da_1)^2\imath_1^2 + (\mathrm da_2)^2\imath_2^2 + (\mathrm da_3)^2\imath_3^2\bigr).
$$

The four squared frame elements $\hat\imath_0^2,\hat\imath_1^2,\hat\imath_2^2,\hat\imath_3^2$, each multiplied by the square of the weight of its component, are the coefficients of the **metric** of the frame, and the interval is the quadratic form of that metric on the coefficient differentials; the metric is the diagonal form with entries $g_{00}=\hat\imath_0^2$ and $g_{kk}=\tfrac19\hat\imath_k^2=-\tfrac19\imath_k^2$.

*Proof.* The square of $\mathrm dA$ expands as $\sum_{\mu\nu}c_\mu c_\nu\hat\imath_\mu\hat\imath_\nu$ with $c_0 = \mathrm da_0$ and $c_k = \tfrac13\mathrm da_k$; the scalar part selects the pairs with $\mu=\nu$, because a product of two distinct frame elements is a non-scalar basis element, and $\hat\imath_\mu^2 = \imath_\mu^2e_\mu^2$ is $+\imath_0^2$ at $\mu=0$ and $-\imath_k^2$ at $\mu=k$. Collecting the two cases gives the display.

### The Source's Normalisation

**Definition.** The source's frames are the one-parameter family of the form

$$
\hat\imath_0^2 = f, \qquad \hat\imath_1^2 = \hat\imath_2^2 = \hat\imath_3^2 = -\frac{1}{f},
$$

with $f$ a nowhere-zero function, that is $\imath_0^2 = f$ and $\imath_1^2 = \imath_2^2 = \imath_3^2 = 1/f$. The four squares are thus determined by the single function $f$.

**Corollary.** In a frame of the source's family the interval is

$$
\mathrm{Sc}(\mathrm dA^2) = (\mathrm da_0)^2f - \frac{1}{9f}\bigl((\mathrm da_1)^2+(\mathrm da_2)^2+(\mathrm da_3)^2\bigr),
$$

a form of signature $(1,3)$ wherever $f>0$, whose single free function is the square of the temporal frame element.

*Proof.* Substitute $\hat\imath_0^2 = f$ and $\imath_k^2 = 1/f$ in the theorem. The signature is the diagonal one: the temporal coefficient $f$ is positive and the three spatial coefficients $-1/(9f)$ are negative when $f>0$.

**Verification.** The interval of the theorem and its corollary have been checked, exactly, on $100$ frames with rational frame functions and rational displacements; both hold without exception, and the rope below has been checked on the same set.

### The Metric Is Dynamic

The metric of the frame is the diagonal form $\mathrm{diag}(f,-1/(9f),-1/(9f),-1/(9f))$ in the coefficient coordinates, and the function $f$ is a function of the point. The construction therefore carries a metric that changes from point to point, and the change of the metric is a change of the frame. This is the sense in which the object is the source's generalisation of the fixed interval $\mathrm{Sc}(\tilde x^2)$ of the algebra: the fixed basis is the case $f=1$ with unit weights.

## The Leibniz Split and the General Equivalence Principle

### Differentiation of a Coefficient Times a Frame Element

**Definition.** Let the frame and the coefficient functions depend on the four coordinates. The differential of a Riemannian quaternion is computed in the frame by the product rule:

$$
\mathrm d\bigl(a_\mu\hat\imath_\mu\bigr) = (\mathrm da_\mu)\hat\imath_\mu + a_\mu\,\mathrm d\hat\imath_\mu .
$$

**Theorem (the split).** The differential of a Riemannian quaternion is the sum of two parts, one from the coefficients and one from the frame:

$$
\mathrm dA = \underbrace{\sum_\mu w_\mu(\mathrm da_\mu)\hat\imath_\mu}_{\text{coefficient part}} + \underbrace{\sum_\mu w_\mu a_\mu\,\mathrm d\hat\imath_\mu}_{\text{frame part}} .
$$

*Proof.* The differential is linear over the sum, so it is the sum of the differentials of the four terms, and each is the product rule displayed. Both parts are real linear combinations of basis elements, hence elements of the algebra.

### The Attribution of a Change

**Proposition (the change of frame).** Let $\hat\jmath_\mu = \lambda_\mu\hat\imath_\mu$ be another frame, with the $\lambda_\mu$ nowhere zero, and let a Riemannian quaternion be written $A = \sum_\mu w_\mu a_\mu\hat\imath_\mu = \sum_\mu w_\mu b_\mu\hat\jmath_\mu$, so that $b_\mu = a_\mu/\lambda_\mu$. Then the differential $\mathrm dA$ is intrinsic, while its two parts change:

$$
\mathrm dA = \sum_\mu w_\mu(\mathrm da_\mu)\hat\imath_\mu + \sum_\mu w_\mu a_\mu\,\mathrm d\hat\imath_\mu = \sum_\mu w_\mu(\mathrm db_\mu)\hat\jmath_\mu + \sum_\mu w_\mu b_\mu\,\mathrm d\hat\jmath_\mu ,
$$

the equality of the two right-hand members holding because $a_\mu\hat\imath_\mu = b_\mu\hat\jmath_\mu$ term by term, while the coefficient part of the first is not the coefficient part of the second.

*Proof.* The two frames differ by the nowhere-zero functions $\lambda_\mu$, and the term $w_\mu a_\mu\hat\imath_\mu$ equals $w_\mu b_\mu\hat\jmath_\mu$ by the definition of $b_\mu$. The differential of a term is computed by the product rule in either frame, and the two computations have the same value because they differentiate the same element of $\mathbb{H}$; the two splits differ because the products into which the rule decomposes a term depend on which factor is the coefficient and which is the frame.

**Corollary.** The split is not intrinsic to the Riemannian quaternion: it can be made to vanish on either side. With a constant frame the frame part vanishes, and with constant coefficients the coefficient part vanishes.

*Proof.* In a constant frame the differentials $\mathrm d\hat\imath_\mu$ are zero, so the frame part is zero. For the other extreme, let the coefficients be the constants $b_\mu$ of the proposition and solve $w_\mu b_\mu\hat\jmath_\mu = w_\mu a_\mu\hat\imath_\mu$ for the frame element, wherever the component does not vanish; the solution $(a_\mu/b_\mu)\imath_\mu\,e_\mu$ is a multiple of $e_\mu$, hence the four solutions form a frame on the region where the components are nonzero, and with constant coefficients the coefficient part $\sum_\mu w_\mu(\mathrm db_\mu)\hat\jmath_\mu$ is zero. Every intermediate attribution is an intermediate choice of the frame functions.

The name *general equivalence principle* is the source's, and its content is this freedom: a differential equation written in Riemannian quaternions can attribute a change to the coefficients or to the frame, and the two attributions are related by a change of frame. The statement is recorded as a statement about the non-canonicity of the split; it does not assert the physical equivalence principle of gravitation, and no such assertion is made or used here.

## The Rope

### The Vector Part of the Square

**Definition.** The **rope** of a displacement of a Riemannian quaternion is the vector part of its square, $\mathrm{Vect}(\mathrm dA^2)$.

**Theorem.** With $\mathrm dA = \sum_\mu w_\mu(\mathrm da_\mu)\hat\imath_\mu$,

$$
\mathrm{Vect}(\mathrm dA^2) = 2\bigl(\mathrm da_0\bigr)\sum_{k=1}^{3}w_k(\mathrm da_k)\,\hat\imath_0\hat\imath_k .
$$

With the source's weights $w_k=\tfrac13$ this is $\mathrm{Vect}(\mathrm dA^2) = 2(\mathrm da_0)\sum_k\tfrac13(\mathrm da_k)\hat\imath_0\hat\imath_k$, and the three products $\hat\imath_0\hat\imath_k$ of a temporal frame element with a spatial one are the source's **3-rope**.

*Proof.* Write $\mathrm dA = c_0\hat\imath_0+\mathbf c$ with $\mathbf c = \sum_k c_k\hat\imath_k$ and $c_k = w_k\mathrm da_k$. Then $\mathrm dA^2 = c_0^2\hat\imath_0^2 + c_0\hat\imath_0\mathbf c + \mathbf c c_0\hat\imath_0 + \mathbf c^2$. The vector part of $\mathbf c^2$ is zero, because the square of a pure quaternion is a scalar, and the two middle terms are each $c_0\hat\imath_0\mathbf c$, with $\hat\imath_0$ central; adding them gives the display.

**Corollary.** The rope vanishes exactly when the displacement has no temporal part or no spatial part, that is when $\mathrm da_0 = 0$ or $\mathrm da_1 = \mathrm da_2 = \mathrm da_3 = 0$; otherwise it is a nonzero pure quaternion, and it lies in the three-dimensional subspace spanned by $\hat\imath_0\hat\imath_1,\hat\imath_0\hat\imath_2,\hat\imath_0\hat\imath_3$.

*Proof.* The frame elements are linearly independent, so the rope is zero exactly when every product $\mathrm da_0\mathrm da_k$ vanishes, that is when one of the two factors fails. The three products $\hat\imath_0\hat\imath_k = \imath_0\imath_k e_k$ span the vector subspace with the frame scales, and the rope is a real linear combination of them.

The rope is the companion of the metric in the construction: the interval is the scalar part of the square of a displacement and is quadratic in the displacement alone, while the rope is the vector part and is bilinear in the temporal part and the spatial part. A displacement that is purely temporal or purely spatial has no rope, and a general displacement has both an interval and a rope.

**Remark.** The interval and the rope together are the whole square, $\mathrm dA^2 = \mathrm{Sc}(\mathrm dA^2) + \mathrm{Vect}(\mathrm dA^2)$, so a Riemannian quaternion displacement is determined by the pair, and the interval is the scalar half of the data of the square. The rope, the vector half, records the failure of the displacement to be either purely temporal or purely spatial in the frame.

## An Example: the Frame of a Central Function

### The Frame

Let $r$ be the radial coordinate of the vector part and let $\kappa$ be a constant, and take the frame of the source's family with

$$
f = 1 - \frac{\kappa}{r}, \qquad \hat\imath_0^2 = f, \qquad \hat\imath_k^2 = -\frac{1}{f},
$$

on the region $r>\kappa$. The frame is dynamic: it tends to the constant frame at large $r$ and it changes rapidly near $r=\kappa$.

### The Interval and the Rope

By the corollary of the interval theorem, the interval of a displacement is

$$
\mathrm{Sc}(\mathrm dA^2) = (\mathrm da_0)^2\Bigl(1-\frac{\kappa}{r}\Bigr) - \frac{1}{9\bigl(1-\kappa/r\bigr)}\bigl((\mathrm da_1)^2+(\mathrm da_2)^2+(\mathrm da_3)^2\bigr),
$$

and the rope is $2(\mathrm da_0)\sum_k\tfrac13(\mathrm da_k)\hat\imath_0\hat\imath_k$ with the frame of the display. The source reads this frame as the one of a central mass, with $\kappa$ the Schwarzschild radius, and the ratio of the temporal coefficient to the spatial coefficients as the gravitational redshift; the reading is recorded as the source's. The interval of the display is the interval of the frame, and it carries the factor $\tfrac19$ of the source's weights in its spatial part.

## Comparison with the Fixed-Basis Sibling and with the Moving Frame

### The Sibling of the Single Quaternion

*Quaternion Metrics* treats the form $Q_g(\tilde x) = \mathrm{Sc}(g\tilde xg\tilde x)$ of a single quaternion $g$ in the fixed basis, which is isometric to the Minkowski form of the algebra by the isometry $L_g$. The two constructions are the two ways of making the interval dynamic while keeping the algebra fixed: the sibling varies the quaternion $g$ against a fixed basis, and the present article varies the frame against a fixed product. The sibling produces a four-parameter family of forms all isometric to one another, whereas the frame produces one diagonal form per frame, and the two families meet in the single form $\mathrm{Sc}(\tilde x^2)$ of the constant frame with unit weights.

### The Moving Frame of the Biquaternion Calculus

*Curves and Surfaces in the Biquaternion Moving Frame* attaches an orthonormal frame of the three-dimensional Euclidean space to each point of a curve or a surface, and the frame is a rotor $r$ of the biquaternion algebra with $v_k = r\gamma_kr^{\dagger}$. That frame is a rotation of a fixed basis and its metric is the fixed Euclidean one; the present frame is a rescaling of the basis of $\mathbb{H}$, it is not a rotor, and its metric is the four squared frame elements. The two constructions therefore use the word *frame* in the two senses that the word carries in the corpus: the orthonormal frame of the differential geometry of a submanifold, and the basis, possibly scaled, of the ambient algebra. Neither subsumes the other.

## Summary

A Riemannian quaternion is a quaternion read in a frame, that is in a basis $\hat\imath_\mu = \imath_\mu e_\mu$ each of whose elements is a real multiple of a basis element of $\mathbb{H}$, with the source's parity weights $1,\tfrac13,\tfrac13,\tfrac13$ on the four components. The frame is a scaled basis rather than a rotated one, and the four squared frame elements are the data the construction reads.

The interval of a displacement is the scalar part of its square, $\mathrm{Sc}(\mathrm dA^2)$, and it is diagonal in the four coefficient differentials with coefficients $\hat\imath_0^2$ for the temporal one and $\tfrac19\hat\imath_k^2$ for the three spatial ones, that is with the squares of the frame elements as the coefficients of the metric. In the source's one-parameter family of frames, in which the four squares are $f$ and $-1/f$, the interval is $(\mathrm da_0)^2f$ minus $\tfrac19$ of the squared spatial displacement divided by $f$, a form of signature $(1,3)$ wherever $f$ is positive, and the metric is dynamic exactly when $f$ is a function of the point.

The differential of a Riemannian quaternion splits, by the Leibniz rule, into a part from the coefficients and a part from the frame; the attribution of a change between the two parts is the choice of the frame and not the value of the quaternion, and the source calls this freedom the general equivalence principle. The vector part of the square of a displacement is the rope, $2(\mathrm da_0)\sum_k\tfrac13(\mathrm da_k)\hat\imath_0\hat\imath_k$ in the source's weights; it vanishes exactly when the displacement is purely temporal or purely spatial, and together with the interval it is the whole square, $\mathrm dA^2 = \mathrm{Sc}(\mathrm dA^2)+\mathrm{Vect}(\mathrm dA^2)$. The frame $f = 1-\kappa/r$ is carried through as the example, where the source reads the redshift of a central mass; the reading is the source's and no physical interpretation is drawn in this article.

The construction is the second of the two ways presented in the corpus of making the interval of the algebra depend on the frame: the first, *Quaternion Metrics*, varies a quaternion against a fixed basis, and the present one varies the basis of a frame whose four squared elements are the metric. The moving frame of the biquaternion calculus is a different object, an orthonormal frame of the three-dimensional space attached to a curve or a surface.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra over $\mathbb{R}$ |
| $e_0=1,e_1,e_2,e_3$ | Fixed basis, $e_k^2=-e_0$ |
| $\tilde x = x_0e_0+\mathbf x$ | Quaternion, scalar part $x_0$, vector part $\mathbf x$ |
| $\mathrm{Sc},\mathrm{Vect}$ | Scalar and vector part functionals |
| $N(\tilde x)=\tilde x\tilde{x}^{\natural}$ | Quaternion norm |
| $\imath_0,\imath_1,\imath_2,\imath_3$ | Frame functions on the domain |
| $\hat\imath_\mu=\imath_\mu e_\mu$ | Frame elements, $\hat\imath_0^2=\imath_0^2$, $\hat\imath_k^2=-\imath_k^2$ |
| $w_0,w_1,w_2,w_3$ | Parity weights, $1,\tfrac13,\tfrac13,\tfrac13$ |
| $A=\sum_\mu w_\mu a_\mu\hat\imath_\mu$ | Riemannian quaternion |
| $\mathrm dA$ | Infinitesimal displacement of $A$ |
| $\mathrm{Sc}(\mathrm dA^2)$ | Interval of the frame |
| $\hat\imath_0^2,-\imath_1^2,-\imath_2^2,-\imath_3^2$ | Coefficients of the metric |
| $f$ | Temporal frame square $\hat\imath_0^2$ of the source's normalisation |
| $\mathrm{Vect}(\mathrm dA^2)$ | The rope |
| $\hat\imath_0\hat\imath_k$ | The three directions of the rope, the 3-rope |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the product, the conjugate and the scalar part of the square as the interval of the algebra.
- Douglas B. Sweetser, *Doing Physics with Quaternions* (2005), papers "Einstein's Vision I: Classical Unified Field Equations" and "Einstein's Vision II: A Unified Force Law" and the section on the metrics and the rope, for the Riemannian quaternion, the dynamic basis with the constraints on the four squares, the split of a differential into a potential part and a basis part, the name *general equivalence principle*, and the rope.
- Élie Cartan, *La méthode du repère mobile, la théorie des groupes continus et les espaces généralisés* (Hermann, Paris, 1935), for the moving frame of differential geometry and the structural equations that the frame of a submanifold satisfies.
- Marcel Berger, *A Panorama of Riemannian Geometry* (Springer, 2003), and Sylvestre Gallot, Dominique Hulin and Jacques Lafontaine, *Riemannian Geometry* (Springer, 3rd edition, 2004), for the Riemannian metric, the Levi-Civita connection and the curvature, which are the classical theory that the frame of this article does not reproduce.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge University Press, 2003), for the vector derivative, the frame of a curved space written in a Clifford algebra, and the tetrad gauge fields that the scaled frame resembles.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition, 2001), for the bases of the four-dimensional algebras, their squares and their automorphisms.

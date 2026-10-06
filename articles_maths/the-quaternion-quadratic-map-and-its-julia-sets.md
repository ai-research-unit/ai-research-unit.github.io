# __The Quaternion Quadratic Map and Its Julia Sets__

## Introduction

The quadratic map of the quaternion algebra is the map

$$
f_c(\tilde q) = \tilde q^2 + c, \qquad \tilde q, c \in \mathbb{H},
$$

the direct translation to $\mathbb{H}$ of the complex quadratic family $z \mapsto z^2+c$. The translation is forced by the algebra and by nothing else: the quaternion product is associative and unital, so the square $\tilde q^2$ is unambiguous and $\tilde q \mapsto \tilde q^2+c$ is a quadratic polynomial with coefficients in $\mathbb{H}$. It is not commutative and not complex-analytic, and the two failures are the whole subject: the map has a critical point and a four-dimensional phase space, yet the critical orbit is planar, and every invariant complex plane through the origin carries a copy of the ordinary complex quadratic map. Those two facts make the four-dimensional object computable from a two-dimensional one, and they are proved here.

This article defines the map, the filled Julia set and the Julia set, proves the bounded–escaping dichotomy and the escape lemma that makes it effective, determines the symmetry group of the family and of a single member, and identifies the invariant complex planes. It is the first article of the quaternion fractal thread and it fixes the objects the rest of the thread uses.

The quaternion algebra, its conjugation and its basis are from *Quaternion Algebra*; the quaternion norm, its multiplicativity and the modulus are from *Quaternion Norm and Invertibility*; the inner automorphisms and the rotation group of the vector subspace are from *Quaternion Automorphisms and Derivations* and *Quaternion Rotations and Reflections*; the complex quadratic family and its Julia set are from *The Julia Sets of a Complex Polynomial*; and the dimensions and the coverings used below are from *Fractal Geometry*, which owns them. The escape radius and the Green's function are the subject of *The Escape Radius and the Green's Function for Quaternions*; the connectedness locus of the family, that of *The Quaternion Mandelbrot Set*; the theorem that a Julia set is recovered from a slice, that of *The Slices of the Quaternion Julia Sets*; and the dimension, that of *The Dimension of the Quaternion Julia Sets*. Nothing of the general theory of the Fatou set and of the Julia set is rebuilt here: it is Part IV's, in *The Geometry of the Julia Sets*. No physics is invoked.

Throughout, $\tilde q = q_0e_0+q_1e_1+q_2e_2+q_3e_3$ with $q_\mu \in \mathbb{R}$, $e_0=1$ and $e_1^2=e_2^2=e_3^2=-e_0$; the conjugate is $\tilde q^{\natural}=q_0e_0-q_1e_1-q_2e_2-q_3e_3$, the norm is $N(\tilde q)=\tilde q\tilde q^{\natural}=q_0^2+q_1^2+q_2^2+q_3^2$, and the modulus is $|\tilde q|=\sqrt{N(\tilde q)}$. The scalar part is $\operatorname{Sc}\tilde q=q_0$ and the vector part is $\operatorname{Vect}\tilde q=\mathbf q=q_1e_1+q_2e_2+q_3e_3$. The unit sphere of the algebra is $S^3=\{\tilde q:N(\tilde q)=1\}$, and the sphere of the imaginary units is $S^2=\{\nu \in \operatorname{Im}\mathbb{H} : N(\nu)=1\}$.

## The Quadratic Map

### Definition

**Definition.** The **quaternion quadratic map** of the parameter $c \in \mathbb{H}$ is

$$
f_c : \mathbb{H} \to \mathbb{H}, \qquad f_c(\tilde q) = \tilde q^2 + c .
$$

Its $n$-th iterate is written $f_c^{\,n}$, with $f_c^{\,0}=\mathrm{id}$, and the **orbit** of $\tilde q$ is the sequence $\tilde q_n = f_c^{\,n}(\tilde q)$.

Because the quaternion product is associative, the iterates satisfy $f_c^{\,m}\circ f_c^{\,n}=f_c^{\,m+n}$ and the orbit is a genuine dynamical system. The map is a **quadratic polynomial** in the coordinates: expanding $\tilde q^2 = q_0^2-|\mathbf q|^2+2q_0\mathbf q$, its four coordinate functions are quadratic forms, so $f_c$ is a polynomial map $\mathbb{R}^4 \to \mathbb{R}^4$ of degree two with the linear part and the constant term prescribed by $c$.

### The Critical Point

**Proposition.** The real-linear map $\mathrm{d}(f_c)_{\tilde q} : \mathbb{H} \to \mathbb{H}$ is the sum of the left and right multiplications,

$$
\mathrm{d}(f_c)_{\tilde q}\,\tilde h = \tilde q\tilde h + \tilde h\tilde q ,
$$

and its determinant, in the real coordinates $\tilde q=q_0e_0+q_1e_1+q_2e_2+q_3e_3$, is

$$
\det \mathrm{d}(f_c)_{\tilde q} = 16\,q_0^2\,N(\tilde q) = 16\,q_0^2\,|\tilde q|^2 .
$$

Hence the differential is invertible exactly for $q_0\neq0$, and it is singular on the hyperplane $\{q_0=0\}$ of the pure vectors, a three-dimensional set; the point $0$ is one of the critical points but not the only one. Here the algebra is identified with $\mathbb{R}^4$ and the differential is taken in the real sense; no complex structure is used.

*Proof.* The product is bilinear, so the differential of $\tilde q \mapsto \tilde q^2$ at $\tilde q$ in the direction $\tilde h$ is $\tilde q\tilde h+\tilde h\tilde q$, and the constant $c$ contributes nothing. The map is the sum $L_{\tilde q}+R_{\tilde q}$ of the left and the right multiplication, and passing through the matrix model $M_2(\mathbb{C})$ the sum $L_{\tilde q}+R_{\tilde q}$ acts on a matrix $X=\Phi(\tilde h)$ by $X\mapsto \Phi(\tilde q)X+X\Phi(\tilde q)$, whose eigenvalues are the four sums $\mu_i+\mu_j$ of the two eigenvalues $\mu_{1,2}=q_0\pm i|\mathbf q|$ of $\Phi(\tilde q)$; the product of the four sums is $4\mu_1\mu_2(\mu_1+\mu_2)^2=4N(\tilde q)(2q_0)^2$, the displayed determinant. It vanishes exactly when $q_0=0$, since $N(\tilde q)=|\tilde q|^2=0$ forces $\tilde q=0$. $\square$

**Remark (the critical set is larger than the point $0$).** The singular set is the hyperplane of the pure vectors, not a point, and the escape theory below is unaffected because it uses only the multiplicativity of the norm. What the connectedness theory uses is the orbit of the *single* point $0$: the point $0$ lies in the plane $\mathbb{R}[c]$ of the parameter, on which $f_c$ restricts to the complex quadratic map $z\mapsto z^2+\kappa(c)$, and it is the critical point of that planar restriction. The orbit of $0$ is therefore the critical orbit of the invariant complex slice, and it is the orbit that governs the locus.

**Definition.** The **critical orbit** of the parameter $c$ is the orbit of the point $0$,

$$
0, \quad c, \quad c^2+c, \quad (c^2+c)^2+c, \quad \ldots ,
$$

the orbit of the critical point of the invariant complex slice $\mathbb{R}[c]$.

The critical orbit is the simplest orbit of the family and, by the critical slice theorem of the next article, the one that decides the connectedness locus.

## The Escape and the Julia Sets

### The Escape Lemma

**Lemma (escape).** Let $c \in \mathbb{H}$ and put $R(c)=1+|c|$. If $|\tilde q_n| \geq R(c)$ for some $n$, then $|\tilde q_k| \to \infty$ as $k \to \infty$.

*Proof.* The quaternion norm is multiplicative, so $|\tilde q^2|=|\tilde q|^2$; the triangle inequality gives

$$
|\tilde q_{n+1}| = |\tilde q_n^2+c| \geq |\tilde q_n|^2 - |c| .
$$

If $|\tilde q_n| \geq 1+|c|$ then $|\tilde q_{n+1}| \geq |\tilde q_n|^2-|c| > |\tilde q_n| \geq R(c)$, so by induction the moduli are strictly increasing from the index $n$ on. Writing $t_n=|\tilde q_n|$, the function $t \mapsto t^2-t-|c|$ is increasing for $t \geq 1/2$, and therefore for every $k \geq n$

$$
t_{k+1} \geq t_k^2-|c| = t_k + \bigl(t_k^2-t_k-|c|\bigr) \geq t_k + \bigl(R(c)^2-R(c)-|c|\bigr) = t_k + |c|^2 ,
$$

using $R(c)^2-R(c)-|c|=(1+|c|)^2-(1+|c|)-|c|=|c|^2$; the moduli grow at least linearly and $t_k \to \infty$. When $c=0$ the same computation gives $t_{k+1}=t_k^2$ and $t_k \geq 1$ diverges. $\square$

**Remark.** The lemma is the whole of the escape theory that the definite case needs. It uses only the multiplicativity of the norm and the triangle inequality, and it is the reason the quaternion quadratic map is computable: a point that leaves the closed ball of radius $R(c)$ is known to escape, and the ball is where all the work is done. The sharper radius and the potential are in *The Escape Radius and the Green's Function for Quaternions*.

### The Filled Julia Set and the Julia Set

**Definition.** The **filled Julia set** of the parameter $c$ is

$$
K_c = \{\tilde q \in \mathbb{H} : \text{the orbit } \tilde q_n \text{ is bounded}\} ,
$$

and the **Julia set** is its topological boundary,

$$
J_c = \partial K_c .
$$

**Proposition.** $K_c$ is closed and bounded, hence compact and nonempty for every $c$; it is forward-invariant, and it contains the critical orbit exactly when the critical orbit is bounded. The Julia set $J_c=\partial K_c$ is nonempty and compact.

*Proof.* $K_c$ is the complement of the escape set, which is open because $f_c$ is continuous and the sequence of moduli depends continuously on the initial point; and $K_c$ is contained in the closed ball of radius $R(c)$ by the escape lemma. For nonemptiness, the fixed-point equation $f_c(\tilde q)=\tilde q$ is $\tilde q^2-\tilde q+c=0$, which becomes $p^2=d$ with $p=\tilde q-\tfrac12 e_0$ and $d=\tfrac14 e_0-c$; every quaternion $d$ has a square root, and for $d\ne0$ the explicit root is

$$
p = \sqrt{\tfrac{|d|+d_0}{2}}\,e_0 + \frac{\mathbf d}{|\mathbf d|}\sqrt{\tfrac{|d|-d_0}{2}} \quad (\mathbf d\ne0), \qquad p=\pm\sqrt{|d_0|}\,\nu \quad (d=d_0\in\mathbb{R},\ d_0<0,\ \nu \in S^2),
$$

with $p=0$ for $d=0$; the identity $p^2=d$ is checked by squaring the decomposition $d=d_0+\mathbf d$ with $|\mathbf d|^2=|d|^2-d_0^2$. A fixed point lies in $K_c$ because its orbit is constant. Forward-invariance is the definition, and the critical orbit lies in $K_c$ exactly when it is bounded. Finally $K_c$ is nonempty and compact with nonempty complement — it is bounded and $\mathbb{H}$ is unbounded — so its boundary is nonempty and compact. $\square$

**Remark (the dichotomy).** The complement of $K_c$ is the **escape set**, the set of points whose orbit leaves every ball, and in the complex plane the parameter space splits into those parameters for which $K_c$ is connected and those for which it is a Cantor set, the critical orbit deciding the case. In the quaternion algebra the critical orbit governs the **connectedness locus**, by the critical slice theorem of *The Quaternion Mandelbrot Set*; **the connectedness locus of the quaternion family is the rotational hull of the complex Mandelbrot set**, and that article owns the statement. The dichotomy of the connected and the Cantor case is a classical complex statement, quoted per slice and not claimed in four dimensions; what four dimensions define is the set of parameters with a bounded critical orbit. The general theory of the partition of the phase space into a Fatou set and a Julia set, of the normal family of the iterates and of the repelling periodic points is Part IV's, in *The Geometry of the Julia Sets* and *The Julia Sets of a Complex Polynomial*, and is not repeated here.

## The Symmetries

### Equivariance of the Family

The **inner automorphisms** of $\mathbb{H}$ are the maps $\operatorname{Ad}_u(\tilde q)=u\tilde q u^{-1}$ for $u \in \mathbb{H}^{\times}$; they are the whole automorphism group of the algebra over $\mathbb{R}$, and they act on the vector subspace by the rotation group of $S^2$, so that $\operatorname{Ad}_u=\operatorname{Ad}_{u/|u|}$ depends only on the class of $u$ in $S^3/\{\pm1\}\cong SO(3)$.

**Proposition (equivariance).** For every unit quaternion $u$ and every parameter $c$,

$$
f_{\operatorname{Ad}_u(c)} \circ \operatorname{Ad}_u = \operatorname{Ad}_u \circ f_c .
$$

Consequently $K_{\operatorname{Ad}_u(c)}=\operatorname{Ad}_u(K_c)$ and $J_{\operatorname{Ad}_u(c)}=\operatorname{Ad}_u(J_c)$.

*Proof.* An automorphism of an associative algebra preserves products, so $\operatorname{Ad}_u(\tilde q^2)=(\operatorname{Ad}_u\tilde q)^2$; adding $\operatorname{Ad}_u(c)$ gives the identity. The inner automorphism $\operatorname{Ad}_u$ is a real-linear isometry of $\mathbb{H}$ with the Euclidean norm, so it carries bounded orbits to bounded orbits and commutes with the boundary. $\square$

**Remark.** The automorphisms are those of *Quaternion Automorphisms and Derivations*, and the realisation by the unit sphere is that of *Quaternion Rotations and Reflections*. The equivariance is the statement that the family is a single dynamical object read in a rotating frame: **the Julia set depends on the parameter only through the orbit of $c$ under $SO(3)$**, so the parameter space is effectively the quotient of $\mathbb{H}$ by the rotations.

### The Stabiliser and the Real Parameters

**Definition.** The **symmetry group** of a single member $f_c$ is the stabiliser of $c$ in the automorphism group,

$$
G_c = \{u \in S^3 : \operatorname{Ad}_u(c)=c\} /\{\pm1\} \leq SO(3) .
$$

**Proposition (stabiliser).** If $c \in \mathbb{R}$ then $G_c=SO(3)$; if $\mathbf c \neq 0$ then $G_c$ is the circle of rotations about the axis $\mathbb{R}\mathbf c$, isomorphic to $SO(2)$.

*Proof.* An inner automorphism fixes $c$ exactly when $u$ commutes with $c$. The centraliser of a real number is the whole algebra, giving $SO(3)$. If $\mathbf c\neq0$ then $c$ generates, with $e_0$, a two-dimensional subalgebra whose commutant is the two-dimensional plane spanned by $e_0$ and $\mathbf c$; the unit quaternions in that commutant form the circle $\{u=\cos t + (\mathbf c/|\mathbf c|)\sin t\}$, whose image in $SO(3)$ is the circle of rotations about the axis $\mathbf c$. $\square$

**Corollary.** For a real parameter $c$ the map $f_c$ commutes with every inner automorphism and with the conjugation; **the filled Julia set $K_c$ and the Julia set $J_c$ are then fully symmetric about the real axis**, their symmetry group acting on the vector subspace being generated by the rotations and the conjugation and equal to the full orthogonal group $O(3)$.

*Proof.* The commutation with all inner automorphisms is the proposition at $\mathbf c=0$. The conjugation is an anti-automorphism and fixes every real number, so $f_c(\tilde q^{\natural})=(f_c(\tilde q))^{\natural}$; an anti-automorphism is a Euclidean isometry of $\mathbb{H}$, so it too carries $K_c$ to itself. $\square$

**Remark (the orthogonal group).** An anti-automorphism $\rho$ of $\mathbb{H}$ reverses products, $\rho(\tilde a\tilde b)=\rho(\tilde b)\rho(\tilde a)$, and therefore still satisfies $\rho(\tilde q^2)=\rho(\tilde q)^2$; hence it commutes with $f_c$ whenever it fixes $c$, exactly as an automorphism does. The full symmetry of $K_c$ is thus generated by the automorphisms and the anti-automorphisms that fix $c$, and it is $O(3)$ for a real parameter and $O(2)$ for a non-real one, the rotations of the proposition being the identity component. The article uses the automorphism group for the equivariance because it acts on the parameter, and it records the reflections here because they are used in the slice theory of *The Slices of the Quaternion Julia Sets*.

**Remark (the sphere of the imaginary units).** The unit imaginary quaternions form the sphere $S^2$, and conjugation by the unit sphere $S^3$ acts on it by the rotation group, with kernel $\{\pm1\}$. **The symmetry group of the family is therefore the group $SO(3)$ of the sphere of the imaginary units**, realised by the double cover $S^3 \to SO(3)$; for a general parameter the effective symmetry of one member is the stabiliser $G_c$, and only the real parameters enjoy the full group. The phrase "the sphere of the imaginary units" records the double cover and not a three-sphere of symmetries: the acting object is $S^3$, and it acts on $S^2$ through its quotient.

### The Conjugation

**Remark.** When $c$ is real, the conjugation ${}^{\natural}$ is an additional symmetry, not an inner automorphism: it is an anti-automorphism, and it reverses the direction of the vector part. Its fixed set is the real axis and its anti-fixed set the vector subspace, and it commutes with $f_c$ for real $c$. For a non-real parameter the map $f_c$ is not conjugation-equivariant, and the group of symmetries is the circle $G_c$.

## The Slices

### The Complex Planes Through the Origin

**Definition.** For a unit imaginary quaternion $\nu \in S^2$, the **complex plane of the axis $\nu$** is

$$
\mathbb{C}_\nu = \operatorname{span}\{e_0,\nu\} = \{a+b\nu : a,b \in \mathbb{R}\} .
$$

**Proposition.** For each $\nu \in S^2$ the plane $\mathbb{C}_\nu$ is a subalgebra of $\mathbb{H}$ isomorphic to $\mathbb{C}$, and the planes are permuted transitively by the automorphism group; every quaternion lies in at least one of them, and a quaternion with nonzero vector part lies in exactly one, namely $\mathbb{C}_{\hat{\mathbf q}}$ with $\hat{\mathbf q}=\mathbf q/|\mathbf q|$.

*Proof.* Since $\nu^2=-e_0$, the span of $e_0$ and $\nu$ is closed under multiplication and is a two-dimensional real division algebra, hence isomorphic to $\mathbb{C}$ by the Frobenius classification quoted in *Quaternion Algebra*. The automorphism $\operatorname{Ad}_u$ carries $\nu$ to the rotation of $\nu$ by $u$; the group $SO(3)$ acts transitively on $S^2$, hence on the planes. A quaternion $a+\mathbf q$ with $\mathbf q\ne0$ lies in $\mathbb{C}_\nu$ exactly when $\mathbf q \in \mathbb{R}\nu$, so the axis is determined; a real quaternion lies in every plane. $\square$

### The Slice Invariant Under the Map

**Proposition (the parameter's plane).** Put $\mathbb{C}_c=\operatorname{span}\{e_0,c\}$ if $c \notin \mathbb{R}$, and $\mathbb{C}_c=\mathbb{R}$ if $c \in \mathbb{R}$. Then $\mathbb{C}_c$ is a subalgebra and $f_c(\mathbb{C}_c) \subseteq \mathbb{C}_c$. In particular the whole critical orbit lies in $\mathbb{C}_c$.

*Proof.* The span of $e_0$ and $c$ is closed under multiplication because $c^2=2c_0c-N(c)e_0$ by *Quaternion Norm and Invertibility*, and $c$ lies in it; if $\tilde q \in \mathbb{C}_c$ then $\tilde q^2 \in \mathbb{C}_c$ and adding $c$ keeps the point in $\mathbb{C}_c$. The critical orbit starts at $0 \in \mathbb{C}_c$ and $f_c(0)=c \in \mathbb{C}_c$, so it stays there. $\square$

**Remark (the slice discipline).** The plane $\mathbb{C}_c$ is the unique slice that contains the critical orbit; every other choice of plane cuts the four-dimensional set in a different way, and a statement about a slice is a statement about that slice and not about the algebra. **Every picture of a quaternion Julia set below the article is a picture of a slice, and the slice is named with the picture.** The recovery of the whole set from one slice is the theorem of *The Slices of the Quaternion Julia Sets*.

### The Rotational Hull of a Real Parameter

**Theorem (the hull of a real parameter).** Let $c \in \mathbb{R}$ and let $\nu \in S^2$. Then

$$
K_c = \operatorname{Ad}_{S^3}\bigl(K_c \cap \mathbb{C}_\nu\bigr) , \qquad J_c = \operatorname{Ad}_{S^3}\bigl(J_c \cap \mathbb{C}_\nu\bigr) ,
$$

and the intersection $K_c \cap \mathbb{C}_\nu$ is the filled Julia set of the complex quadratic map $z \mapsto z^2+c$ under the isomorphism $\mathbb{C}_\nu \cong \mathbb{C}$ that sends $\nu$ to $i$. Thus **for a real parameter the quaternion Julia set is the rotational hull of the ordinary complex Julia set**.

*Proof.* By the corollary above, $K_c$ is invariant under every inner automorphism. Every quaternion $a+\mathbf q$ with $\mathbf q\ne0$ equals $\operatorname{Ad}_u(a+|\mathbf q|\nu)$ for some $u \in S^3$, since $SO(3)$ is transitive on the sphere of radius $|\mathbf q|$ in the vector subspace; a real quaternion is fixed, and it lies in $\mathbb{C}_\nu$. Hence $K_c \subseteq \operatorname{Ad}_{S^3}(K_c\cap\mathbb{C}_\nu)$, and the reverse inclusion is the invariance. The same argument applies to $J_c=\partial K_c$ because an automorphism is a homeomorphism. Finally, on $\mathbb{C}_\nu$ the map $a+b\nu \mapsto a+bi$ is an algebra isomorphism onto $\mathbb{C}$, and $f_c$ restricts to $z \mapsto z^2+c$; the orbit stays in the slice by the proposition, and the intersection is exactly the filled Julia set of that complex map. The Julia set is its boundary in each case. $\square$

**Remark.** The hull theorem is stated for a real parameter because that is the case in which the full group $SO(3)$ acts; it is the structural reason a four-dimensional set is drawn from a two-dimensional computation, and it is used in *The Slices of the Quaternion Julia Sets* and in *The Dimension of the Quaternion Julia Sets*. For a non-real parameter only the circle $G_c$ acts, and the naive hull statement fails; the precise statement for general parameters is in *The Slices of the Quaternion Julia Sets*, where it is given as the equivariance it is.

## Worked Example

**Example (the first orbits of three parameters).** The computations below are the ones a reader can repeat by hand from the multiplication table, and they are the numerical check recorded in the companion file.

**(a) A real parameter, $c=-1$.** The critical orbit is $0 \mapsto -1 \mapsto 0 \mapsto -1 \mapsto \cdots$, a two-cycle, so $c=-1$ lies in the connectedness locus and the critical orbit is bounded. The point $\tilde q = e_0+e_1$ has orbit $e_0+e_1 \mapsto -e_0+2e_1 \mapsto -4e_0-4e_1 \mapsto -e_0+32e_1 \mapsto \ldots$, so $e_0+e_1$ escapes and is not in the filled Julia set.

**(b) A purely imaginary parameter, $c=e_1$.** The critical orbit is

$$
0 \mapsto e_1 \mapsto -e_0+e_1 \mapsto -e_1 \mapsto -e_0+e_1 \mapsto \cdots ,
$$

so it enters the two-cycle $\{-e_0+e_1,-e_1\}$ and $c=e_1$ lies in the connectedness locus. The plane $\mathbb{C}_{e_1}=\operatorname{span}\{e_0,e_1\}$ is invariant, and the critical orbit is the complex orbit of $z \mapsto z^2+i$.

**(c) A parameter outside the locus, $c=e_0$.** The critical orbit is $0 \mapsto e_0 \mapsto 2e_0 \mapsto 5e_0 \mapsto 26e_0 \mapsto \ldots$, which escapes: $c=1$ is not in the quaternion Mandelbrot set, and the escape begins at the second iterate.

**(d) The rotation of a parameter.** The parameters $c=e_1$, $c=e_2$ and $c=e_3$ all have modulus $1$, and $\operatorname{Ad}_u(e_1)=e_2$ for the unit quaternion $u=(e_1+e_2)/\sqrt2$; by equivariance their filled Julia sets are rotations of one another, and their membership in the connectedness locus is the same.

## Summary

The quaternion quadratic map is $f_c(\tilde q)=\tilde q^2+c$, a degree-two polynomial map of $\mathbb{R}^4$ whose differential at $\tilde q$ is the sum of the left and right multiplications, singular exactly on the hyperplane of the pure vectors and with determinant $16q_0^2|\tilde q|^2$, and whose critical orbit is the orbit of the point $0$. A point whose modulus reaches $R(c)=1+|c|$ escapes, by the multiplicativity of the quaternion norm and the triangle inequality, so the filled Julia set $K_c$ is the compact set of points whose orbit never leaves the closed ball of radius $R(c)$, and the Julia set is $J_c=\partial K_c$. Both are nonempty and compact, and $J_c=K_c$ when $K_c$ has empty interior.

The automorphism group of $\mathbb{H}$ is the inner automorphism group $SO(3)=S^3/\{\pm1\}$, and the family is equivariant, $f_{\operatorname{Ad}_u c}\circ\operatorname{Ad}_u=\operatorname{Ad}_u\circ f_c$, so the Julia set depends on $c$ only through its rotational orbit. The stabiliser of $c$ is the whole group for a real parameter and the circle of rotations about the axis $\mathbf c$ otherwise; for a real parameter the map commutes with every automorphism and with the conjugation, and $J_c$ is fully rotationally symmetric. Every unit imaginary quaternion $\nu$ spans with $e_0$ a plane $\mathbb{C}_\nu$ isomorphic to $\mathbb{C}$; the plane $\mathbb{C}_c$ of the parameter is invariant and carries the whole critical orbit; and for a real parameter the quaternion Julia set is the rotational hull of the ordinary complex Julia set, the general recovery from a slice being the theorem of *The Slices of the Quaternion Julia Sets*. The escape radius and the Green's function are the subject of *The Escape Radius and the Green's Function for Quaternions*; the connectedness locus is that of *The Quaternion Mandelbrot Set*; and the dimension is that of *The Dimension of the Quaternion Julia Sets*. The general theory of the Fatou and Julia sets is Part IV's, in *The Geometry of the Julia Sets*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde q = q_0e_0+q_1e_1+q_2e_2+q_3e_3$ | A quaternion, scalar part $q_0$, vector part $\mathbf q$ |
| $\tilde q^{\natural}$, $N(\tilde q)$, $\lvert\tilde q\rvert$ | Conjugate; norm $q_0^2+q_1^2+q_2^2+q_3^2$; modulus $\sqrt N$ |
| $f_c(\tilde q)=\tilde q^2+c$ | The quaternion quadratic map |
| $\tilde q_n=f_c^{\,n}(\tilde q)$ | The orbit of $\tilde q$ |
| $R(c)=1+\lvert c\rvert$ | Escape radius: $\lvert\tilde q_n\rvert \geq R$ implies escape |
| $K_c$, $J_c=\partial K_c$ | Filled Julia set; Julia set |
| $\operatorname{Ad}_u(\tilde q)=u\tilde q u^{-1}$ | Inner automorphism, $u \in S^3/\{\pm1\}=SO(3)$ |
| $G_c$ | Stabiliser of $c$; $SO(3)$ if $c$ real, $SO(2)$ otherwise |
| $S^3$, $S^2$ | Unit quaternions; unit imaginary quaternions |
| $\mathbb{C}_\nu=\operatorname{span}\{e_0,\nu\}$ | Complex plane of the axis $\nu$, $\cong \mathbb{C}$ |
| $\mathbb{C}_c$ | The invariant plane of the parameter, carrying the critical orbit |

## Further Reading

- Gaston Julia, "Mémoire sur l'itération des fonctions rationnelles", *Journal de Mathématiques Pures et Appliquées* 8 (1918), 47–245. The original theory of the Julia set, in the complex case.
- Benoit B. Mandelbrot, *The Fractal Geometry of Nature* (Freeman, 1982). The quadratic family and the Mandelbrot set, and the dimension as the definition of a fractal.
- John Milnor, *Dynamics in One Complex Variable*, 3rd ed. (Princeton, 2006). The complex quadratic family, the filled Julia set and the dichotomy, which the quaternion family restricts to its slices.
- Paul J. Gomatam, Jay S. Doyle, Gy. Lakner and others, "Generalized Mandelbrot set in quaternion space", *Advances in Applied Clifford Algebras* (2006). The critical slice and the reduction of the quaternion connectedness locus to the complex one.
- Kenneth Falconer, *Fractal Geometry: Mathematical Foundations and Applications*, 3rd ed. (Wiley, 2014). The dimensions and the coverings, cited to *Fractal Geometry*.

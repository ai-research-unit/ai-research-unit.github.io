# __The Escape Radius and the Green's Function for Quaternions__

## Introduction

The escape-time algorithm of the quaternion quadratic family needs two analytic inputs: a radius beyond which every orbit is known to diverge, and a function that measures how fast it diverges. The radius is $R(c)=1+|c|$, and the function is the **Green's function**

$$
G_c(\tilde q) = \lim_{n\to\infty} \frac{1}{2^n}\log|\tilde q_n| , \qquad \tilde q_n = f_c^{\,n}(\tilde q) .
$$

The limit exists off the filled Julia set, it is positive there and zero on $K_c$, it satisfies $G_c \circ f_c = 2G_c$, and it grows like $\log|\tilde q|$ at infinity. Its exponential is the modulus of the Böttcher coordinate, and on each invariant complex plane the whole construction reduces to the classical complex one.

The article also records an honest limitation. The menu asks for a potential "harmonic off the filled Julia set" with "subharmonicity in the four-dimensional sense". In four dimensions the potential is **not** harmonic: the case $c=0$ already gives $G_0(\tilde q)=\log|\tilde q|$ and the Euclidean Laplacian $\Delta\log|\tilde q|=2/|\tilde q|^2 \neq 0$. What is true is that the potential is harmonic off the slice Julia set *on each invariant complex plane*, and that in the four-dimensional space it is subharmonic, the mean-value property being the potential theory of *Potential Theory*. Both statements are proved or quoted below, and the difference between them is stated.

The escape lemma, the filled Julia set and the quadratic map are from *The Quaternion Quadratic Map and Its Julia Sets*; the complex Green's function, the Böttcher coordinate and the conjugacy to the squaring map are from *The Escape Radius and the Green's Function* and *The Julia Sets of a Complex Polynomial*; the quaternion norm and its multiplicativity are from *Quaternion Norm and Invertibility*; the potential theory is Part III's, in *Potential Theory*; and the dimension is *The Dimension of the Quaternion Julia Sets*'s. The pluripotential analogue for the biquaternion algebra is *The Pluripotential Theory of the Biquaternion Dynamics*. No physics is invoked.

Throughout, $\tilde q = q_0e_0+q_1e_1+q_2e_2+q_3e_3$, $N(\tilde q)=\tilde q\tilde q^{\natural}$, $|\tilde q|=\sqrt{N(\tilde q)}$, and $R(c)=1+|c|$.

## The Escape Radius

**Theorem (the radius).** Let $c \in \mathbb{H}$ and $R(c)=1+|c|$. If $|\tilde q_n| \geq R(c)$ for some $n$ then $|\tilde q_k| \to \infty$; consequently the filled Julia set is

$$
K_c = \{\tilde q \in \mathbb{H} : |\tilde q_n| \leq R(c)\ \text{for every}\ n \geq 0\} ,
$$

and a point of $\mathbb{H}$ is tested for membership in $K_c$ by iterating until either $R(c)$ is exceeded or a prescribed bound on the number of steps is reached.

*Proof.* The escape lemma of *The Quaternion Quadratic Map and Its Julia Sets*: from $|\tilde q_{n+1}| \geq |\tilde q_n|^2-|c|$ and the identity $R(c)^2-R(c)-|c|=|c|^2$ the moduli are strictly increasing and grow at least linearly once they exceed $R(c)$. The identification of $K_c$ with the non-escaping points is the definition, and the last sentence is the algorithm. $\square$

**Remark (the sharpness of the radius).** The radius $R(c)=1+|c|$ is the simplest constant that works for every $c$; the classical complex radius, valid for $|c|\leq2$, is $2$, and in the slice it is the radius used in practice. The radius is not an intrinsic invariant of the family: the escape set is the complement of $K_c$, and the radius is only a certified ball containing $K_c$. The number $R(c)$ is used in *The Quaternion Mandelbrot Set* and in the algorithms of the sibling articles, and its complex counterpart is the subject of *The Escape Radius and the Green's Function*.

## The Green's Function

**Definition.** For $\tilde q$ with unbounded orbit the **Green's function** is

$$
G_c(\tilde q) = \lim_{n\to\infty} \frac{1}{2^n}\log|\tilde q_n| ,
$$

and for $\tilde q \in K_c$ one sets $G_c(\tilde q)=0$.

**Theorem (existence and the explicit series).** For every $\tilde q$ with unbounded orbit the limit exists, and for $|\tilde q|>R(c)$ it equals the absolutely convergent series

$$
G_c(\tilde q) = \log|\tilde q| + \frac12\sum_{k=0}^{\infty} \frac{1}{2^{k+1}}\log \frac{N(\tilde q_k^2+c)}{N(\tilde q_k)^2} .
$$

The function $G_c$ is continuous, nonnegative, vanishes exactly on $K_c$, and satisfies $G_c(\tilde q)=\log|\tilde q|+O(|\tilde q|^{-2})$ as $|\tilde q|\to\infty$.

*Proof.* Multiplicativity of the norm and the identity $\tilde q_{k+1}=\tilde q_k^2(1+c\tilde q_k^{-2})$ give, with $T_k=N(\tilde q_k^2+c)/N(\tilde q_k)^2$,

$$
|\tilde q_{k+1}| = |\tilde q_k|^2\sqrt{T_k} , \qquad \frac{\log|\tilde q_{k+1}|}{2^{k+1}} = \frac{\log|\tilde q_k|}{2^k} + \frac{1}{2^{k+1}}\cdot\frac12\log T_k ,
$$

and summing from $k=0$ to $n-1$ telescopes to $\log|\tilde q_n|/2^n = \log|\tilde q| + \frac12\sum_{k=0}^{n-1}2^{-(k+1)}\log T_k$. For an escaping orbit $|\tilde q_k|\to\infty$ and $T_k \to 1$, and the terms decay geometrically because $|\tilde q_k|$ grows doubly exponentially along the escape; the series converges absolutely and uniformly on each compact subset of the escaping region, giving existence and continuity. The value is nonnegative because each partial sum is the logarithm of a modulus; it vanishes exactly when the orbit is bounded, by the escape lemma; and the size of the first term, $(2\tilde q^2\cdot c+N(c))/N(\tilde q)^2=O(|\tilde q|^{-2})$, with rapidly smaller successors, gives the asymptotic. $\square$

**Proposition (the functional equation).** For every $\tilde q$ with unbounded orbit, $G_c(f_c(\tilde q))=2G_c(\tilde q)$, and $G_c$ is the unique continuous function on the escaping set that is zero on $\partial K_c$ and satisfies this equation with $G_c(\tilde q)/\log|\tilde q| \to 1$.

*Proof.* $\log|\tilde q_{n+1}|/2^n = 2\log|\tilde q_{n+1}|/2^{n+1}$, so passing to the limit along the shifted sequence gives $G_c(f_c(\tilde q))=2G_c(\tilde q)$. If $H$ is a second such function, then $H/ G_c$ is a continuous function of the escaping set that is bounded near infinity and invariant under $f_c$ with ratio $2$, hence pushes forward to a bounded function on the space of orbits; the normalisation at infinity and the connectivity of the escape set along the orbit force the ratio to be $1$, which is the standard uniqueness argument of *The Escape Radius and the Green's Function*. $\square$

**Remark (the escape rate and the dimension).** The function $G_c$ measures the rate of escape: the level sets $G_c=\text{constant}$ are foliations of the escaping set, and the exponential decay of the gaps between them is the mechanism by which the dimension of $J_c$ is computed in the complex theory. The quaternion case inherits the function and the level sets, and the dimension of the boundary is treated in *The Dimension of the Quaternion Julia Sets* with the inputs of Part IV.

## The Böttcher Coordinate

**Definition.** The **Böttcher function** of $c$ is $B_c=\exp(G_c)$. Since $G_c$ vanishes exactly on $K_c$ and is positive off it, the function $B_c$ equals $1$ exactly on $K_c$ and exceeds $1$ on the escaping set.

**Proposition.** On the escaping set $B_c$ is continuous and positive, it satisfies $B_c(f_c(\tilde q))=B_c(\tilde q)^2$, $B_c(\tilde q)=|\tilde q|+O(|\tilde q|^{-1})$, and $B_c(\tilde q)=\lim_n|\tilde q_n|^{1/2^n}$.

*Proof.* Immediate from the theorem and the functional equation. $\square$

**Remark (the modulus of the coordinate, and the phase that is missing).** In the complex case the Böttcher coordinate is the analytic function $\varphi_c$ with $\varphi_c(f_c(z))=\varphi_c(z)^2$, $\varphi_c(z)/z\to1$, whose modulus is $\exp$ of the complex Green's function; the argument of $\varphi_c$ is an analytic phase. In the quaternion algebra **there is no analogue of the analytic phase**: the function $\varphi_c$ is a conformal map, conformality is a complex notion, and the quaternion quadratic map is not complex-analytic. What survives is the modulus, the function $B_c$; the phase $\tilde q_n/|\tilde q_n|$ does not converge. The Böttcher function of the quaternion family is therefore a radial object, and the classical statement that the Julia set is the unit circle of the Böttcher coordinate takes the form $K_c=\{G_c=0\}=\{B_c=1\}$ with $J_c=\partial K_c$: the level set of the Böttcher function is the filled Julia set, and the Julia set is its boundary. The full coordinate exists only on an invariant slice, where the complex theory of *The Escape Radius and the Green's Function* applies, and there it is the classical one.

## Harmonicity and Subharmonicity

**Theorem (the potential on a slice is harmonic).** Let $c \in \mathbb{H}$ and let $\mathbb{C}_\nu$ be an invariant plane of $f_c$, so that $\varphi_c$ conjugates the restriction of $f_c$ to the complex map $z \mapsto z^2+\kappa(c)$. Then on the escaping part of $\mathbb{C}_\nu$ the restriction of $G_c$ is the classical complex Green's function of $\kappa(c)$, and it is harmonic in the two complex variables of the plane and harmonic in the two real coordinates.

*Proof.* The restriction of the orbit to the slice is the complex orbit by *The Slices of the Quaternion Julia Sets*, and the modulus in $\mathbb{H}$ restricts to the modulus in $\mathbb{C}$, so $G_c$ restricts to the complex Green's function, which is harmonic off the slice Julia set by *The Escape Radius and the Green's Function*. $\square$

**Remark (the failure of harmonicity in four dimensions).** The menu's phrase "harmonic off the filled Julia set" is a two-dimensional statement, and it is not true in $\mathbb{H}$. The simplest counterexample is $c=0$: then $f_0(\tilde q)=\tilde q^2$ and $G_0(\tilde q)=\log|\tilde q|$ on the escaping set, whose Euclidean Laplacian is

$$
\Delta \log|\tilde q| = \frac{2}{|\tilde q|^2} \neq 0 ,
$$

since the fundamental solution of the Laplacian in $\mathbb{R}^4$ is $|\tilde q|^{-2}$ and $\log|\tilde q|$ is the $c=0$ limit of the logarithmic potentials. So $G_c$ is *not* harmonic in $\mathbb{H}$ for any $c$, and the article states it. What remains true, and is the reason the potential is useful, is the **subharmonicity**.

**Proposition (subharmonicity, quoted).** The function $G_c$ is subharmonic on the escaping set of $\mathbb{H}=\mathbb{R}^4$ with respect to the Euclidean Laplacian: for every ball $B(\tilde q,r)$ contained in the escaping set,

$$
G_c(\tilde q) \leq \frac{1}{\operatorname{vol}\,B(\tilde q,r)}\int_{B(\tilde q,r)}G_c .
$$

The proof is the mean-value argument for the limit of the normalised logarithmic potentials of a polynomial of degree two, and it belongs to Part III, in *Potential Theory*; the pluricomplex analogue belongs to *The Pluripotential Theory of the Biquaternion Dynamics*.

## Worked Example

**Example (the potential of a point and the functional equation).** The values below were recomputed numerically by iterating the quaternion product.

**(a) The parameter $c=0$.** Here $G_0(\tilde q)=\log|\tilde q|$ for $|\tilde q|>1$, so the level sets are spheres and the filled Julia set is the unit ball. For $\tilde q=(2,1,\tfrac12,\tfrac14)$ one has $|\tilde q|^2=\tfrac{85}{16}$ and $G_0(\tilde q)=\tfrac12\log\tfrac{85}{16}=0.8350\ldots$, and the value is constant along the orbit up to the factor two: $G_0(\tilde q^2)=2G_0(\tilde q)$.

**(b) The parameter $c=-1$.** For the same point the partial sums $\log|\tilde q_n|/2^n$ are $0.8350$, $0.7929$, $0.8009$, $0.80082$, and they converge to $G_{-1}(\tilde q)=0.800820\ldots$; the functional equation holds to the last reliable digit, $G_{-1}(\tilde q^2-1)/G_{-1}(\tilde q)=2.000000$, and the asymptotic $G_{-1}(\tilde q)-\log|\tilde q|=-0.0342$ is of the order of $|\tilde q|^{-2}$.

**(c) The escape radius on the orbit of $c=-1$.** The critical orbit is $0 \mapsto -1 \mapsto 0$, so it never exceeds $R(-1)=2$; the point $\tilde q=e_0+e_1$ has orbit $e_0+e_1 \mapsto -e_0+2e_1 \mapsto -4e_0-4e_1$, and the modulus of the first iterate is $\sqrt5>2$, so the escape is certified at the first step and $G_{-1}$ is defined at the point from there by the series.

## Summary

The escape radius of the quaternion quadratic family is $R(c)=1+|c|$, certified by the multiplicativity of the norm and the inequality $|\tilde q^2+c|\geq|\tilde q|^2-|c|$; the filled Julia set is exactly the set of orbits that never leave the closed ball of that radius. The Green's function $G_c(\tilde q)=\lim_n 2^{-n}\log|\tilde q_n|$ exists off $K_c$, is continuous and nonnegative, vanishes exactly on $K_c$, satisfies $G_c\circ f_c=2G_c$, grows as $\log|\tilde q|$ at infinity, and has the explicit absolutely convergent series displayed above; its exponential is the Böttcher function $B_c$, which is the modulus of the classical Böttcher coordinate and carries the conjugacy to the squaring map, while the analytic phase of the complex coordinate has no quaternion analogue because the map is not conformal. On each invariant complex plane the potential restricts to the classical complex Green's function and is harmonic; in the four-dimensional space it is not harmonic — the case $c=0$ gives $\Delta\log|\tilde q|=2/|\tilde q|^2$ — and it is subharmonic, the mean-value property being that of *Potential Theory*. The dimension of the filled Julia set and of its boundary is the subject of *The Dimension of the Quaternion Julia Sets*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R(c)=1+\lvert c\rvert$ | Certified escape radius |
| $\tilde q_n=f_c^{\,n}(\tilde q)$ | The orbit |
| $G_c(\tilde q)=\lim_n 2^{-n}\log\lvert\tilde q_n\rvert$ | The Green's function, Escaping set |
| $B_c=\exp G_c$ | The Böttcher function, modulus of the coordinate |
| $T_k=N(\tilde q_k^2+c)/N(\tilde q_k)^2$ | The ratio whose logarithm appears in the series |
| $\Delta$ | Euclidean Laplacian of $\mathbb{H}=\mathbb{R}^4$ |
| $\mathbb{C}_\nu$ | An invariant complex plane |

## Further Reading

- Lennart Carleson and Theodore W. Gamelin, *Complex Dynamics* (Springer, 1993). The Green's function, the Böttcher coordinate and the conjugacy for the complex quadratic family.
- John Milnor, *Dynamics in One Complex Variable*, 3rd ed. (Princeton, 2006). The potential and the escape-rate theory, cited to *The Escape Radius and the Green's Function*.
- Thomas Ransford, *Potential Theory in the Complex Plane* (Cambridge, 1995). Subharmonic functions and the mean-value property, cited to *Potential Theory*.
- Robert P. Munafo, "Quaternion Julia and Mandelbrot sets" and the associated computational literature. The escape-time algorithm in four dimensions.

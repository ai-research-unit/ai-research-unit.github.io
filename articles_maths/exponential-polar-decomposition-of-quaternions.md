# __Exponential Polar Decomposition of Quaternions__

## Introduction

This article treats the **exponential polar decomposition** of a nonzero quaternion: the writing

$$
\tilde q=\exp(\tilde q_{\log}), \qquad \tilde q_{\log}=\ln r+\vec v,
$$

$$
\tilde q_{\log}=q_{\log}e_t+\vec q_{\log}, \qquad q_{\log}=\operatorname{Sc}\tilde q_{\log}=\ln r, \quad \vec q_{\log}=\operatorname{Vect}\tilde q_{\log}=\vec v,
$$

with $r>0$ the modulus, $\vec v$ the pure exponent, $q_{\log}$ the logarithmic scale, and $\vec q_{\log}$ the vector coordinate, the angle and the axis. The product of the scale and the rotor is $r\exp(\vec q_{\log})$. The exponential and the logarithm are defined and studied in *Quaternion Special Functions*, §*The Quaternion Exponential* and §*The Quaternion Logarithm*; this article does not define them again. It uses the closed form and the description of the logarithms from that article.

The decomposition is the exponential form of the modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Quaternions*, which writes every nonzero quaternion as

$$
\tilde q = r\,\tilde u_{\mathrm r}, \qquad r \in \mathbb{R}, \quad r>0, \qquad \tilde u_{\mathrm r}\in\mathbb{H}, \quad \langle\tilde u_{\mathrm r}\rangle_{\natural}=1,
$$

with $r$ the modulus and $\tilde u_{\mathrm r}$ the unit factor. That writing is quoted here in the same form because it is used outside this category, in *Rational-Chart Polar Decomposition of Quaternions* and in the biquaternion articles, so the symbols must agree. The unit factor is written $\tilde u_{\mathrm r}=\exp(\vec v)=\cos\theta+\vec n\sin\theta$, the rotor of the decomposition. The rational-chart form of *Rational-Chart Polar Decomposition of Quaternions* is the third presentation. The amalgamation into one exponential survives because the logarithmic scale is real and central. What does not survive is the reading of the exponent as a group coordinate: the exponential is not a homomorphism, and its kernel is not a subgroup.

The article states the decomposition and computes its data (§*The Decomposition*), identifies the exponent with the logarithm and separates the principal logarithm from the general one (§*The Logarithm*), proves existence and uniqueness (§*Existence and Uniqueness*), gives examples (§*Worked Examples*), and then treats the matrix picture (§*The Matrix Picture*), the comparison with the two other polar forms (§*The Three Polar Decompositions*) and the exponential coordinates (§*The Exponential Coordinates*).

The symbols are those of *Quaternion Algebra*, *Norm and Invertibility in the Quaternion Algebra* and *Conventions in Mathematics*. The modulus is written through the algebraic norm, $r=\sqrt{\langle\tilde q\rangle_{\natural}}$, and the modulus of a pure element through $\sqrt{\langle\vec v\rangle_{\natural}}$; a pure element carries the arrow. Every numerical value displayed below was recomputed in double precision.

## The Decomposition

### The Data

Let $\tilde q=q_te_t+\vec q\neq0$, with $\vec q$ the vector part. The **modulus** and the **principal angle** are

$$
r=\sqrt{\langle\tilde q\rangle_{\natural}}>0, \qquad
\theta=\arccos\frac{q_t}{r}\in[0,\pi],
$$

and the **axis** is the unit pure quaternion

$$
\vec n=\frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}}
$$

when $\vec q\neq0$. Euler's formula, $\exp(\theta\vec n)=\cos\theta+\vec n\sin\theta$, and $r=\exp(\ln r)$ give

$$ \boxed{\; \tilde q=r(\cos\theta+\vec n\sin\theta)=r\exp(\theta\vec n)=\exp(\tilde q_{\log}),
\qquad \tilde q_{\log}=\ln r+\theta\vec n \;} .$$

The three expressions are the same number. The middle one is the modulus–unit form; the last one is the exponential polar decomposition. The identity $\cos\theta=q_t/r$ follows from the definition of $\theta$, and $\sin\theta=\sqrt{\langle\vec q\rangle_{\natural}}/r$ follows from $\langle\tilde q\rangle_{\natural}=q_t^2+\langle\vec q\rangle_{\natural}$. At $\vec q=0$ the product $\vec n\sin\theta$ is read as $0$.

**Definition.** An **exponential polar decomposition** of $\tilde q\in\mathbb{H}^{\times}$ is a writing

$$
\tilde q=\exp(\tilde q_{\log}), \qquad \tilde q_{\log}=\ln r+\vec v, \quad r>0,\quad \vec v\in\operatorname{Im}\mathbb{H},
$$

equivalently $\tilde q=\exp(\ln r)\exp(\vec v)$, in which $\exp(\ln r)=r$ is the **scale** and $\exp(\vec v)$ is the **unit factor**, the rotor. The **exponent** is the logarithm $\tilde q_{\log}$, with scalar coordinate $q_{\log}=\ln r$ and vector coordinate $\vec q_{\log}=\vec v$.

Write $\vec v=\theta\vec n$ with $\theta=\sqrt{\langle\vec v\rangle_{\natural}}\ge0$ and $\vec n$ a unit pure quaternion when $\vec v\neq0$. The **angle** is $\theta$ and the **axis** is $\vec n$. The angle is defined modulo $2\pi$, because $\exp((\theta+2\pi k)\vec n)=\exp(\theta\vec n)$; the axis is a point of the sphere $S^2$ of unit pure quaternions. The pair $(r,\exp(\vec v))$ is the modulus–unit pair.

### The Two Coordinates

The exponent has one scalar coordinate and one vector coordinate, and they play different roles.

| coordinate | formula from $\tilde q$ | range | role |
|---|---|---|---|
| $q_{\log}=\operatorname{Sc}\tilde q_{\log}$ | $\ln\sqrt{\langle\tilde q\rangle_{\natural}}$ | $\mathbb{R}$ | logarithmic scale $\ln r$; one value, no branch |
| $\vec q_{\log}=\operatorname{Vect}\tilde q_{\log}$ | $\theta\vec n$, with $\theta=\arccos\bigl(q_t/\sqrt{\langle\tilde q\rangle_{\natural}}\bigr)$ and $\vec n=\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ | $\operatorname{Im}\mathbb{H}$ | angle and axis; one line off the real axis, one sphere on it |

The scalar coordinate is unique: it is fixed by the modulus, $q_{\log}=\ln r=\tfrac12\ln\langle\tilde q\rangle_{\natural}$, and carries the scale. The vector coordinate is a pure quaternion, not a scalar: it is the quaternion analogue of the primed coordinate $q'_{\log}$ of the complex case, and it carries both the angle and the axis. The prime is not written, because a quaternion coefficient is real and the prime marks an imaginary coordinate only. At $\vec q=0$ the axis is free: the coordinate is $0$ at $+r$ and $(2k+1)\pi\vec n$ at $-r$.

Read backwards, the pair gives the element:

$$
\tilde q=\exp(q_{\log})\exp(\vec q_{\log})=\sqrt{\langle\tilde q\rangle_{\natural}}\bigl(\cos\theta+\vec n\sin\theta\bigr).
$$

The subscript is a label, not an operation: $q_{\log}$ is the scalar coordinate of $\tilde q_{\log}$, not the logarithm of $q_t$.

### The Two Factors

The factors are read from $\tilde q$ directly:

$$ \boxed{\; \exp(\ln r)=r=\sqrt{\langle\tilde q\rangle_{\natural}}, \qquad
\exp(\vec v)=\frac{\tilde q}{r}=\frac{\tilde q}{\sqrt{\langle\tilde q\rangle_{\natural}}} \;} .$$

The first is positive real; the second has norm one, $\langle\exp(\vec v)\rangle_{\natural}=1$, and lies on the unit sphere $S^3$. They recover the modulus–unit decomposition. The table records the two factors.

| factor | formula | range | coordinate | parameter |
|---|---|---|---|---|
| scale | $\exp(q_{\log})=r$ | $(0,\infty)$ | $q_{\log}=\ln r$ | $r>0$ |
| unit factor (rotor) | $\exp(\vec q_{\log})=\tilde q/r$ | $S^3$ | $\vec q_{\log}=\theta\vec n$ | $\theta\in[0,\pi)$, $\vec n\in S^2$ |

The real dimensions are $1$ and $3$, and they add to the real dimension $4$ of $\mathbb{H}$. The scale is non-compact; the unit factor is compact. This is the compact case of the polar decomposition: the group of units retracts onto the sphere.

### The Rotor Part

The unit factor is a unit real quaternion, and the corpus calls it a **rotor**: it is the rotor part of the decomposition. The symbol is $\tilde u_{\mathrm r}$, the one used in *Modulus–Unit Polar Decomposition of Quaternions* and in the biquaternion articles, where it is the fourth factor of the word. *Conventions in Mathematics* (§*Symbols*) writes a rotor $\tilde u$ when no other unit is in play. In the exponential form it is

$$
\tilde u_{\mathrm r}=\exp(\vec v)=\cos\theta+\vec n\sin\theta, \qquad \langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

A rotor acts on the pure quaternions by the sandwich, and the sandwich by $\tilde u_{\mathrm r}$ is Rodrigues' rotation by $2\theta$:

$$
\tilde u_{\mathrm r}\,\vec x\,\tilde u_{\mathrm r}^{-1}=\vec x\cos 2\theta+(\vec n\times\vec x)\sin 2\theta+\vec n\,(\vec n\cdot\vec x)(1-\cos 2\theta).
$$

The angle $\theta$ of the exponent is the **half-angle** stored in the rotor, and the rotation produced by the sandwich is twice it. The rotor that produces the rotation by $\theta$ itself is $\exp(\tfrac12\vec v)=\cos\tfrac{\theta}{2}+\vec n\sin\tfrac{\theta}{2}$, whose square is $\tilde u_{\mathrm r}$. The biquaternion article stores the rotation angle itself in the exponent of its rotor, so its $\exp(\tfrac{\Theta}{2}\vec u_{\mathrm r})$ has $\Theta=2\theta$ in the notation of this article.

Two consequences follow. The exponent $\vec v$ is not the rotation vector of $\tilde q$: the rotation attached to the element is the sandwich by its unit factor, with angle $2\theta$ about $\vec n$, that is the vector $2\vec v$ read modulo $2\pi$ in the angle. And on the principal chart $\theta\in[0,\pi)$ the rotation angle $2\theta$ runs over $[0,2\pi)$. The two rotors $\pm\tilde u_{\mathrm r}$ give the same rotation, which is the double cover $S^3\to SO(3)$ of *Modulus–Unit Polar Decomposition of Quaternions*.

For $\tilde q=3e_t+4\vec e_x$ the rotor is $\tilde u_{\mathrm r}=0.6e_t+0.8\vec e_x$, and the sandwich by it rotates by $2\theta=1.8545904360$ about $\vec e_x$. The rotor of the rotation by $\theta$ is the square root, $0.8944271910e_t+0.4472135955\vec e_x$.

### One Exponential

The product of the two factors is one exponential:

$$
\tilde q=\exp(\ln r)\exp(\vec v)=\exp(\ln r+\vec v).
$$

The amalgamation uses the fact that $\ln r$ is real and central, so it commutes with $\vec v$. It does not use a group law of the exponential, and the exponential is not a homomorphism. For two pure exponents the failure is explicit. Take $\tilde q_1=\tfrac{\pi}{2}\vec e_x$ and $\tilde q_2=\tfrac{\pi}{2}\vec e_y$. Then

$$
\exp(\tilde q_1)\exp(\tilde q_2)=\vec e_x\vec e_y=\vec e_z,
$$

whereas

$$
\exp(\tilde q_1+\tilde q_2)
=\cos\frac{\pi}{\sqrt2}+\frac{\vec e_x+\vec e_y}{\sqrt2}\sin\frac{\pi}{\sqrt2}
=-0.6056998671+0.5626400586\,(\vec e_x+\vec e_y),
$$

which is not $\vec e_z$. The first obstruction is the commutator $[\vec v_1,\vec v_2]=2\,\vec v_1\times\vec v_2$, and the Baker–Campbell–Hausdorff series begins

$$
\log\bigl(\exp(\tilde q_1)\exp(\tilde q_2)\bigr)
=\tilde q_1+\tilde q_2+\tfrac12[\tilde q_1,\tilde q_2]+\cdots .
$$

The word **polar** names the two factors, not two independent exponentials. The single exponent $\tilde q_{\log}=\ln r+\vec v$ carries both the scale and the rotor. It is not a group coordinate: the product of two elements is not the exponential of the sum of their exponents.

### Existence and Uniqueness

**Theorem.** Every $\tilde q\in\mathbb{H}^{\times}$ has an exponential polar decomposition. The principal one, with $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$, exists exactly on $\mathbb{H}\setminus(-\infty,0]$ and is unique there. The general case is as follows.

- If $\tilde q\notin\mathbb{R}$, then there are unique $r>0$, $\theta\in(0,\pi)$ and $\vec n\in S^2$ with $\tilde q=\exp(\ln r+\theta\vec n)$. Every exponent of $\tilde q$ is $\ln r+(\theta+2\pi k)\vec n$, $k\in\mathbb{Z}$.
- If $\tilde q=r_0e_t$ with $r_0>0$, then $r=r_0$ and the angle is $0$. The exponents are $\ln r_0+2\pi k\,\vec n$ with $k\in\mathbb{Z}_{\ge0}$ and $\vec n\in S^2$, the value $k=0$ giving the principal exponent $\ln r_0$.
- If $\tilde q=-r_0e_t$ with $r_0>0$, then $r=r_0$ and the angle is $\pi$. The exponents are $\ln r_0+(2k+1)\pi\,\vec n$ with $k\in\mathbb{Z}_{\ge0}$ and $\vec n\in S^2$. None has vector part of length below $\pi$, so there is no principal exponent.

**Existence.** Let $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ and $\tilde u_{\mathrm r}=\tilde q/r$, so $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$. If $\tilde u_{\mathrm r}\neq\pm e_t$, write $\tilde u_{\mathrm r}=\cos\theta+\vec n\sin\theta$ with $\theta\in(0,\pi)$ and $\vec n\in S^2$. Then $\exp(\ln r+\theta\vec n)=r\tilde u_{\mathrm r}=\tilde q$. At $\tilde u_{\mathrm r}=e_t$ take $\vec v=0$; at $\tilde u_{\mathrm r}=-e_t$ take $\vec v=\pi\vec n$ for any $\vec n\in S^2$. In both cases $\exp(\vec v)=\tilde u_{\mathrm r}$ and the identity follows.

**Uniqueness.** Suppose $\exp(\ln r_1+\vec v_1)=\exp(\ln r_2+\vec v_2)$. Taking norms gives $r_1=r_2$, because $\langle\exp(\ln r+\vec v)\rangle_{\natural}=r^2$. Hence $\exp(\vec v_1)=\exp(\vec v_2)$. For a non-real element, write the common unit value as $\cos\theta+\vec n\sin\theta$ with $\theta\in(0,\pi)$. The closed form gives

$$
\cos\sqrt{\langle\vec v_j\rangle_{\natural}}=\cos\theta, \qquad
\frac{\vec v_j}{\sqrt{\langle\vec v_j\rangle_{\natural}}}\sin\sqrt{\langle\vec v_j\rangle_{\natural}}=\vec n\sin\theta .
$$

Since $\sin\theta\neq0$, the second equation forces the direction of $\vec v_j$ to be $\pm\vec n$ and $\sin\sqrt{\langle\vec v_j\rangle_{\natural}}$ to have the same sign; hence $\vec v_j=(\theta+2\pi k_j)\vec n$. The bound $\sqrt{\langle\vec v_j\rangle_{\natural}}<\pi$ forces $k_j=0$, so $\vec v_1=\vec v_2$. For a real element the same equations read $\cos\sqrt{\langle\vec v_j\rangle_{\natural}}=\pm1$ and $\sin\sqrt{\langle\vec v_j\rangle_{\natural}}=0$, which gives the two real families above with a free axis.

The data of the principal decomposition are collected in one table.

| datum | formula |
|---|---|
| element | $\tilde q=q_te_t+\vec q\neq0$, $\tilde q\notin(-\infty,0]$ |
| modulus | $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ |
| angle | $\theta=\arccos(q_t/r)\in[0,\pi)$ |
| axis | $\vec n=\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ |
| exponent | $\tilde q_{\log}=\log\tilde q=\ln r+\theta\vec n$ |
| scale | $\exp(\ln r)=r$ |
| unit factor | $\exp(\theta\vec n)=\tilde q/r$ |
| reconstruction | $\tilde q=\exp(\tilde q_{\log})=r\exp(\theta\vec n)$ |

The principal cylinder $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$ is the exact domain of uniqueness. On its boundary the exponential sends the sphere of radius $\pi$ to the negative real axis, where the axis is not determined by the image.

### The Group Law

The modulus–unit form gives the group law. In the coordinates $(\ln r,\tilde u_{\mathrm r})\in\mathbb{R}\times S^3$,

$$
(\ln r_1,\tilde u_{\mathrm r,1})(\ln r_2,\tilde u_{\mathrm r,2})
=\bigl(\ln(r_1r_2),\ \tilde u_{\mathrm r,1}\tilde u_{\mathrm r,2}\bigr).
$$

The logarithmic scale adds and the unit factors multiply. The group of units is the direct product $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3$.

In exponential coordinates the law is not additive. With $\tilde u_{\mathrm r,j}=\cos\theta_j+\vec n_j\sin\theta_j$, the product is

$$
\tilde u_{\mathrm r,1}\tilde u_{\mathrm r,2}
=\cos\theta_1\cos\theta_2-\langle\vec n_1,\vec n_2\rangle\sin\theta_1\sin\theta_2
+\cos\theta_1\sin\theta_2\,\vec n_2+\sin\theta_1\cos\theta_2\,\vec n_1
+\sin\theta_1\sin\theta_2\,\vec n_1\times\vec n_2,
$$

where $\langle\vec n_1,\vec n_2\rangle$ is the Euclidean scalar product. It is $\exp(\vec v_1+\vec v_2)$ when the two exponents commute, that is, when $\vec n_1\times\vec n_2=0$ or one exponent is zero; it fails for non-commuting exponents in general. The exponential coordinates therefore parametrise the group without linearising it. Since the kernel is not a subgroup, $\mathbb{H}^{\times}$ is not a quotient of $\mathbb{H}$ by $\ker\exp$; the modulus–unit splitting is the group statement that survives.

## The Logarithm

### The General Logarithm

**Recall.** From *Quaternion Special Functions*, §*The Quaternion Logarithm*, a **logarithm** of $\tilde q\in\mathbb{H}^{\times}$ is a quaternion $\tilde q_{\log}$ with $\exp(\tilde q_{\log})=\tilde q$. The definition is an equation, not a formula.

Let $\tilde q_{\log}=q_{\log}e_t+\vec v$ be a logarithm, with $\vec v$ pure. Taking norms in the equation forces $q_{\log}=\ln\sqrt{\langle\tilde q\rangle_{\natural}}$, so the scalar coordinate is unique. The vector part is the logarithm of the unit factor, and it is read from the three cases of §*Existence and Uniqueness*.

| element | vector part $\vec v$ | logarithms |
|---|---|---|
| non-real, $\tilde q\notin\mathbb{R}$ | $(\theta+2\pi k)\vec n$, $k\in\mathbb{Z}$ | one for each integer |
| positive real, $\tilde q=r>0$ | $2\pi k\,\vec n$, $k\in\mathbb{Z}_{\ge0}$, $\vec n\in S^2$ | $0$, then a sphere for each $k\ge1$ |
| negative real, $\tilde q=-r<0$ | $(2k+1)\pi\,\vec n$, $k\in\mathbb{Z}_{\ge0}$, $\vec n\in S^2$ | a sphere for each $k$ |

In the first row $\theta=\arccos(q_t/r)\in(0,\pi)$ and $\vec n=\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$. The general logarithms are therefore

$$
\tilde q_{\log}=q_{\log}e_t+(\theta+2\pi k)\vec n,
\qquad q_{\log}=\ln\sqrt{\langle\tilde q\rangle_{\natural}},\quad k\in\mathbb{Z},
$$

for a non-real element, and the two sphere families on the real axis. Every nonzero quaternion has a logarithm, and no logarithm is unique. The ambiguity is not a translate of the kernel: the kernel is a union of spheres and the family above is a line. This is treated in §*The Kernel and the Fibre*.

The two coordinates are those of §*The Two Coordinates*: $q_{\log}=\ln r$ is unique, and $\vec q_{\log}=(\theta+2\pi k)\vec n$ carries the branch. Off the real axis $\vec n=\operatorname{sgn}\tilde q$.

### The Principal Logarithm

Single-valuedness is obtained by restricting the exponent to the **principal cylinder**

$$
B=\Bigl\{\ln r+\vec v:\ r>0,\ \sqrt{\langle\vec v\rangle_{\natural}}<\pi\Bigr\}.
$$

The exponential maps $B$ bijectively onto $\mathbb{H}\setminus(-\infty,0]$, and its inverse is the **principal logarithm**

$$ \boxed{\; \log\tilde q=\ln\sqrt{\langle\tilde q\rangle_{\natural}}
+\arccos\frac{q_t}{\sqrt{\langle\tilde q\rangle_{\natural}}}\,
\frac{\vec q}{\sqrt{\langle\vec q\rangle_{\natural}}},
\qquad \tilde q\notin(-\infty,0] \;} ,$$

with the second term read as $0$ when $\vec q=0$, that is, on the positive real axis. The scalar factor is the **argument** $\operatorname{Arg}\tilde q=\arccos(q_t/r)\in[0,\pi)$, so that

$$
\log\tilde q=\ln\sqrt{\langle\tilde q\rangle_{\natural}}+\operatorname{Arg}\tilde q\;\vec n .
$$

The inverse is discontinuous on the negative real axis, the **branch cut**. As $\tilde q\to-r_0$, the direction $\vec n$ tends to the direction of approach and the angle tends to $\pi$, so $\log\tilde q\to\ln r_0+\pi\vec n$ for whichever unit pure $\vec n$ the path selects. No value is distinguished at $\tilde q=-r_0$. On the cut itself the principal value is not defined; it is the cylinder, not the exponential, that ends there. The cylinder is a fundamental domain for the identification $\vec v\sim\vec v+2\pi k\vec n$ along each axis.

| $\tilde q$ | $r$ | $\operatorname{Arg}\tilde q$ | $\log\tilde q$ |
|---|---|---|---|
| $3e_t+4\vec e_x$ | $5$ | $0.9272952180016123$ | $1.6094379124341003+0.9272952180016123\,\vec e_x$ |
| $2e_t$ | $2$ | $0$ | $0.6931471805599453$ |
| $-2e_t$ | $2$ | $\pi$ | undefined |
| $\vec e_x$ | $1$ | $\pi/2$ | $1.5707963267948966\,\vec e_x$ |
| $e_t+\vec e_x$ | $\sqrt2$ | $\pi/4$ | $0.3465735902799727+0.7853981633974483\,\vec e_x$ |
| $-e_t-\vec e_x$ | $\sqrt2$ | $3\pi/4$ | $0.3465735902799727-2.356194490192345\,\vec e_x$ |

The sixth line is the mirror of the fifth: the element $-e_t-\vec e_x$ has argument $3\pi/4$ and axis $-\vec e_x$, so the vector part of the logarithm is negative.

### The Kernel and the Fibre

The kernel measures the failure of injectivity. It is computed from the closed form.

**Theorem.** Let $\tilde q=q_te_t+\vec v$ with $\vec v$ pure. Then $\exp(\tilde q)=e_t$ if and only if $q_t=0$ and $\sqrt{\langle\vec v\rangle_{\natural}}\in2\pi\mathbb{Z}$.

**Proof.** If $\exp(\tilde q)=e_t$ then taking norms gives $\exp(q_t)=1$, hence $q_t=0$. If $\vec v=0$ the condition is met. If $\vec v\neq0$, the closed form gives

$$
\cos\sqrt{\langle\vec v\rangle_{\natural}}
+\frac{\vec v}{\sqrt{\langle\vec v\rangle_{\natural}}}
\sin\sqrt{\langle\vec v\rangle_{\natural}}=e_t .
$$

Comparing the pure parts gives $\sin\sqrt{\langle\vec v\rangle_{\natural}}=0$, so $\sqrt{\langle\vec v\rangle_{\natural}}\in\pi\mathbb{Z}$, and comparing the scalar parts gives $\cos\sqrt{\langle\vec v\rangle_{\natural}}=1$, so $\sqrt{\langle\vec v\rangle_{\natural}}\in2\pi\mathbb{Z}$. Conversely, if $q_t=0$ and $\sqrt{\langle\vec v\rangle_{\natural}}=2\pi k$, the closed form gives $\cos(2\pi k)+(\vec v/\sqrt{\langle\vec v\rangle_{\natural}})\sin(2\pi k)=e_t$; for $k=0$ one has $\vec v=0$ and $\exp(0)=e_t$.

Hence

$$
\ker\exp=\{0\}\cup\bigcup_{k\ge1}\bigl\{\vec v\in\operatorname{Im}\mathbb{H}:
\langle\vec v\rangle_{\natural}=(2\pi k)^2\bigr\},
$$

a union of two-dimensional spheres, one for each positive integer, together with the isolated origin.

**Corollary.** The kernel is not a subgroup of $(\mathbb{H},+)$. The elements $2\pi\vec e_x$ and $2\pi\vec e_y$ lie in the kernel, but their sum $2\pi(\vec e_x+\vec e_y)$ has norm $8\pi^2$, which is not the square of a multiple of $2\pi$, so the sum is not in the kernel.

The fibre over a non-real element is the discrete line of §*The General Logarithm*. It is not a translate of the kernel: the kernel is a union of spheres and the fibre is a line. The fibre over a positive real element is the translate $\ln r+\ker\exp$, because $\ker\exp$ contains the origin and the spheres of radius $2\pi k$. The fibre over a negative real element is a union of spheres of radius $(2k+1)\pi$, also not a translate of the kernel. In the complex case the kernel $2\pi i\mathbb{Z}$ is a subgroup and every fibre is a coset; here only the positive real axis gives a translate of the kernel.

## Worked Examples

A full set of eight cases, with reconstruction and logarithm tables and the boundary family, is in *Worked Examples of Exponential Polar Decomposition of Quaternions*. The examples here show the generic computation and the table.

### A Generic Quaternion

Take $\tilde q=3e_t+4\vec e_x$. Then

$$
r=\sqrt{9+16}=5, \qquad \ln r=1.6094379124341003, \qquad
\theta=\arccos\frac35=0.9272952180016123,
$$

and the axis is $\vec e_x$. The principal exponent is $\tilde q_{\log}=q_{\log}e_t+\vec q_{\log}$ with

$$
q_{\log}=1.6094379124341003, \qquad \vec q_{\log}=0.9272952180016123\,\vec e_x .
$$

The reconstruction is

$$
\exp(\log\tilde q)=3.000000000000000\,e_t+4.000000000000000\,\vec e_x,
$$

with error $6.3\times10^{-16}$ in the norm $\sqrt{\langle\cdot\rangle_{\natural}}$.

Take now

$$
\tilde q=e_t+2\vec e_x+3\vec e_y+4\vec e_z .
$$

The modulus is $r=\sqrt{30}=5.477225575051661$, the scalar part of the unit factor is $1/\sqrt{30}=0.1825741858$, and

$$
\theta=\arccos\frac{1}{\sqrt{30}}=1.387192316515978, \qquad
\vec n=0.371390676354\,\vec e_x+0.557086014531\,\vec e_y+0.742781352708\,\vec e_z .
$$

The exponent is

$$
\log\tilde q=1.700598690831078+0.515190292664085\,\vec e_x
+0.772785438996128\,\vec e_y+1.030380585328170\,\vec e_z,
$$

and $\exp(\log\tilde q)$ reproduces $\tilde q$ to $1.1\times10^{-15}$ in each coefficient. The unit factor is the rotor $\tilde u_{\mathrm r}=0.1825741858e_t+0.3651483717\vec e_x+0.5477225575\vec e_y+0.7302967433\vec e_z$, and the sandwich by it rotates by $2\theta=2.7743846330$ about $\vec n$.

### A Table of Examples

| $\tilde q$ | $r$ | $q_{\log}=\ln r$ | $\theta$ | $\vec n$ | $\vec q_{\log}=\theta\vec n$ | $\sqrt{\langle\exp(\tilde q_{\log})-\tilde q\rangle_{\natural}}$ |
|---|---|---|---|---|---|---|
| $2e_t$ | $2$ | $0.6931471805599453$ | $0$ | arbitrary | $0$ | $0$ |
| $-\vec e_t$ | $1$ | $0$ | $\pi$ | arbitrary; $\vec e_x$ chosen | $3.141592653589793\,\vec e_x$ | $1.2\times10^{-16}$ |
| $\vec e_x$ | $1$ | $0$ | $1.5707963267948966$ | $\vec e_x$ | $1.5707963267948966\,\vec e_x$ | $6.1\times10^{-17}$ |
| $3e_t+4\vec e_x$ | $5$ | $1.6094379124341003$ | $0.9272952180016123$ | $\vec e_x$ | $0.9272952180016123\,\vec e_x$ | $6.3\times10^{-16}$ |
| $0.5e_t+0.1\vec e_x-0.2\vec e_y+0.3\vec e_z$ | $0.6244997998398398$ | $-0.4708042699292225$ | $0.6424323987868091$ | $0.2672612419124244\,\vec e_x-0.5345224838248488\,\vec e_y+0.8017837257372731\,\vec e_z$ | $0.1716972807445405\,\vec e_x-0.343394561489081\,\vec e_y+0.5150918422336214\,\vec e_z$ | $1.2\times10^{-16}$ |
| $e_t+2\vec e_x+3\vec e_y+4\vec e_z$ | $5.477225575051661$ | $1.7005986908310777$ | $1.387192316515978$ | $0.3713906763541037\,\vec e_x+0.5570860145311556\,\vec e_y+0.7427813527082074\,\vec e_z$ | $0.515190292664085\,\vec e_x+0.7727854389961275\,\vec e_y+1.03038058532817\,\vec e_z$ | $1.1\times10^{-15}$ |

The first line is the positive real axis: the angle is zero and the axis is undetermined. The second line is the negative real axis: the angle is $\pi$, the axis is arbitrary, and $\pi\vec e_x$ is one choice among a sphere of choices; no principal value exists. The third line is a pure unit, whose angle is $\pi/2$ and whose axis is itself.

### The Kernel and the Branch

The elements $2\pi\vec e_x$, $2\pi\vec e_y$ and $2\pi(\vec e_x+\vec e_y)/\sqrt2$ lie in the kernel, and their exponentials are $e_t$ to $2.4\times10^{-16}$. The sum $2\pi(\vec e_x+\vec e_y)$ does not lie in the kernel. Its norm is $8\pi^2$, whose square root is $2\pi\sqrt2$, and

$$
\exp\bigl(2\pi(\vec e_x+\vec e_y)\bigr)
=\cos(2\pi\sqrt2)+\frac{\vec e_x+\vec e_y}{\sqrt2}\sin(2\pi\sqrt2)
=-0.8582161857+0.3629497063\,(\vec e_x+\vec e_y),
$$

which is not $e_t$.

For $\tilde q=\vec e_x$ the principal exponent is $(\pi/2)\vec e_x$. The other logarithms are $(\pi/2+2\pi k)\vec e_x$, and $\exp((5\pi/2)\vec e_x)=\vec e_x$ to $3.1\times10^{-16}$. Adding $2\pi\vec e_y$ does not give another logarithm:

$$
\exp\bigl(\tfrac{\pi}{2}\vec e_x+2\pi\vec e_y\bigr)
=0.9813614629+0.0466083046\,\vec e_x+0.1864332186\,\vec e_y,
$$

which is not $\vec e_x$, because the two exponents do not commute. The fibre of $\vec e_x$ is the line $(\pi/2+2\pi k)\vec e_x$, not the translate of the kernel.

## The Matrix Picture

### The Exponential of a Conformal Matrix

Let $\iota$ be the embedding of *Modulus–Unit Polar Decomposition of Quaternions*, §*The Embedding in M_2(C)*. For a unit pure quaternion $\vec n$, the matrix $N=\iota(\vec n)$ satisfies

$$
N^{\dagger}=-N, \qquad N^2=-I, \qquad \operatorname{tr}N=0 .
$$

The exponential form of a quaternion reads, in matrices,

$$
M_{\tilde q}=\iota(\tilde q)=\exp\bigl(\ln r\,I+\theta N\bigr)
=r\bigl(\cos\theta\,I+\sin\theta\,N\bigr),
$$

with $\theta=\sqrt{\langle\vec v\rangle_{\natural}}$ and $N=\iota(\vec v/\sqrt{\langle\vec v\rangle_{\natural}})$. The determinant is

$$
\det M_{\tilde q}=r^2=\langle\tilde q\rangle_{\natural},
$$

as it must be, since the determinant of the exponential is the exponential of the trace.

Every invertible complex $2\times2$ matrix has a polar decomposition $B=PU$ with $P$ Hermitian positive definite and $U$ $*$-unitary, and for $B=M_{\tilde q}$ the conformal identity $M_{\tilde q}M_{\tilde q}^{\dagger}=r^2I$ gives $P=rI$ and $U=M_{\tilde u_{\mathrm r}}\in SU(2)$. The positive factor is a scalar because the only positive definite Hermitian matrices in the family are the positive multiples of the identity. The general theorem is the same splitting without the conformal restriction; the positive factor then carries the two singular values instead of the single scale $r$.

| factor | matrix | logarithm | determinant |
|---|---|---|---|
| modulus | $rI$ | $\ln r\,I$ | $r^2$ |
| unit factor | $M_{\tilde u_{\mathrm r}}\in SU(2)$ | $\theta N$ | $1$ |
| $\tilde q$ | $M_{\tilde q}$ | $\ln r\,I+\theta N$ | $r^2$ |

### The Matrix Logarithm and the Derivative

The matrix logarithm of $M_{\tilde q}$ is the matrix of the quaternion logarithm:

$$
\log M_{\tilde q}=\ln r\,I+\theta N
$$

on the principal branch. Adding $2\pi kN$ gives another logarithm, because $\exp(2\pi kN)=I$, and at $M_{\tilde q}=-rI$ every traceless skew-Hermitian $N$ with $N^2=-I$ gives a logarithm $\ln r\,I+\pi N$. The matrix logarithm inherits exactly the ambiguity of §*Existence and Uniqueness*.

The differential of the exponential is

$$
\mathrm d\exp_{\tilde q}
=L_{\exp(\tilde q)}\circ\frac{1-\exp(-\operatorname{ad}_{\tilde q})}{\operatorname{ad}_{\tilde q}},
$$

where $L$ denotes left multiplication and $\operatorname{ad}_{\tilde q}(X)=[\tilde q,X]$. The left factor is invertible, so the rank is that of

$$
A=\frac{1-\exp(-\operatorname{ad}_{\tilde q})}{\operatorname{ad}_{\tilde q}} .
$$

For $\tilde q=q_te_t+\vec v$ with $\theta=\sqrt{\langle\vec v\rangle_{\natural}}\neq0$, the eigenvalues of $\operatorname{ad}_{\tilde q}$ are $0$ with multiplicity two, on the span of $e_t$ and $\vec v$, and $\pm2i\theta$ with multiplicity one each on the orthogonal complement of $\vec v$ in the pure subspace. Hence the eigenvalues of $A$ are $1$ with multiplicity two and

$$
\frac{1-\exp(\mp2i\theta)}{\pm2i\theta}
=\exp(\mp i\theta)\frac{\sin\theta}{\theta}
$$

with multiplicity one each; at $\vec v=0$ all four are $1$. The differential is invertible exactly when $\theta\notin\pi\mathbb{Z}_{>0}$. The critical set is the union of the spheres $\theta=\pi k$, $k\ge1$, at every scalar height; at a critical point the rank drops by two, and the critical value is

$$
\exp(q_t)\bigl(\cos\pi k+\vec n\sin\pi k\bigr)=(-1)^k\exp(q_t)e_t .
$$

The critical values are exactly the nonzero real quaternions, positive for even $k$ and negative for odd $k$.

The determinant of the differential is the product of the determinant of left multiplication by $\exp(\tilde q)$ and the determinant of $A$. Left multiplication by a quaternion of modulus $\exp(q_t)$ has determinant $\exp(4q_t)$, and $A$ has determinant $(\sin\theta/\theta)^2$, with the value $1$ at $\vec v=0$. Hence

$$
\lvert\det\mathrm d\exp_{\tilde q}\rvert
=\exp(4q_t)\left(\frac{\sin\theta}{\theta}\right)^2 .
$$

The singular values are read from the same decomposition: the differential rotates the plane spanned by $e_t$ and $\vec v$ by $\theta$ and scales it by $\exp(q_t)$, with multiplicity two, and it scales the orthogonal pure plane by

$$
\exp(q_t)\frac{\lvert\sin\theta\rvert}{\theta},
$$

again with multiplicity two. The map is a similarity on the first plane and a different similarity on the second. It is conformal only where the two factors agree, which is $\lvert\sin\theta\rvert=\theta$, that is, only at $\vec v=0$. The quaternion exponential is not a conformal map of four-space.

## The Three Polar Decompositions

### The Three Forms

| decomposition | formula | parameters | domain | uniqueness | functions | group reading |
|---|---|---|---|---|---|---|
| modulus–unit | $\tilde q=r\tilde u_{\mathrm r}$ | $r>0$, $\tilde u_{\mathrm r}\in S^3$ | $\mathbb{H}^{\times}$ | unique | square root | $\mathbb{R}_{>0}\times S^3$ |
| rational-chart | $\tilde q=r\,(1-\vec v)(1+\vec v)^{-1}$ | $r>0$, $\vec v\in\operatorname{Im}\mathbb{H}$ | $\mathbb{H}\setminus(-\infty,0]$ | unique on the chart | rational | $\mathbb{R}_{>0}\times\mathbb{R}^3$, local |
| exponential | $\tilde q=\exp(\ln r+\vec v)$ | $r>0$, $\vec v\in\operatorname{Im}\mathbb{H}$ | $\mathbb{H}^{\times}$ | exponent modulo $2\pi$ along the axis; unique with $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$ | exponential and logarithm | not a quotient; the kernel is not a subgroup |

### The Modulus–Unit Form

The modulus–unit form is $\tilde q=r\tilde u_{\mathrm r}$ with $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ and $\tilde u_{\mathrm r}=\tilde q/\sqrt{\langle\tilde q\rangle_{\natural}}$. It is unique on the whole of $\mathbb{H}^{\times}$, it uses the square root of the norm, and it is the product decomposition of the group of units. It is the form developed in *Modulus–Unit Polar Decomposition of Quaternions*.

### The Rational-Chart Form

The rational-chart form writes the unit factor by the Cayley chart of the sphere. For $\vec v\in\operatorname{Im}\mathbb{H}$,

$$
\tilde u(\vec v)=(1-\vec v)(1+\vec v)^{-1},
$$

and $\vec v\mapsto\tilde u(\vec v)$ is a bijection from the pure subspace onto $S^3\setminus\{-e_t\}$. It is rational, uses no transcendental function, and misses the single point $-e_t$, the unit factor of the negative real axis. The decomposition $\tilde q=r\,\tilde u(\vec v)$ is therefore a rational chart, not a global decomposition. It is developed in *Rational-Chart Polar Decomposition of Quaternions*.

### The Change of Coordinates

Comparing $\tilde u(\vec v)=(1-\vec v)(1+\vec v)^{-1}$ with $\tilde u_{\mathrm r}=\exp(\theta\vec n)$ and writing $\vec v=s\vec n$ gives

$$
(1-s\vec n)(1+s\vec n)^{-1}
=\frac{1-s^2}{1+s^2}-\frac{2s}{1+s^2}\vec n
=\cos\theta+\vec n\sin\theta,
\qquad s=-\tan\frac{\theta}{2},
$$

so the passage between the rational coordinate and the angle is

$$
s=-\tan\frac{\theta}{2}, \qquad \theta=-2\arctan s .
$$

The map $s\mapsto\theta$ sends $\mathbb{R}$ onto $(-\pi,\pi)$, and $s\to\pm\infty$ corresponds to $\theta\to\mp\pi$. The cut $\theta=\pi$ is the negative real axis; its unit factor is $-e_t$, the single point the rational chart misses, and it is also the point at which the rational coordinate escapes to infinity.

### What the Comparison Says

The three forms are three presentations of one factorisation. The modulus–unit form is coordinate-free; the rational form puts a local rational coordinate on the sphere; the exponential form puts a global transcendental coordinate on it. The exponential form is the only one in which the exponent is additive, and even there only for commuting exponents. The modulus–unit form is the only one that is algebraic and global. The rational-chart form is the only one that is rational and local.

Four departures from the complex template separate the quaternion case from the commutative one.

- **The kernel is not a subgroup.** It is a union of spheres, not a discrete lattice, so $\mathbb{H}/\ker\exp$ is not a group.
- **The fibres are not all cosets.** For $\tilde q\notin\mathbb{R}$ the logarithms form the line $\ln r+(\theta+2\pi k)\vec n$, not the translate $\log\tilde q+\ker\exp$.
- **The exponential has critical points.** The spheres $\sqrt{\langle\vec v\rangle_{\natural}}=\pi k$ are critical, with the nonzero real axis as image; the complex exponential has none.
- **The principal domain is a cylinder, not a strip.** It is $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$, whose boundary sphere maps onto the negative real axis; the complex principal strip is half-open and contains that axis. On the real axis the angle is fixed and the axis is an arbitrary point of $S^2$, whereas in $\mathbb{C}$ there is only one imaginary direction.

## The Exponential Coordinates

### The Coordinate Lines

The **exponential coordinates** are the map

$$
E:\mathbb{R}\times\bigl\{\vec v\in\operatorname{Im}\mathbb{H}:
\sqrt{\langle\vec v\rangle_{\natural}}<\pi\bigr\}
\longrightarrow\mathbb{H}\setminus(-\infty,0],
\qquad E(q_{\log},\vec v)=\exp(q_{\log}+\vec v).
$$

**Theorem.** The map $E$ is a diffeomorphism onto its image.

**Proof.** The map is smooth. On the image, the inverse is $q_{\log}=\ln\sqrt{\langle\tilde q\rangle_{\natural}}$ and $\vec v$ the principal logarithm of §*The Principal Logarithm*; it is smooth because $\arccos$ and the quotient $\theta\vec q/\sqrt{\langle\vec q\rangle_{\natural}}$ extend smoothly across $\vec q=0$, and the remaining singular point $\tilde q=-r$ lies on the boundary $\sqrt{\langle\vec v\rangle_{\natural}}=\pi$. The differential is invertible on the open cylinder by §*The Matrix Logarithm and the Derivative*, so the inverse function theorem makes the map a local diffeomorphism; the explicit inverse makes it bijective. Hence it is a diffeomorphism.

The coordinates $(q_{\log},\vec v)$ give three families of curves and surfaces.

- **The scale lines.** At fixed $\vec v$, the curve $q_{\log}\mapsto\exp(q_{\log}+\vec v)$ is the ray of positive multiples of $\exp(\vec v)$. It runs from the origin, which is not attained, through $\exp(\vec v)$ and to infinity.
- **The angle lines.** At fixed unit $\vec n$, the curve $\theta\mapsto\exp(q_{\log}+\theta\vec n)$ is the arc of the great circle in the plane spanned by $e_t$ and $\vec n$. On the principal domain $\theta\in[0,\pi)$ it runs from $\exp(q_{\log})e_t$ to the point $\exp(q_{\log})(-e_t)$, which is excluded.
- **The latitude spheres.** At fixed $q_{\log}$ and fixed $\rho=\sqrt{\langle\vec v\rangle_{\natural}}$, the set of $\exp(q_{\log}+\rho\vec n)$ over unit $\vec n$ is the two-sphere

$$
\bigl\{\tilde q:\langle\tilde q\rangle_{\natural}=\exp(2q_{\log}),\
\operatorname{Sc}\tilde q=\exp(q_{\log})\cos\rho\bigr\},
$$

a latitude sphere in the three-sphere of radius $\exp(q_{\log})$. The exponential reads these families as the scale, the angle and the axis.

### The Conformal Factor

The differential rotates the plane spanned by $e_t$ and $\vec n$ by $\rho$ and scales it by $\exp(q_{\log})$, and it scales the orthogonal pure plane by $\exp(q_{\log})\lvert\sin\rho\rvert/\rho$, so the pullback of the Euclidean metric is

$$
(\exp^*g)_{(q_{\log},\rho,\vec n)}
=\exp(2q_{\log})\bigl(dq_{\log}^2+d\rho^2+\sin^2\rho\,d\Omega^2\bigr),
$$

where $d\Omega^2$ is the round metric of $S^2$. The bracket is the round metric of $\mathbb{R}\times S^3$ in the coordinates $(q_{\log},\rho,\vec n)$, not the Euclidean metric of the cylinder. The exponential is therefore conformal from the cylinder $\mathbb{R}\times S^3$ with the product metric, and not conformal from the Euclidean metric on the same cylinder. In Cartesian coordinates the Jacobian determinant is

$$
\exp(4q_{\log})\left(\frac{\sin\rho}{\rho}\right)^2,
$$

and the volume element is

$$
\mathrm dV=\exp(4q_{\log})\left(\frac{\sin\rho}{\rho}\right)^2\mathrm dq_{\log}\,\mathrm d\vec v
=\exp(4q_{\log})\sin^2\rho\,\mathrm dq_{\log}\,\mathrm d\rho\,\mathrm d\Omega .
$$

The factor $(\sin\rho/\rho)^2$ equals one at $\rho=0$ and vanishes on the boundary spheres $\rho=\pi k$, $k\ge1$.

### The Harmonic Reading

The complex reading does not carry over. In $\mathbb{C}$ the logarithm is holomorphic and its real part is harmonic; here the logarithm is a real-analytic map of four variables and is not quaternion-holomorphic, and the logarithmic scale is not harmonic either. With $r=\sqrt{\langle\tilde q\rangle_{\natural}}$,

$$
\Delta\ln r=\frac{2}{r^2}\neq0,
$$

because the Laplacian is four-dimensional. The function $r^{-2}=1/\langle\tilde q\rangle_{\natural}$ is harmonic off the origin, and it is the radial harmonic function of the layer. The components of the exponential are not harmonic: the scalar component $\exp(q_{\log})\cos\rho$ has Laplacian $-2\exp(q_{\log})\sin\rho/\rho$, which is nonzero on the open principal cylinder and vanishes on the boundary spheres $\rho=\pi k$, $k\ge1$. There are therefore no harmonic conjugates of the logarithmic scale, and the exponential is not a harmonic morphism. The coordinate $q_{\log}=\ln r$ is a smooth coordinate and the map $E$ is a diffeomorphism, but the analytic structure it carries is that of the product $\mathbb{R}\times S^3$, not that of a holomorphic plane.

## Summary

Every nonzero quaternion has an exponential polar decomposition

$$
\tilde q=\exp(\ln r+\vec v), \qquad r=\sqrt{\langle\tilde q\rangle_{\natural}}>0,
$$

with pure exponent $\vec v=\theta\vec n$, angle $\theta=\sqrt{\langle\vec v\rangle_{\natural}}$ and axis $\vec n\in S^2$; the unit factor is the rotor $\tilde u_{\mathrm r}=\cos\theta+\vec n\sin\theta$, whose sandwich rotates by $2\theta$. The pair $(r,\theta\vec n)$ is unique off the real axis. On the positive real axis the angle is $0$ and the axis is arbitrary; on the negative real axis the angle is $\pi$ and the axis is arbitrary. The principal representation has $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$ and covers the quaternion space cut along the closed negative real axis. Its exponent is the principal logarithm $\log\tilde q=\ln\sqrt{\langle\tilde q\rangle_{\natural}}+\theta\vec n$; every other logarithm is $\log\tilde q+2\pi k\vec n$ off the real axis, and a union of spheres on it.

The kernel is $\{0\}\cup2\pi S^2\cup4\pi S^2\cup\cdots$, a union of spheres and not a subgroup. The exponential is therefore not a homomorphism: the bracket of two pure exponents is twice their cross product, and $\exp(\tilde q_1+\tilde q_2)\neq\exp(\tilde q_1)\exp(\tilde q_2)$ for non-commuting exponents. The group of units is not $\mathbb{H}/\ker\exp$: off the real axis the fibres are lines, on the real axis they are spheres, and only the positive real axis gives cosets of the kernel. The amalgamation into one exponential survives because the logarithmic scale is central; the group law survives in the modulus–unit form, $\mathbb{H}^{\times}\cong\mathbb{R}_{>0}\times S^3$.

The differential of the exponential is invertible exactly off the spheres $\sqrt{\langle\vec v\rangle_{\natural}}=\pi k$, $k\ge1$, whose image is the nonzero real axis; its determinant is $\exp(4q_t)(\sin\theta/\theta)^2$. In the matrix picture the exponential is $\exp(\ln r\,I+\theta N)$ with $N$ skew-Hermitian and $N^2=-I$, and the matrix polar decomposition of the conformal matrix has positive factor $rI$ and special $*$-unitary factor. The exponential coordinates are a diffeomorphism from the cylinder $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$ onto the cut space; they are conformal from the cylinder $\mathbb{R}\times S^3$, not from the Euclidean metric on that cylinder.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde q=q_te_t+\vec q$ | a quaternion, $q_t$ its scalar part, $\vec q$ its pure part |
| $\tilde q^{\natural}=q_te_t-\vec q$ | the quaternion conjugate |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | the quaternion norm, positive definite |
| $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus |
| $\vec v=\theta\vec n$ | the pure exponent, $\theta=\sqrt{\langle\vec v\rangle_{\natural}}$, $\vec n\in S^2$ |
| $\exp(\tilde q)=\exp(q_t)(\cos\theta+(\vec v/\sqrt{\langle\vec v\rangle_{\natural}})\sin\theta)$ | the closed form |
| $\ker\exp=\{0\}\cup\bigcup_{k\ge1}\{\vec v:\langle\vec v\rangle_{\natural}=(2\pi k)^2\}$ | the kernel, not a subgroup |
| $[\vec v_1,\vec v_2]=2\,\vec v_1\times\vec v_2$ | the commutator of pure quaternions |
| $\mathrm d\exp_{\tilde q}$ | the differential, invertible off $\sqrt{\langle\vec v\rangle_{\natural}}\in\pi\mathbb{Z}_{>0}$ |
| $\exp(4q_t)(\sin\theta/\theta)^2$ | the Jacobian determinant |
| $\tilde u_{\mathrm r}=\exp(\vec v)$ | the rotor part, the unit factor, of norm one |
| $\tilde q_{\log}=q_{\log}e_t+\vec q_{\log}$ | the exponent, principal when $\sqrt{\langle\vec v\rangle_{\natural}}<\pi$ |
| $q_{\log}=\ln r$, $\vec q_{\log}=\vec v=\theta\vec n$ | the scalar and vector coordinates of the exponent |
| $\log\tilde q=\ln r+\theta\vec n$ | the principal logarithm, on $\mathbb{H}\setminus(-\infty,0]$ |
| $N=\iota(\vec n)$ | the skew-Hermitian matrix of the unit axis |
| $M_{\tilde q}=\exp(\ln r\,I+\theta N)$ | the matrix exponential |
| $\mathbb{H}\setminus(-\infty,0]$ | the image of the principal coordinates |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Quaternions](worked-examples-of-exponential-polar-decomposition-of-quaternions.html), for the eight cases, the reconstruction and logarithm tables, the real axis family and the product defect.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the matrix exponential, the matrix logarithm and the polar decomposition.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the exponential map of $SU(2)$ and the unit quaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition 2001), for the quaternion exponential and its relation to the rotation group.
- S. J. Sangwine and E. Hitzer, "Polar decomposition of complexified quaternions and octonions", *Advances in Applied Clifford Algebras* **30** (2020), for the exponential trichotomy and the polar forms of the hypercomplex algebras.

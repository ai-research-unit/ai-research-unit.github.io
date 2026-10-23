# __Rational-Chart Polar Decomposition of Quaternions__

## Introduction

The modulus–unit polar decomposition of *Modulus–Unit Polar Decomposition of Quaternions* writes every nonzero quaternion as

$$
\tilde q = r\,\tilde u_{\mathrm r}, \qquad r = \sqrt{\langle\tilde q\rangle_{\natural}} > 0, \qquad \langle\tilde u_{\mathrm r}\rangle_{\natural} = 1,
$$

with $r$ the modulus and $\tilde u_{\mathrm r}$ the unit factor. That article proves the pair unique and treats $\tilde u_{\mathrm r}$ as a point of the unit sphere $S^3$. It chooses no coordinate on the sphere: the unit factor is named by the equation $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$, not by a triple of numbers.

This article names it. For a pure quaternion $\vec v = v_x\vec e_x+v_y\vec e_y+v_z\vec e_z$ put

$$
u(\vec v) = (1-\vec v)(1+\vec v)^{-1},
$$

and write

$$
\tilde q = r\,u(\vec v) = r\,(1-\vec v)(1+\vec v)^{-1}.
$$

Nothing in the decomposition changes. The number $r$ is still the modulus, the element $u(\vec v)$ is still the same unit factor, and the pair $(r,u)$ is still unique. The only new object is the pure quaternion $\vec v$, which replaces the point of the sphere by a coordinate in the three-dimensional pure subspace.

The chart is rational: $u(\vec v)$ and its inverse are ratios of polynomials, and no transcendental function occurs. The price is locality. As $\sqrt{\langle \vec v\rangle_{\natural}}$ grows the unit $u(\vec v)$ approaches $-1$ without attaining it, so the one unit factor that is missed is $-1$, the unit factor of every negative real quaternion. The decomposition therefore holds on $\mathbb{H}$ cut along the negative real axis, and it fails on the cut.

Noncommutativity enters the coordinate calculus. The inverse is a rational expression in $u$, and in $\mathbb{H}$ its two orderings coincide; the product is not a bare fraction. The coordinate of a product is the bare fraction conjugated by $1+\vec v_1$, a sandwich that is the exact noncommutative correction. The complex formula is the commutative shadow of this law.

The plan is as follows. The modulus–unit form is recalled (§*The Modulus–Unit Form Recalled*), the chart and its inverse are defined (§*The Chart*, §*The Inverse*), and the chart is proved a bijection (§*The Bijection*). The decomposition is then stated and proved (§*The Rational-Chart Decomposition*), the group law in the coordinate is computed (§*The Group Law*), the covering of the sphere by two charts and the cost of rationality are described (§*Covering the Sphere and the Price of Locality*), and the matrix picture (§*The Matrix Picture*) and worked examples (§*Worked Examples*) close the mathematical part. The comparison with the two other forms is in §*Covering the Sphere and the Price of Locality* and in *Exponential Polar Decomposition of Quaternions*, §*The Three Polar Decompositions*.

The symbols are those of *Quaternion Algebra* and *Norm and Invertibility in the Quaternion Algebra*, and the conventions are those of *Conventions in Mathematics*. The notation is collected in §*Summary of Notation*.

Every numerical value displayed below was recomputed in double precision.

## The Unit Factor and Its Chart

### The Modulus–Unit Form Recalled

For a quaternion $\tilde q$ the norm is

$$
\langle\tilde q\rangle_{\natural} = \tilde q\tilde q^{\natural} = q_t^2+q_x^2+q_y^2+q_z^2,
$$

which is positive off the origin. The modulus is $r=\sqrt{\langle\tilde q\rangle_{\natural}}$, a positive real with no sign choice, and the unit factor is

$$
\tilde u_{\mathrm r} = \frac{\tilde q}{r}, \qquad \langle\tilde u_{\mathrm r}\rangle_{\natural} = \frac{\langle\tilde q\rangle_{\natural}}{r^2} = 1.
$$

The unit factor lies on the unit sphere $\mathrm{Sp}(1)=\{\tilde u:\langle\tilde u\rangle_{\natural}=1\}=S^3$. The pair $(r,\tilde u_{\mathrm r})$ is unique: taking norms in $\tilde q=r\tilde u_{\mathrm r}$ forces $r=\sqrt{\langle\tilde q\rangle_{\natural}}$, and then $\tilde u_{\mathrm r}=\tilde q/r$.

This is where the modulus–unit article stops. The present article adds one object, the pure quaternion $\vec v$, and changes nothing else.

The unit sphere is a compact, connected, simply connected group of dimension three. Its inverse is the quaternion conjugate, $\tilde u^{-1}=\tilde u^{\natural}$, and it is non-abelian. The chart below is a chart of this three-dimensional group, not of a circle; the extra two dimensions are the reason the chart's parameter is a pure quaternion and the reason the group law is a noncommutative sandwich rather than a scalar fraction.

### The Chart

**Definition.** For a pure quaternion $\vec v$ the **chart** is

$$
u(\vec v) = (1-\vec v)(1+\vec v)^{-1} = \frac{(1-\langle \vec v\rangle_{\natural})-2\vec v}{1+\langle \vec v\rangle_{\natural}}.
$$

The denominator $1+\vec v$ is invertible because

$$
\langle 1+\vec v\rangle_{\natural} = (1+\vec v)(1+\vec v)^{\natural} = 1+\langle \vec v\rangle_{\natural} > 0,
$$

and its inverse is $(1-\vec v)/(1+\langle \vec v\rangle_{\natural})$, since $(1+\vec v)(1-\vec v)=1-\vec v^2=1+\langle \vec v\rangle_{\natural}$. Substituting gives the expanded form. The real and pure parts of $u(\vec v)$ are

$$
\operatorname{Sc}u(\vec v) = \frac{1-\langle \vec v\rangle_{\natural}}{1+\langle \vec v\rangle_{\natural}}, \qquad \operatorname{Vec}u(\vec v) = -\frac{2\vec v}{1+\langle \vec v\rangle_{\natural}}.
$$

Their squares satisfy

$$
\left(\frac{1-\langle \vec v\rangle_{\natural}}{1+\langle \vec v\rangle_{\natural}}\right)^2 + \frac{4\langle \vec v\rangle_{\natural}}{(1+\langle \vec v\rangle_{\natural})^2}
= \frac{(1+\langle \vec v\rangle_{\natural})^2}{(1+\langle \vec v\rangle_{\natural})^2} = 1,
$$

so every $u(\vec v)$ is a unit quaternion. Three values fix the orientation:

$$
u(0)=1, \qquad u(\vec e_x)=-\vec e_x, \qquad u(\vec e_y)=-\vec e_y .
$$

The second value is the general rule for a unit pure parameter: if $\sqrt{\langle \vec v\rangle_{\natural}}=1$ then $u(\vec v)=-\vec v$.

The chart almost covers the sphere, but not quite. If $u(\vec v)=-1$ then $1-\vec v=-(1+\vec v)$, hence $1=-1$, which is impossible; so $-1$ is not attained. As $\sqrt{\langle \vec v\rangle_{\natural}}$ grows without bound,

$$
u(\vec v) = -1+\frac{2}{1+\langle \vec v\rangle_{\natural}}-\frac{2\vec v}{1+\langle \vec v\rangle_{\natural}} \longrightarrow -1,
$$

so $-1$ is the limit of the chart at infinity in every direction.

Geometrically, the line through $-1$ and $u(\vec v)$ meets the pure subspace at $-\vec v$. Indeed the point $-1+t(u(\vec v)+1)$ has scalar part $-1+t(1+\operatorname{Sc}u(\vec v))$, which vanishes at $t=1/(1+\operatorname{Sc}u(\vec v))$, and its pure part is then $\operatorname{Vec}u(\vec v)/(1+\operatorname{Sc}u(\vec v))=-\vec v$. The standard stereographic coordinate of $u(\vec v)$ from $-1$ is therefore $-\vec v$: the chart is that coordinate with the sign reversed.

### The Inverse

**Proposition.** Let $u\in\mathrm{Sp}(1)$ with $u\neq-1$. Then $u=u(\vec v)$ for the pure quaternion

$$ \boxed{\; \vec v = (1-u)(1+u)^{-1} \;} .$$

**Proof.** Write $u=a+w$ with $a\in\mathbb{R}$ and $w$ pure. Since $\langle u\rangle_{\natural}=1$, one has $a^2+\langle w\rangle_{\natural}=1$, and since $u\neq-1$, one has $a\neq-1$. The inverse of $1+u=(1+a)+w$ is

$$
(1+u)^{-1} = \frac{(1+a)-w}{(1+a)^2+\langle w\rangle_{\natural}} = \frac{(1+a)-w}{2(1+a)} .
$$

Therefore

$$
(1-u)(1+u)^{-1} = \bigl((1-a)-w\bigr)\frac{(1+a)-w}{2(1+a)}
= \frac{1-a^2-\langle w\rangle_{\natural}-2w}{2(1+a)} = -\frac{w}{1+a},
$$

which is pure. Calling it $\vec v$, one has $\vec v=(1-u)(1+u)^{-1}$, and the computation of §*The Chart* read backwards gives $u=(1-\vec v)(1+\vec v)^{-1}=u(\vec v)$.

The same computation gives the **pure-part formula**

$$
\vec v = -\frac{\operatorname{Vec}u}{1+\operatorname{Sc}u},
$$

valid for every unit $u\neq-1$. The two orderings of the inverse coincide in any associative algebra: the factors $1+u$ and $1-u$ are polynomials in $u$, hence commute, so $(1+u)^{-1}(1-u)=(1-u)(1+u)^{-1}$.

For a quaternion $\tilde q$ of modulus $r$ the unit factor is $\tilde u_{\mathrm r}=\tilde q/r$, and the coordinate is

$$
\vec v = (1-\tilde u_{\mathrm r})(1+\tilde u_{\mathrm r})^{-1} = (r-\tilde q)(r+\tilde q)^{-1}.
$$

The second form names $\vec v$ by $\tilde q$ alone. On the domain, its denominator vanishes exactly at $\tilde q=-r$, the negative real axis, where the chart has no point.

### The Bijection

**Theorem.** The map $\vec v\mapsto u(\vec v)$ is a bijection from the pure subspace onto $\mathrm{Sp}(1)\setminus\{-1\}$.

**Injectivity.** Suppose $u(\vec v_1)=u(\vec v_2)$. The scalar parts give

$$
\frac{1-\langle \vec v_1\rangle_{\natural}}{1+\langle \vec v_1\rangle_{\natural}} = \frac{1-\langle \vec v_2\rangle_{\natural}}{1+\langle \vec v_2\rangle_{\natural}},
$$

and cross-multiplication gives $\langle \vec v_1\rangle_{\natural}=\langle \vec v_2\rangle_{\natural}$. The pure parts then give

$$
\frac{2\vec v_1}{1+\langle \vec v_1\rangle_{\natural}} = \frac{2\vec v_2}{1+\langle \vec v_2\rangle_{\natural}},
$$

and the common denominator is equal, so $\vec v_1=\vec v_2$.

**Surjectivity.** This is the proposition of §*The Inverse*: for every unit $u\neq-1$ the pure quaternion $\vec v=(1-u)(1+u)^{-1}$ satisfies $u(\vec v)=u$.

The chart is therefore one-to-one, and its image is the sphere with the single point $-1$ removed.

## The Rational-Chart Decomposition

### Existence and Uniqueness

**Theorem.** Every quaternion outside the closed negative real axis has exactly one rational-chart polar decomposition

$$ \boxed{\; \tilde q = r\,(1-\vec v)(1+\vec v)^{-1}, \qquad r>0, \quad \vec v\in\operatorname{Im}\mathbb{H} \;} .$$

**Existence.** Let $\tilde q\notin(-\infty,0]$, and put $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ and $\tilde u_{\mathrm r}=\tilde q/r$. Then $r>0$ and $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$. If $\tilde u_{\mathrm r}=-1$ then $\tilde q=-r$ is a negative real, contrary to the hypothesis, so $\tilde u_{\mathrm r}\neq-1$; the bijection then gives a pure $\vec v$ with $\tilde u_{\mathrm r}=u(\vec v)$. Hence $\tilde q=ru(\vec v)$.

**Uniqueness.** Taking norms gives $r=\sqrt{\langle\tilde q\rangle_{\natural}}$, and then $\tilde u_{\mathrm r}=\tilde q/r$; the chart is injective, so $\vec v$ is determined by $\tilde u_{\mathrm r}$.

The coordinate is $\vec v=(r-\tilde q)(r+\tilde q)^{-1}$ of §*The Inverse*, and the reconstruction is exact:

$$
\tilde q = r\,\frac{(1-\langle \vec v\rangle_{\natural})-2\vec v}{1+\langle \vec v\rangle_{\natural}}.
$$

### The Domain

The domain is

$$
\mathbb{H}\setminus(-\infty,0] = \{\,\tilde q : \tilde q\neq0 \ \text{and} \ \tilde q\notin\mathbb{R}_{<0}\,\},
$$

the quaternion space cut along the closed negative real axis.

The origin is excluded because no polar decomposition of any kind exists there. The negative real axis is excluded because its unit factor is $-1$, the point the chart does not attain. Every other point of the sphere is attained exactly once. In the formula $\vec v=(r-\tilde q)(r+\tilde q)^{-1}$ the two exclusions are visible at once: the denominator vanishes at $\tilde q=-r$, the negative real axis, and numerator and denominator both vanish at $\tilde q=0$, where $r=0$ and no decomposition exists. Unlike the split cases, there is no null cone and no element of vanishing norm; the cut is a ray, not a hypersurface.

## The Group Law

### The Product Formula

The product of two unit factors is a unit factor, and the coordinate of the product is a rational function of the two coordinates.

**Proposition.** For pure $\vec v_1,\vec v_2$ with $1+\vec v_1\vec v_2\neq0$,

$$ \boxed{\; u(\vec v_1)u(\vec v_2) = u(\vec v_3), \qquad
\vec v_3 = (1+\vec v_1)^{-1}(\vec v_1+\vec v_2)(1+\vec v_1\vec v_2)^{-1}(1+\vec v_1) \;} .$$

**Proof.** Write $A=1+\vec v_1$ and $B=1+\vec v_2$. From $1-u(\vec v)=2\vec v(1+\vec v)^{-1}$ and $1+u(\vec v)=2(1+\vec v)^{-1}$, applied to each factor,

$$
1-u(\vec v_1)u(\vec v_2) = \bigl(1-u(\vec v_1)\bigr)+u(\vec v_1)\bigl(1-u(\vec v_2)\bigr)
= 2A^{-1}\Bigl(\vec v_1+(1-\vec v_1)\vec v_2B^{-1}\Bigr),
$$

$$
1+u(\vec v_1)u(\vec v_2) = \bigl(1+u(\vec v_1)\bigr)-u(\vec v_1)\bigl(1-u(\vec v_2)\bigr)
= 2A^{-1}\Bigl(1-(1-\vec v_1)\vec v_2B^{-1}\Bigr).
$$

The two inner parentheses simplify:

$$
\vec v_1+(1-\vec v_1)\vec v_2B^{-1} = \bigl(\vec v_1B+(1-\vec v_1)\vec v_2\bigr)B^{-1} = (\vec v_1+\vec v_2)B^{-1},
$$

$$
1-(1-\vec v_1)\vec v_2B^{-1} = \bigl(B-(1-\vec v_1)\vec v_2\bigr)B^{-1} = (1+\vec v_1\vec v_2)B^{-1}.
$$

Hence

$$
\vec v_3 = (1-u_1u_2)(1+u_1u_2)^{-1}
= A^{-1}(\vec v_1+\vec v_2)B^{-1}\,B(1+\vec v_1\vec v_2)^{-1}A
= A^{-1}(\vec v_1+\vec v_2)(1+\vec v_1\vec v_2)^{-1}A,
$$

which is the stated formula.

### The Noncommutative Correction

Write

$$
B_{\mathrm{bare}} = (\vec v_1+\vec v_2)(1+\vec v_1\vec v_2)^{-1}.
$$

Then the exact law reads

$$
\vec v_3 = (1+\vec v_1)^{-1}\,B_{\mathrm{bare}}\,(1+\vec v_1).
$$

The bare fraction is the complex formula $(s_1+s_2)/(1-s_1s_2)$ transplanted to the quaternion coordinate, and it is **wrong** in general. The exact coordinate is its conjugate by $1+\vec v_1$. Conjugation preserves the scalar part and rotates the pure part, so it preserves $\sqrt{\langle B_{\mathrm{bare}}\rangle_{\natural}}$ and changes its direction; the bare fraction has the right modulus and the wrong axis. No choice of ordering repairs it: the alternative $(1+\vec v_1\vec v_2)^{-1}(\vec v_1+\vec v_2)$ is another wrong value, not the conjugate of the first. When $\vec v_1$ and $\vec v_2$ commute, the conjugating factor acts trivially and $\vec v_3=B_{\mathrm{bare}}=(\vec v_1+\vec v_2)(1+\vec v_1\vec v_2)^{-1}$, which is the commutative law.

A clean counterexample is $\vec v_1=\vec e_x$ and $\vec v_2=\vec e_y$. Then $u(\vec v_1)=-\vec e_x$ and $u(\vec v_2)=-\vec e_y$, so

$$
u(\vec v_1)u(\vec v_2)=\vec e_x\vec e_y=\vec e_z,
$$

and therefore $\vec v_3=-\vec e_z$. The bare fraction is

$$
B_{\mathrm{bare}} = (\vec e_x+\vec e_y)(1+\vec e_z)^{-1}
= \frac{(\vec e_x+\vec e_y)(1-\vec e_z)}{2} = \vec e_y,
$$

which is a different pure quaternion; the error is $\sqrt{\langle\vec e_y+\vec e_z\rangle_{\natural}}=\sqrt{2}=1.414213562$. The sandwich conjugates $\vec e_y$ by $1-\vec e_x$ and returns $-\vec e_z$.

### Identity, Inverse and the Pole

The law has the identity $\vec v=0$, because $u(0)=1$. The inverse coordinate is $-\vec v$, because

$$
u(\vec v)u(-\vec v) = (1-\vec v)(1+\vec v)^{-1}(1+\vec v)(1-\vec v)^{-1}=1 .
$$

It is associative wherever it is defined, being inherited from the multiplication of the sphere.

When $1+\vec v_1\vec v_2=0$ the formula has a pole. Since $\mathbb{H}$ is a division algebra, this happens exactly when $\vec v_1\vec v_2=-1$. For pure $\vec v_1,\vec v_2$,

$$
\vec v_1\vec v_2 = -\vec v_1\cdot \vec v_2 + \vec v_1\times \vec v_2,
$$

so the product is real exactly when $\vec v_1$ and $\vec v_2$ are parallel or one of them vanishes, and it equals $-1$ exactly when

$$
\vec v_2 = \frac{\vec v_1}{\langle \vec v_1\rangle_{\natural}}.
$$

When $\sqrt{\langle \vec v_1\rangle_{\natural}}=1$ this is $\vec v_2=\vec v_1$, and then $u(\vec v_1)=-\vec v_1$ gives $u(\vec v_1)^2=-1$; in every case the product $u(\vec v_1)u(\vec v_2)$ equals $-1$, the missing point, and the coordinate escapes to infinity. The chart is therefore a **group chunk**, not a global group. It is a coordinate on the pure subspace, and that subspace must be compactified to see the whole sphere.

## Covering the Sphere and the Price of Locality

### The Second Chart

The chart misses $-1$. A second chart, $-u(\vec v)$, misses $+1$ and supplies $-1$. On the common domain the two are related by

$$
-u(\vec v) = u(\vec v^{-1}), \qquad \vec v^{-1} = -\frac{\vec v}{\langle \vec v\rangle_{\natural}},
$$

for $\vec v\neq0$. To prove the identity, write $1-\vec v^{-1}=\vec v^{-1}(\vec v-1)$ and $1+\vec v^{-1}=\vec v^{-1}(\vec v+1)$; then

$$
u(\vec v^{-1}) = \vec v^{-1}(\vec v-1)(\vec v+1)^{-1}\vec v = \vec v^{-1}\bigl(-u(\vec v)\bigr)\vec v = -u(\vec v),
$$

because $u(\vec v)$ commutes with $\vec v$. The second chart attains $-1$ at $\vec v=0$ and misses $+1$, since $-u(\vec v)=1$ would give $u(\vec v)=-1$. The two charts

$$
\vec v\longmapsto u(\vec v), \qquad \vec v\longmapsto -u(\vec v)
$$

therefore cover the sphere, the first missing $-1$ and the second missing $+1$.

### The Two Charts and the Cut

The first chart covers every nonzero quaternion except the negative real axis; the second covers every nonzero quaternion except the positive real axis. Together they cover $\mathbb{H}^{\times}$. Topologically the one-point compactification of the pure subspace is a three-sphere, $\operatorname{Im}\mathbb{H}\cup\{\infty\}\cong S^3$, and the first chart extends to a homeomorphism onto $S^3$ by setting $u(\infty)=-1$.

The chart has three properties, and they are the terms of an exchange.

- **It is rational.** Both $u(\vec v)$ and its inverse are ratios of polynomials; once the modulus $r$ is known, the decomposition uses field operations alone, with no transcendental function and no infinite series.
- **It is local.** It misses one point of the sphere, and therefore one ray of the quaternion space. A second chart, or the point at infinity, is needed to recover the sphere.
- **It is unbounded.** Near the missing point the coordinate escapes to infinity, and the approach to the cut from different directions gives coordinates escaping in those directions.

The modulus–unit form is global and uses a square root. The exponential form, treated in *Exponential Polar Decomposition of Quaternions*, is global and uses a transcendental function. The present form is the one that stays rational, and locality is its price. In the quaternion case there is a second price: the group law is not the commutative fraction, and the chart is a group chunk only through a sandwich. The three forms are compared in *Exponential Polar Decomposition of Quaternions*, §*The Three Polar Decompositions*; the rational chart is the only one that stays rational.

### The Departures from the Complex Template

The complex rational chart is $u(s)=(1-is)/(1+is)$ with $s\in\mathbb{R}$ and group law $s_3=(s_1+s_2)/(1-s_1s_2)$. The quaternion chart keeps the shape $(1-\vec v)(1+\vec v)^{-1}$ but changes four things.

- **The parameter is a pure quaternion, not a scalar.** The chart is a chart of a three-dimensional sphere, so the coordinate has three real components.
- **The group law is a sandwich.** The complex fraction is replaced by $(1+\vec v_1)^{-1}B_{\mathrm{bare}}(1+\vec v_1)$, the conjugation by $1+\vec v_1$. The bare fraction is correct only when $1+\vec v_1$ commutes with $B_{\mathrm{bare}}$, which is automatic in the commutative case and fails here.
- **The inverse is unambiguous in both orderings.** The complex formula $s=i(u-1)/(u+1)$ has no order to specify. In $\mathbb{H}$ the formula $\vec v=(1-u)(1+u)^{-1}$ also has no order to specify, because $1+u$ and $1-u$ commute; the noncommutativity appears in the product, not in the inverse.
- **The chart is minus the stereographic coordinate.** The line through $-1$ and $u(\vec v)$ meets the pure subspace at $-\vec v$, not at $\vec v$; the sign is a convention of the chart and does not affect the decomposition.

The cut and the missing point are exactly as in the complex case: one unit factor, $-1$, is missing, and the elements with that unit factor are the negative real axis. The difference is that this axis is a ray in three-dimensional space, and as an element approaches it the coordinate escapes in the direction of its approach, so the cut has a whole sphere of escape directions rather than two sides.

## The Matrix Picture

### The Cayley Transform in SU(2)

Let $V=\iota(\vec v)$ be the image of the pure quaternion $\vec v$ under the embedding of *Modulus–Unit Polar Decomposition of Quaternions*, §*The Embedding in M_2(C)*. Since $\vec v$ is pure, $V$ is skew-Hermitian and traceless, and

$$
V^{\dagger}=-V, \qquad V^2=-\langle \vec v\rangle_{\natural} I .
$$

The chart is the **Cayley transform** of $V$:

$$
M(\vec v) = \iota\bigl(u(\vec v)\bigr) = (I-V)(I+V)^{-1}.
$$

The matrices $I-V$ and $I+V$ commute, and $I+V$ is invertible because its eigenvalues are $1\pm i\sqrt{\langle \vec v\rangle_{\natural}}$. The matrix $M(\vec v)$ is unitary,

$$
M(\vec v)^{\dagger}M(\vec v) = (I+V^{\dagger})^{-1}(I-V^{\dagger})(I-V)(I+V)^{-1} = I,
$$

and its determinant is

$$
\det M(\vec v) = \frac{\det(I-V)}{\det(I+V)} = \frac{1+\langle \vec v\rangle_{\natural}}{1+\langle \vec v\rangle_{\natural}}=1,
$$

because the eigenvalues of $V$ are $\pm i\sqrt{\langle \vec v\rangle_{\natural}}$ and each determinant is $1+\langle \vec v\rangle_{\natural}$. Hence $M(\vec v)\in SU(2)$, as it must be, since it is the image of the unit quaternion $u(\vec v)$.

In coordinates,

$$
M(\vec v)=\frac{1}{1+\langle \vec v\rangle_{\natural}}
\begin{pmatrix}
1-\langle \vec v\rangle_{\natural}+2iv_z & 2iv_x+2v_y\\
2iv_x-2v_y & 1-\langle \vec v\rangle_{\natural}-2iv_z
\end{pmatrix}.
$$

The Cayley transform is the matrix analogue of the chart: it maps the skew-Hermitian space onto $SU(2)$ minus the matrix $-I$, and its inverse is $V=(I-M)(I+M)^{-1}$. The sandwich of §*The Product Formula* is the coordinate expression of the noncommutativity of $SU(2)$, not an artefact of the chart.

## Worked Examples

### A Generic Quaternion

Take

$$
\tilde q = e_t+2\vec e_x+3\vec e_y+4\vec e_z .
$$

The norm is $30$, so $r=\sqrt{30}=5.477225575$ and

$$
\tilde u_{\mathrm r}=0.182574186\,e_t+0.365148372\,\vec e_x+0.547722558\,\vec e_y+0.730296743\,\vec e_z .
$$

The chart coordinate is

$$
\vec v=-0.308774178\,\vec e_x-0.463161266\,\vec e_y-0.617548355\,\vec e_z,
$$

with $\sqrt{\langle \vec v\rangle_{\natural}}=0.831399917$. The reconstruction $r\,u(\vec v)$ reproduces $\tilde q$ to $4.4\times10^{-16}$ in each coefficient.

### The Real and the Excluded Cases

For $\tilde q=2e_t$ the modulus is $2$ and the unit factor is $1$, so $\vec v=0$. For $\tilde q=-3e_t$ the unit factor is $-1$, which the chart does not attain; the element is excluded. For $\tilde q=\vec e_x$ the modulus is $1$ and the unit factor is $\vec e_x$, so

$$
\vec v = (1-\vec e_x)(1+\vec e_x)^{-1} = -\vec e_x,
$$

which is consistent with $u(-\vec e_x)=\vec e_x$.

### A Table of Examples

The table collects the cases computed in this article.

| $\tilde q$ | $r$ | $\tilde u_{\mathrm r}$ | $\vec v$ | $\sqrt{\langle \vec v\rangle_{\natural}}$ | reconstruction error |
|---|---|---|---|---|---|
| $2e_t$ | $2$ | $e_t$ | $0$ | $0$ | $0$ |
| $\vec e_x$ | $1$ | $\vec e_x$ | $-\vec e_x$ | $1$ | $0$ |
| $3\vec e_x-4\vec e_z$ | $5$ | $0.6\vec e_x-0.8\vec e_z$ | $-0.6\vec e_x+0.8\vec e_z$ | $1$ | $2.8\times10^{-16}$ |
| $e_t+\vec e_x$ | $\sqrt{2}$ | $(e_t+\vec e_x)/\sqrt{2}$ | $-0.414213562\,\vec e_x$ | $0.414213562$ | $0$ |
| $-e_t+\vec e_x$ | $\sqrt{2}$ | $(-e_t+\vec e_x)/\sqrt{2}$ | $-2.414213562\,\vec e_x$ | $2.414213562$ | $2.2\times10^{-16}$ |
| $e_t+2\vec e_x+3\vec e_y+4\vec e_z$ | $\sqrt{30}$ | the unit factor above | the coordinate above | $0.831399917$ | $4.4\times10^{-16}$ |
| $-3e_t$ | $3$ | $-e_t$ | excluded | — | — |

The table shows the sign rule of the chart: for a pure unit $\vec e_x$ the coordinate is $-\vec e_x$, and for $3\vec e_x-4\vec e_z$ it is the negative of the vector part. The fifth line is already close to the cut: its unit factor has scalar part $-1/\sqrt{2}$ and its coordinate has modulus $2.414$. A point nearer the cut has a much larger coordinate.

### The Near-Cut Behaviour

Take $\tilde q=-e_t+0.001\vec e_x$. Its modulus is $r=1.000000500$ and its unit factor is

$$
\tilde u_{\mathrm r}=-0.999999500\,e_t+0.000999999\,\vec e_x .
$$

The coordinate is

$$
\vec v=-2000.000500\,\vec e_x,
$$

with $\sqrt{\langle \vec v\rangle_{\natural}}=2000.000500$. The reconstruction returns $\tilde q$ to $1.1\times10^{-16}$. The example makes the cut visible: as the scalar part of $\tilde q$ approaches $-r$, the denominator $r+\tilde q$ approaches zero and the coordinate escapes along the direction of the vector part, which is the direction of approach to the cut.

## Summary

Every quaternion outside the closed negative real axis has exactly one rational-chart polar decomposition $\tilde q=r\,u(\vec v)$, with $r=\sqrt{\langle\tilde q\rangle_{\natural}}>0$, $u(\vec v)=(1-\vec v)(1+\vec v)^{-1}$ and $\vec v$ a pure quaternion. The coordinate is $\vec v=(1-u)(1+u)^{-1}=(r-\tilde q)(r+\tilde q)^{-1}$, and the chart is a bijection from the pure subspace onto the unit sphere minus $-1$.

The chart is rational in both directions and misses the unit factor $-1$, so the decomposition is defined on $\mathbb{H}\setminus(-\infty,0]$. A second chart, $-u(\vec v)=u(\vec v^{-1})$, supplies $-1$ and misses $+1$; the two charts cover the sphere. The group law is the sandwich $\vec v_3=(1+\vec v_1)^{-1}(\vec v_1+\vec v_2)(1+\vec v_1\vec v_2)^{-1}(1+\vec v_1)$, which is the bare fraction conjugated by $1+\vec v_1$; the pole is $\vec v_1\vec v_2=-1$, where the product is the missing point and the coordinate escapes. In the matrix picture the chart is the Cayley transform $M(\vec v)=(I-V)(I+V)^{-1}$ into $SU(2)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{H}$ | the quaternion algebra, basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$ |
| $\tilde q=q_t e_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ | a quaternion |
| $\tilde q^{\natural}$ | the quaternion conjugate |
| $\langle\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | the quaternion norm, positive definite |
| $r=\sqrt{\langle\tilde q\rangle_{\natural}}$ | the modulus |
| $\tilde u_{\mathrm r}=\tilde q/r$ | the unit factor |
| $\mathrm{Sp}(1)=S^3$ | the unit sphere |
| $\vec v=v_x\vec e_x+v_y\vec e_y+v_z\vec e_z$ | a pure quaternion, the chart coordinate |
| $u(\vec v)=(1-\vec v)(1+\vec v)^{-1}$ | the chart, a unit quaternion |
| $\vec v=(1-u)(1+u)^{-1}$ | the inverse chart |
| $\mathbb{H}\setminus(-\infty,0]$ | the domain of the chart decomposition |
| $\vec v_3=(1+\vec v_1)^{-1}(\vec v_1+\vec v_2)(1+\vec v_1\vec v_2)^{-1}(1+\vec v_1)$ | the group law in the coordinate |
| $V=\iota(\vec v)$ | the skew-Hermitian matrix of $\vec v$ |
| $M(\vec v)=(I-V)(I+V)^{-1}$ | the Cayley transform into $SU(2)$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the Cayley transform and the polar decomposition of an invertible matrix.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $SU(2)$, the Cayley transform and the unit quaternions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition 2001), for the quaternion algebra and its exponential and rational parametrisations.
- Michael Artin, *Algebra* (Prentice Hall, 2nd edition 2011), for the Cayley transform of an associative algebra and the group law it induces.

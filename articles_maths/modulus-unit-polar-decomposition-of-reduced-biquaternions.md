# __Modulus–Unit Polar Decomposition of Reduced Biquaternions__

## Introduction

This article treats the **modulus–unit polar decomposition** of a reduced biquaternion: the writing

$$
\boxed{\;
\breve Q=\breve r\,u,\qquad \breve r\in P,\qquad u\in T^2
\;},
$$

with $\breve r$ the **modulus** and $u$ the **unit factor**. The modulus is not a real number: it is an element of the **positive cone**

$$
P=\{\,x+jy:x>|y|\,\}
$$

of the plane $\mathbb{R}\{1,j\}$, the interior of the light cone of the split-complex plane. The unit factor is a point of the **unit torus**

$$
T^2=\{\,u:u\bar u=1\,\},
$$

the two-dimensional group of elements whose two circular components have modulus one. The decomposition carries four real parameters, two for the modulus and two for the torus, which is the real dimension of the algebra.

The decomposition is the polar decomposition of the algebra for the coefficient conjugation. The **bar** fixes $1$ and $j$ and conjugates the complex coefficients, and the modulus is the unique positive square root

$$
\breve r=\sqrt{\breve Q\bar{\breve Q}}
$$

taken in the cone $P$, the unit factor being $u=\breve r^{-1}\breve Q$, which satisfies $u\bar u=1$. In the complex algebra the same formulas read $r=\sqrt{Q\bar Q}$ and $u=Q/r$; the difference is that the positive square root now lives in a two-dimensional cone, not in a ray, and that the unit factor runs on a two-torus, not on a circle.

In the coordinates $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ the two circular components are the two complex numbers $Q_{+}$ and $Q_{-}$. The modulus–unit decomposition is therefore a pair of complex modulus–unit decompositions, written in the algebra. This is the source of every difference from the complex case: the modulus is doubled, the phase is doubled, the unit factor is a torus, and the failure set is the union of two real two-planes rather than the origin alone.

The decomposition is the algebraic member of the three polar decompositions of the algebra. The modulus–unit form, treated here, uses the bar, the positive square root and the unit torus, and chooses no coordinate on the torus. The rational-chart form puts the Cayley coordinate on each circle of the torus, and is developed in *Rational-Chart Polar Decomposition of Reduced Biquaternions*. The exponential form puts the Lie-algebra coordinate on the torus, and is developed in *Exponential Polar Decomposition of Reduced Biquaternions*.

The plan is as follows. The two factors are defined (§*The Two Factors*), existence and uniqueness are proved (§*Existence and Uniqueness*), the group of units and the torus are described (§*The Group of Units and the Torus*), the two planes of the bar are classified (§*The Two Axes*), the matrix picture is given (§*The Matrix Picture*), examples are computed (§*Worked Examples*), and the place of the algebra in the family is recorded (§*The Other Algebras*).

Every numerical value displayed below was recomputed in double precision.

## The Two Factors

### The Norm and the Modulus

Let $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ with $Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}$. The **bar** is the involution

$$
\overline{Q_{\blacktriangle}+jQ_{\blacktriangledown}}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}.
$$

It fixes $1$ and $j$ and negates $i$ and $ij$. The algebra carries two quadratic norms. The **reduced norm** is

$$
\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=Q_{+}Q_{-},
$$

complex-valued, multiplicative, and vanishing exactly on the two complex lines $Q_{\blacktriangle}=Q_{\blacktriangledown}$ and $Q_{\blacktriangle}=-Q_{\blacktriangledown}$, that is on the zero divisors. The **squared Euclidean norm** is

$$
\langle\breve Q\rangle_{\mathrm{ts}*}=|Q_{\blacktriangle}|^2+|Q_{\blacktriangledown}|^2,
$$

real and positive definite. Neither form is the modulus: the first is complex and vanishes on the zero divisors, the second is real but is not multiplicative.

The product $\breve Q\bar{\breve Q}$ is computed from the bar:

$$
\breve Q\bar{\breve Q}=(Q_{\blacktriangle}+jQ_{\blacktriangledown})(\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown})
=\bigl(|Q_{\blacktriangle}|^2+|Q_{\blacktriangledown}|^2\bigr)+2j\operatorname{Re}(Q_{\blacktriangle}\bar Q_{\blacktriangledown})
=q+jq',
$$

with $q=|Q_{\blacktriangle}|^2+|Q_{\blacktriangledown}|^2$ and $q'=2\operatorname{Re}(Q_{\blacktriangle}\bar Q_{\blacktriangledown})$. The key identity is

$$
q^2-q'^2=|Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2|^2=|\langle\breve Q\rangle_{\mathrm{ts}}|^2.
$$

For a unit the right side is positive, so $q>|q'|$, and $\breve Q\bar{\breve Q}$ lies in the positive cone

$$
P=\{\,x+jy:x>|y|\,\}.
$$

The **modulus** is the unique element $\breve r\in P$ with

$$
\breve r^2=\breve Q\bar{\breve Q}.
$$

It is the positive square root of $\breve Q\bar{\breve Q}$ in the cone, the exact analogue of $r=\sqrt{Q\bar Q}$ in $\mathbb{C}$ with the positive ray replaced by the cone $P$. Explicitly, with $q$ and $q'$ as above,

$$
\breve r=\sqrt{\frac{q+\sqrt{q^2-q'^2}}{2}}
+j\,\operatorname{sgn}q'\sqrt{\frac{q-\sqrt{q^2-q'^2}}{2}},
$$

and the sign convention is immaterial when $q'=0$. The two coordinates of $\breve r$ are real, so $\bar{\breve r}=\breve r$.

**Proposition (the two scales).** Write $\breve r=x+jy$ with $x,y\in\mathbb{R}$, and put

$$
\rho_+=x+y>0,\qquad \rho_-=x-y>0.
$$

Then

$$
\rho_+=|Q_{+}|,\qquad \rho_-=|Q_{-}|,\qquad \rho_+\rho_-=\sqrt{q^2-q'^2}=|\langle\breve Q\rangle_{\mathrm{ts}}|.
$$

Conversely,

$$
\breve r=\frac{\rho_++\rho_-}{2}+j\,\frac{\rho_+-\rho_-}{2}
=\rho\bigl(\cosh\phi+j\sinh\phi\bigr),
\qquad
\rho=\sqrt{\rho_+\rho_-},\qquad \phi=\operatorname{artanh}\frac{\rho_+-\rho_-}{\rho_++\rho_-}.
$$

*Proof.* Since $\breve r^2=q+jq'$ and $\breve r^2=(x^2+y^2)+2xyj$, one has $x^2+y^2=q$ and $2xy=q'$. Hence

$$
(x+y)^2=x^2+y^2+2xy=q+q'=|Q_{+}|^2,
$$

because $|Q_{+}|^2=|Q_{\blacktriangle}|^2+|Q_{\blacktriangledown}|^2+2\operatorname{Re}(Q_{\blacktriangle}\bar Q_{\blacktriangledown})=q+q'$; and similarly $(x-y)^2=q-q'=|Q_{-}|^2$. Both $x\pm y$ are positive because $x>|y|$, so $\rho_\pm=|Q_{\pm}|$. The product is $\rho_+\rho_-=x^2-y^2=\sqrt{q^2-q'^2}$. The parametrisation is the identity $\cosh\phi\pm\sinh\phi=e^{\pm\phi}$ applied to $\rho_\pm=\rho e^{\pm\phi}$.

The modulus therefore carries two positive scales, $\rho_+$ and $\rho_-$. The reduced norm sees only their product $\rho_+\rho_-$, and the Euclidean norm only their sum of squares $\rho_+^2+\rho_-^2$; neither form distinguishes the two scales from their interchange, and the pair carries the sign of the boost, which both forms lose. No scalar modulus exists, and the modulus is genuinely two-dimensional.

### The Unit Factor and the Torus

The **unit factor** is

$$
u=\breve r^{-1}\breve Q.
$$

Since $\bar{\breve r}=\breve r$ and $\breve r^2=\breve Q\bar{\breve Q}$,

$$
u\bar u=\breve r^{-1}\bar{\breve r}^{-1}\breve Q\bar{\breve Q}
=\breve r^{-2}\breve r^2=1.
$$

The set of such elements is the **unit torus**

$$
T^2=\{\,u\in\mathbb{B}_{\mathrm{r}}:u\bar u=1\,\}.
$$

It is a group under multiplication: if $u\bar u=v\bar v=1$ then $(uv)\overline{(uv)}=uv\bar u\bar v=1$, and the inverse of $u$ is $\bar u$. It is closed and bounded in $\mathbb{B}_{\mathrm{r}}\cong\mathbb{R}^4$, hence compact.

**Proposition (the torus as a product of two circles).** Let $u=u_{\blacktriangle}+ju_{\blacktriangledown}$. Then

$$
u\bar u=1\quad\Longleftrightarrow\quad |u_{+}|=|u_{-}|=1.
$$

The map

$$
u\longmapsto(u_{+},\ u_{-})
$$

is a bijection from $T^2$ onto $S^1\times S^1$, with inverse

$$
u_{\blacktriangle}=\frac{u_{+}+u_{-}}{2},\qquad u_{\blacktriangledown}=\frac{u_{+}-u_{-}}{2},\qquad u_{+}=u_{\blacktriangle}+u_{\blacktriangledown},\quad u_{-}=u_{\blacktriangle}-u_{\blacktriangledown}.
$$

*Proof.* From the computation of $u\bar u$, the condition $u\bar u=1$ is $|u_{\blacktriangle}|^2+|u_{\blacktriangledown}|^2=1$ and $\operatorname{Re}(u_{\blacktriangle}\bar u_{\blacktriangledown})=0$. Then

$$
|u_{\pm}|^2=|u_{\blacktriangle}|^2+|u_{\blacktriangledown}|^2\pm2\operatorname{Re}(u_{\blacktriangle}\bar u_{\blacktriangledown})=1.
$$

Conversely, if $|u_{+}|=|u_{-}|=1$, adding the two squared identities gives $2(|u_{\blacktriangle}|^2+|u_{\blacktriangledown}|^2)=2$ and subtracting gives $4\operatorname{Re}(u_{\blacktriangle}\bar u_{\blacktriangledown})=0$, so $u\bar u=1$. The inverse formula is the linear change $(u_{\blacktriangle},u_{\blacktriangledown})\leftrightarrow(u_{+},u_{-})$.

The torus is therefore the product of the two circles $|u_{+}|=1$ and $|u_{-}|=1$, and it is two-dimensional. In the coordinates $(u_{\blacktriangle},u_{\blacktriangledown})\in\mathbb{C}^2\cong\mathbb{R}^4$ it is described by the single complex equation $u\bar u=1$, that is by the two real equations $|u_{\blacktriangle}|^2+|u_{\blacktriangledown}|^2=1$ and $\operatorname{Re}(u_{\blacktriangle}\bar u_{\blacktriangledown})=0$.

**Proposition (the torus is not a norm-one set).** The reduced-norm-one set $\{\breve Q:\langle\breve Q\rangle_{\mathrm{ts}}=1\}$ is $\{Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=1\}$, a complex quadric of real dimension two, non-compact. The Euclidean unit sphere $S^3=\{\langle\breve Q\rangle_{\mathrm{ts}*}=1\}$ contains the zero divisor $Q_{\blacktriangle}=Q_{\blacktriangledown}=1/\sqrt2$, and is not a group. The unit factor is the bar-unitary torus, neither the reduced-norm-one set nor the Euclidean sphere.

*Proof.* The reduced-norm-one set is the level set of a holomorphic function, of real dimension two; it contains the unbounded curve $Q_{\blacktriangle}=\cosh t$, $Q_{\blacktriangledown}=\sinh t$. The point $Q_{\blacktriangle}=Q_{\blacktriangledown}=1/\sqrt2$ lies on $S^3$ and is a zero divisor, since $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=0$. The bar-unitary set is compact and closed under multiplication by the proposition above.

The three sets coincide only in the complex algebra, where the norm is definite and the unit factor is one circle. Here the reduced norm is complex, the Euclidean norm is not multiplicative, and only the bar-unitary condition gives a compact group.

### The Count of the Parameters

A unit carries four real parameters. The modulus carries two, the scales $\rho_+,\rho_-$, equivalently the radius $\rho>0$ and the boost $\phi\in\mathbb{R}$. The unit factor carries two, the two circles of $T^2$. The counts add:

$$
4=2+2.
$$

The cone $P$ is non-compact, the torus $T^2$ is compact, and the product is the group of units. The decomposition separates the non-compact directions from the compact ones, exactly as the complex decomposition separates the radius from the circle. What the two parameters of $u$ are parametrised by is a separate question, answered by a chart of the torus; the rational chart is the subject of *Rational-Chart Polar Decomposition of Reduced Biquaternions*, the exponential chart the subject of *Exponential Polar Decomposition of Reduced Biquaternions*, and this article chooses none.

## Existence and Uniqueness

**Theorem.** Every unit $\breve Q$ has exactly one modulus–unit polar decomposition $\breve Q=\breve r u$ with $\breve r\in P$ and $u\in T^2$.

**Existence.** Put $\breve r=\sqrt{\breve Q\bar{\breve Q}}$ in $P$ and $u=\breve r^{-1}\breve Q$. The element $\breve r$ is defined because $\breve Q\bar{\breve Q}\in P$ for a unit, and $u\bar u=1$ by the computation of §*The Unit Factor and the Torus*. Hence $\breve Q=\breve r u$ with the two factors in the required sets.

**Uniqueness.** Suppose $\breve r u=\breve r'u'$ with $\breve r,\breve r'\in P$ and $u\bar u=u'\bar u'=1$. Multiplying by the bar gives $\breve r^2=\breve r'^2$, because $\bar{\breve r}=\breve r$, $\bar{\breve r}'=\breve r'$ and $u\bar u=u'\bar u'=1$. Two elements of $P$ with the same square are equal: if $x+jy\in P$ and $x'+jy'\in P$ have square $q+jq'$, then $x^2+y^2=x'^2+y'^2=q$ and $xy=x'y'=q'/2$; the positive numbers $x^2-y^2$ and $x'^2-y'^2$ both equal $\sqrt{q^2-q'^2}$, so $x^2=x'^2$, $x=x'>0$, and then $y=y'$. Hence $\breve r=\breve r'$, and $u=\breve r^{-1}\breve Q=u'$.

The pair $(\breve r,u)$ is unique. This is a statement about the factorisation, not about a coordinate on the torus: two different charts of $T^2$ assign different parameters to the same unit factor.

**Corollary (the failure set).** The decomposition exists exactly on the units. It fails exactly on the zero divisors

$$
\boxed{\;
\{Q_{\blacktriangle}^2=Q_{\blacktriangledown}^2\}=\{Q_{\blacktriangle}=Q_{\blacktriangledown}\}\cup\{Q_{\blacktriangle}=-Q_{\blacktriangledown}\}
\;},
$$

the union of the two complex lines $\mathbb{C}(1+j)$ and $\mathbb{C}(1-j)$, each of real dimension two. The failure set has real codimension two, as the origin does in $\mathbb{C}$.

*Proof.* The construction uses $\breve r\in P$, which requires $q^2-q'^2>0$, that is $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0$. The vanishing of $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ is the vanishing of $Q_{+}Q_{-}$, the two lines named.

## The Group of Units and the Torus

### The Splitting of the Group of Units

The map

$$
\Phi:\mathbb{B}_{\mathrm{r}}^{\times}\longrightarrow P\times T^2,\qquad \Phi(\breve Q)=\bigl(\breve r,u\bigr),
$$

is a group isomorphism. It is bijective by the theorem of §*Existence and Uniqueness*, with inverse $(\breve r,u)\mapsto\breve r u$, and it is a homomorphism because the modulus of a product is the product of the moduli and the unit factor of a product is the product of the unit factors:

$$
\breve r(\breve Q_1\breve Q_2)=\breve r(\breve Q_1)\breve r(\breve Q_2),\qquad
u(\breve Q_1\breve Q_2)=u(\breve Q_1)u(\breve Q_2).
$$

The first identity follows from $(\breve Q_1\breve Q_2)\overline{(\breve Q_1\breve Q_2)}=\breve Q_1\bar{\breve Q}_1\breve Q_2\bar{\breve Q}_2=\breve r_1^2\breve r_2^2$ and from $\breve r_1\breve r_2\in P$; the second is the definition of $u$ and the cancellation of the moduli.

Since $P\cong\mathbb{R}_{>0}\times\mathbb{R}$ under $(\rho,\phi)\mapsto\rho(\cosh\phi+j\sinh\phi)$, and $T^2\cong S^1\times S^1$,

$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{R}_{>0}\times\mathbb{R}\times T^2\cong\mathbb{R}^2\times T^2.
$$

**Corollary (the real dimension and the fundamental group).** The group of units is connected of real dimension four, with fundamental group $\mathbb{Z}^2$. It is not simply connected, and its universal cover is the algebra $\mathbb{B}_{\mathrm{r}}\cong\mathbb{R}^4$.

*Proof.* The cone is connected and simply connected, the torus is connected with fundamental group $\mathbb{Z}^2$, and the product has the product of the fundamental groups. The algebra is contractible and the exponential of *Exponential Polar Decomposition of Reduced Biquaternions* is a covering onto the units with kernel $\mathbb{Z}^2$.

### The Maximal Compact Subgroup

**Theorem.** The torus $T^2$ is the maximal compact subgroup of $\mathbb{B}_{\mathrm{r}}^{\times}$.

*Proof.* Let $K\subset\mathbb{B}_{\mathrm{r}}^{\times}$ be a compact subgroup. The modulus map $\breve Q\mapsto\breve r$ is a continuous homomorphism onto $P$, so its image is a compact subgroup of $P$. A compact subgroup of $P$ is trivial: in the coordinates $(\rho,\phi)$ of $P\cong\mathbb{R}_{>0}\times\mathbb{R}$, a nontrivial element has $\phi\neq0$ or $\rho\neq1$; its powers have $|n\phi|\to\infty$ or $\rho^n\to0$ or $\infty$, and no such sequence stays in a compact set. Hence every element of $K$ has modulus $1$, that is $K\subset T^2$. The torus is compact, so it is maximal.

The compact factor is two-dimensional, not one-dimensional as in $\mathbb{C}$ and not zero-dimensional as in the split-complex algebra. The rank of the compact group is two.

### The Deformation Retraction

The map

$$
H:[0,1]\times\mathbb{B}_{\mathrm{r}}^{\times}\longrightarrow\mathbb{B}_{\mathrm{r}}^{\times},
\qquad H(t,\breve Q)=\bigl((1-t)\breve r+t\bigr)u
$$

is continuous, fixes $T^2$ at every $t$, is the identity at $t=0$, and lands in $T^2$ at $t=1$. The element $(1-t)\breve r+t$ lies in $P$ for every $t$, because $P$ is convex: its coordinates are $(1-t)x+t$ and $(1-t)y$, and $|(1-t)y|<(1-t)x+t$. The group of units therefore deformation retracts onto the torus. Since the group is already a product $P\times T^2$, the retraction is the projection onto the second factor followed by a linear contraction of the first.

### The Two Circles

The torus contains the two circles

$$
S_i=\{\exp(i\alpha):\alpha\in\mathbb{R}\},\qquad
S_{ij}=\{\exp(ij\beta):\beta\in\mathbb{R}\},
$$

the **scalar circle** and the **$ij$-circle**. Their elements are

$$
\exp(i\alpha)=\cos\alpha+i\sin\alpha,\qquad
\exp(ij\beta)=\cos\beta+ij\sin\beta.
$$

Every element of $T^2$ is a product $\exp(i\alpha)\exp(ij\beta)=\exp(i\alpha+ij\beta)$, and the parametrisation is a group homomorphism from $\mathbb{R}^2$ onto $T^2$ whose kernel is the lattice

$$
2\pi\mathbb{Z}^2+\pi\mathbb{Z}(1,1).
$$

The two circles intersect at $\exp(i\alpha)=\exp(ij\beta)$, that is at $\alpha,\beta\in\pi\mathbb{Z}$ with the same parity, which gives the two points $1$ and $-1$. The product map $S_i\times S_{ij}\to T^2$ is therefore not injective: it is a two-to-one covering, and $T^2$ is the quotient of $S^1\times S^1$ by the involution $(z,w)\mapsto(-z,-w)$.

The genuine splitting of the torus is the map $u\mapsto(u_{+},u_{-})$ of §*The Unit Factor and the Torus*, which is a bijection onto $S^1\times S^1$. The two circles $S_i$ and $S_{ij}$ generate the torus, but they are not independent; the two circular components $u_{+}$ and $u_{-}$ are.

**Corollary (the Clifford torus).** The torus $T^2$ lies in the Euclidean unit sphere $S^3$, and it is the Clifford torus

$$
T^2=\{\,|u_{+}|=|u_{-}|\,\}\cap S^3
$$

in it. The sphere is three-dimensional and the torus is two-dimensional; the remaining direction is the difference $|u_{+}|-|u_{-}|$, which the torus sets to zero.

*Proof.* On $T^2$ one has $|u_{+}|=|u_{-}|=1$ and $|u_{\blacktriangle}|^2+|u_{\blacktriangledown}|^2=1$, so $T^2\subset S^3$. Conversely, on $S^3$ one has $|u_{+}|^2+|u_{-}|^2=2(|u_{\blacktriangle}|^2+|u_{\blacktriangledown}|^2)=2$, so the single equation $|u_{+}|=|u_{-}|$ forces both moduli to be $1$, which is the torus. The remaining direction is the difference of the two moduli.

### Multiplication, Powers and Roots

**Theorem (the product in polar form).** For two units

$$
\breve Q_1=\breve r_1u_1,\qquad \breve Q_2=\breve r_2u_2,
$$

the product is

$$
\breve Q_1\breve Q_2=(\breve r_1\breve r_2)(u_1u_2),
$$

with $\breve r_1\breve r_2\in P$ and $u_1u_2\in T^2$. In the scales and the circular components,

$$
\rho_+(\breve Q_1\breve Q_2)=\rho_+(\breve Q_1)\rho_+(\breve Q_2),\qquad
\rho_-(\breve Q_1\breve Q_2)=\rho_-(\breve Q_1)\rho_-(\breve Q_2),
$$

and the phases add.

*Proof.* The product of the moduli lies in $P$, because $(x_1x_2+y_1y_2)^2-(x_1y_2+y_1x_2)^2=(x_1^2-y_1^2)(x_2^2-y_2^2)>0$ and the first coordinate is positive. The product of the unit factors lies in $T^2$, because $(u_1u_2)\overline{(u_1u_2)}=u_1\bar u_1u_2\bar u_2=1$. The scale identities follow from the product formula for $Q_{\pm}$.

**Corollary (powers and roots).** For a positive integer $n$,

$$
\breve Q^n=\breve r^n u^n,
$$

and the $n$-th roots of a unit have modulus $\breve r^{1/n}$ and $n^2$ choices of the unit factor. In particular a generic unit has four square roots.

*Proof.* The power is the repeated product. On the torus, an $n$-th root is a pair $(u_{+},u_{-})$ whose $n$-th powers are the two prescribed circular components of the target unit factor; each of the two complex equations has $n$ roots, and the choices are independent, giving $n^2$.

The unit group in polar form is the product of the cone and the torus, and the product law multiplies the scales and the unit factors. The algebra is commutative, so the unit factor carries no rotor: the compact directions are the two scalar phases, and the split unit $j$ acts only through the relative scale $\rho_+/\rho_-=e^{2\phi}$. This is the reason the polar word is a pair of complex polar words and not a richer object.

## The Two Axes

### The Bar and the Two Planes

The bar fixes $1$ and $j$ and negates $i$ and $ij$, so its fixed space is the **scale plane** $\mathbb{R}\{1,j\}$ and its anti-fixed space is the **angle plane** $\mathbb{R}\{i,ij\}$.

The algebra is the direct sum $\mathbb{B}_{\mathrm{r}}=\mathbb{R}\{1,j\}\oplus\mathbb{R}\{i,ij\}$, and the two planes are each of real dimension two. The modulus lies in $\mathbb{R}\{1,j\}$: it is bar-fixed and positive. The angle of the logarithm lies in $\mathbb{R}\{i,ij\}$: the exponent of *Exponential Polar Decomposition of Reduced Biquaternions* is $\breve Q_{\log}=\breve r_{\log}+i\Theta$ with $\breve r_{\log}=\ln\rho+j\phi\in\mathbb{R}\{1,j\}$ and $i\Theta=i\alpha+ij\beta\in\mathbb{R}\{i,ij\}$. The unit factor itself is not in $\mathbb{R}\{i,ij\}$; it is the exponential of an element of $\mathbb{R}\{i,ij\}$, and it winds around the torus.

### The Roots of Plus One, Zero and Minus One

Let $\breve R=R_{\blacktriangle}+jR_{\blacktriangledown}$ with $R_{\blacktriangle},R_{\blacktriangledown}\in\mathbb{C}$. Then

$$
\breve R^2=(R_{\blacktriangle}^2+R_{\blacktriangledown}^2)+2R_{\blacktriangle}R_{\blacktriangledown}\,j.
$$

The three scalar equations are solved directly.

| equation | roots in $\mathbb{B}_{\mathrm{r}}$ | plane | image of $t\mapsto\exp(\breve R t)$ |
|---|---|---|---|
| $\breve R^2=-1$ | $\pm i,\ \pm ij$ | $\mathbb{R}\{i,ij\}$ | two circles, generating $T^2$ |
| $\breve R^2=0$ | $0$ | — | $\{1\}$ |
| $\breve R^2=+1$ | $\pm1,\ \pm j$ | $\mathbb{R}\{1,j\}$ | $\mathbb{R}_{>0}$ for $\pm1$; the future branch of the hyperbola for $\pm j$ |

For $\breve R^2=-1$ the equations are $R_{\blacktriangle}^2+R_{\blacktriangledown}^2=-1$ and $R_{\blacktriangle}R_{\blacktriangledown}=0$. If $R_{\blacktriangle}=0$ then $R_{\blacktriangledown}^2=-1$, so $R_{\blacktriangledown}=\pm i$ and $\breve R=\pm ij$; if $R_{\blacktriangledown}=0$ then $R_{\blacktriangle}=\pm i$ and $\breve R=\pm i$. The four roots are the two scalar imaginary units and the two $ij$ directions. For $\breve R^2=+1$ the same computation with $R_{\blacktriangle}^2+R_{\blacktriangledown}^2=1$ gives $R_{\blacktriangle}=\pm1$ or $R_{\blacktriangledown}=\pm1$, that is $\breve R=\pm1$ or $\breve R=\pm j$. For $\breve R^2=0$ the equations $R_{\blacktriangle}^2+R_{\blacktriangledown}^2=0$ and $R_{\blacktriangle}R_{\blacktriangledown}=0$ force $R_{\blacktriangle}=R_{\blacktriangledown}=0$, so the algebra has no nilpotent direction.

The unit factor uses the roots of $-1$: $\exp(i\alpha)$ and $\exp(ij\beta)$ are the two circles. The modulus uses the roots of $+1$: the one-parameter subgroups $\exp(t)$ and $\exp(jt)$ give the two positive directions of the plane $\mathbb{R}\{1,j\}$, and their product is the cone $P$. This is the exact doubling of the complex case: the two roots $\pm i$ of $-1$ give one circle there and two circles here, and the two roots $\pm1$ of $+1$ give one ray there and a two-dimensional cone here.

### Position and Signature

The algebraic norm of the multiplication is

$$
\langle\breve Q\rangle=Q_{\blacktriangle}^2+Q_{\blacktriangledown}^2.
$$

On the scale plane $\mathbb{R}\{1,j\}$, for $\breve Q=q_{\blacktriangle}+jq_{\blacktriangledown}$ with $q_{\blacktriangle},q_{\blacktriangledown}\in\mathbb{R}$, it is $q_{\blacktriangle}^2+q_{\blacktriangledown}^2$, positive definite. On the angle plane $\mathbb{R}\{i,ij\}$, for $\breve Q=iq_{\blacktriangle}+ijq_{\blacktriangledown}$, it is $-(q_{\blacktriangle}^2+q_{\blacktriangledown}^2)$, negative definite. The algebraic norm therefore has real signature $(2,2)$, with $\mathbb{R}\{1,j\}$ the positive plane and $\mathbb{R}\{i,ij\}$ the negative plane. This is the form that sees the split of the algebra.

The reduced norm behaves differently. On $\mathbb{R}\{1,j\}$ it is $q_{\blacktriangle}^2-q_{\blacktriangledown}^2$, and on $\mathbb{R}\{i,ij\}$ it is $q_{\blacktriangledown}^2-q_{\blacktriangle}^2$; it is indefinite on both planes, with null lines $q_{\blacktriangle}=\pm q_{\blacktriangledown}$ in $\mathbb{R}\{1,j\}$, that is $\mathbb{R}(1\pm j)$, and their $i$-rotates $\mathbb{R}i(1\pm j)$ in $\mathbb{R}\{i,ij\}$. These four real lines are the real forms of the two complex zero-divisor lines.

**Remark (which form is used where).** The modulus–unit decomposition uses the bar and the positive square root of $\breve Q\bar{\breve Q}$, not the reduced norm and not the algebraic norm. The algebraic norm is recorded here because it is the form whose signature separates $\mathbb{R}\{1,j\}$ from $\mathbb{R}\{i,ij\}$; it does not decide invertibility, and it is not the norm of the polar decomposition.

## The Matrix Picture

### The Matrix of Multiplication

In the real basis $\{1,i,j,ij\}$ the left multiplication by $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, has the matrix

$$
M_{\breve Q}=
\begin{pmatrix}
q_{\blacktriangle}&-q'_{\blacktriangle}&q_{\blacktriangledown}&-q'_{\blacktriangledown}\\
q'_{\blacktriangle}&q_{\blacktriangle}&q'_{\blacktriangledown}&q_{\blacktriangledown}\\
q_{\blacktriangledown}&-q'_{\blacktriangledown}&q_{\blacktriangle}&-q'_{\blacktriangle}\\
q'_{\blacktriangledown}&q_{\blacktriangledown}&q'_{\blacktriangle}&q_{\blacktriangle}
\end{pmatrix}.
$$

Its transpose is the matrix of the bar:

$$
M_{\overline{\breve Q}}=M_{\breve Q}^{\mathsf T}.
$$

This is the matrix form of the identity $\overline{Q_{\blacktriangle}+jQ_{\blacktriangledown}}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$ in the real basis. In the complex basis $\{1,j\}$ the same matrix is the block matrix

$$
M_{\breve Q}=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$

acting on $(z,w)\in\mathbb{C}^2$ by $z+jw\mapsto(Q_{\blacktriangle}z+Q_{\blacktriangledown}w)+j(Q_{\blacktriangledown}z+Q_{\blacktriangle}w)$.

### The Matrix of a Unit

The modulus has the matrix

$$
M_{\breve r}=
\begin{pmatrix}
x&0&y&0\\
0&x&0&y\\
y&0&x&0\\
0&y&0&x
\end{pmatrix},
\qquad \breve r=x+jy,
$$

symmetric with eigenvalues $x+y=\rho_+$ and $x-y=\rho_-$, each repeated twice; it is positive definite because both are positive.

The unit factor has the matrix $M_u$, and the bar identity gives

$$
M_u^{\mathsf T}M_u=M_{\bar u}M_u=M_{\bar u u}=M_1=I.
$$

Its determinant is the determinant of the complex matrix $\begin{pmatrix}u_{\blacktriangle}&u_{\blacktriangledown}\\u_{\blacktriangledown}&u_{\blacktriangle}\end{pmatrix}$, which is $u_{\blacktriangle}^2-u_{\blacktriangledown}^2$, read in the real basis:

$$
\det M_u=|u_{\blacktriangle}^2-u_{\blacktriangledown}^2|^2=|u_{+}|^2|u_{-}|^2=1.
$$

Hence $M_u$ lies in the special orthogonal group $SO(4)$. The map $u\mapsto M_u$ is an injective homomorphism, and its image is a maximal torus of $SO(4)$.

The decomposition of matrices is therefore

$$
M_{\breve Q}=M_{\breve r}M_u,
$$

with $M_{\breve r}$ symmetric positive definite and $M_u\in SO(4)$.

### The Matrix Polar Decomposition

**Theorem.** For every unit $\breve Q$, the matrix $M_{\breve Q}$ has the polar decomposition

$$
\boxed{\;
M_{\breve Q}=P U,\qquad P=M_{\breve r}=(M_{\breve Q}M_{\breve Q}^{\mathsf T})^{1/2},\quad U=M_u
\;},
$$

with $P$ symmetric positive definite and $U$ orthogonal. The factors are unique.

*Proof.* The identity $M_{\overline{\breve Q}}=M_{\breve Q}^{\mathsf T}$ gives $M_{\breve Q}M_{\breve Q}^{\mathsf T}=M_{\breve Q\overline{\breve Q}}=M_{\breve r^2}=M_{\breve r}^2$. The matrix $M_{\breve r}$ is symmetric with positive eigenvalues $\rho_+,\rho_+,\rho_-,\rho_-$, so it is the positive square root. The matrix $M_u=M_{\breve r}^{-1}M_{\breve Q}$ is orthogonal, because $M_uM_u^{\mathsf T}=M_{\breve r}^{-1}M_{\breve Q}M_{\breve Q}^{\mathsf T}M_{\breve r}^{-1}=I$. Uniqueness is the uniqueness of the positive square root and of the polar decomposition of an invertible matrix.

The general polar decomposition of an invertible real $4\times4$ matrix $X$ is $X=M_+U$ with $M_+=(XX^{\mathsf T})^{1/2}$ and $U=M_+^{-1}X$. For $X=M_{\breve Q}$ the two factors collapse to the form above, because $M_{\breve Q}$ is the sum of two conformal blocks. The singular values of $M_{\breve Q}$ are $\rho_+,\rho_+,\rho_-,\rho_-$: each scale is repeated twice. The matrix is conformal exactly when $\rho_+=\rho_-$; otherwise it has two distinct singular values, and it is only block-conformal.

## Worked Examples

### A Generic Element

Take $\breve Q=3+4i+j(1-i)$, that is $Q_{\blacktriangle}=3+4i$ and $Q_{\blacktriangledown}=1-i$. Then

$$
Q_{+}=4+3i,\qquad Q_{-}=2+5i,
$$

so

$$
\rho_+=|Q_{+}|=5,\qquad \rho_-=|Q_{-}|=\sqrt{29}=5.385164807134504.
$$

The squared Euclidean norm and the reduced norm are

$$
q=|Q_{\blacktriangle}|^2+|Q_{\blacktriangledown}|^2=25+2=27,\qquad
q'=2\operatorname{Re}(Q_{\blacktriangle}\bar Q_{\blacktriangledown})=2\operatorname{Re}\bigl((3+4i)(1+i)\bigr)=-2,
$$

and

$$
\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=(4+3i)(2+5i)=-7+26i,
$$

of modulus $\sqrt{49+676}=\sqrt{725}=\rho_+\rho_-$.

The modulus is

$$
\breve r=\sqrt{\frac{q+\sqrt{725}}{2}}+j\,\operatorname{sgn}(q')\sqrt{\frac{q-\sqrt{725}}{2}}
=5.192582403567252-0.192582403567252\,j,
$$

whose coordinates are $x=(\rho_++\rho_-)/2=5.192582403567252$ and $y=(\rho_+-\rho_-)/2=-0.192582403567252$. The unit factor has the circular components

$$
(Q_{+})/\rho_+=0.8+0.6i,\qquad (Q_{-})/\rho_-=\frac{2+5i}{\sqrt{29}}=0.371390676354104+0.928476690885259\,i.
$$

### The Hyperbolic Line

For $\breve Q=\exp(j\phi)=\cosh\phi+j\sinh\phi$ the coefficients are $Q_{\blacktriangle}=\cosh\phi$ and $Q_{\blacktriangledown}=\sinh\phi$, so

$$
Q_{+}=e^{\phi},\qquad Q_{-}=e^{-\phi},\qquad
\rho_+=e^{\phi},\qquad \rho_-=e^{-\phi}.
$$

The modulus is

$$
\breve r=\frac{e^{\phi}+e^{-\phi}}{2}+j\,\frac{e^{\phi}-e^{-\phi}}{2}=\cosh\phi+j\sinh\phi=\breve Q,
$$

and the unit factor is $1$. The relative scale is

$$
\frac{\rho_+}{\rho_-}=e^{2\phi},
$$

which is the boost parameter of the split-complex companion. There is no separate boost factor: the split unit $j$ is absorbed into the two scales, and the boost is their ratio.

### The Zero Divisors

For $\breve Q=1+j$ the coefficients are $Q_{\blacktriangle}=Q_{\blacktriangledown}=1$, so $Q_{-}=0$ and $\rho_-=0$: the element lies on the line $Q_{\blacktriangle}=Q_{\blacktriangledown}$ and has no modulus–unit decomposition, because the second scale would have to be positive and it is zero. For $\breve Q=1-j$ the coefficients are $Q_{\blacktriangle}=1$, $Q_{\blacktriangledown}=-1$, so $Q_{+}=0$ and the decomposition fails in the other scale.

The element $j$ is not a zero divisor: $Q_{\blacktriangle}=0$ and $Q_{\blacktriangledown}=1$, so $Q_{+}=1$ and $Q_{-}=-1$, both of modulus one, and

$$
j=1\cdot j
$$

with modulus $1$ and unit factor $j$.

### A Table of Examples

| $\breve Q$ | $Q_{+}$ | $Q_{-}$ | $\rho_+$ | $\rho_-$ | unit factor |
|---|---|---|---|---|---|
| $3+4i+j(1-i)$ | $4+3i$ | $2+5i$ | $5$ | $\sqrt{29}$ | $0.8+0.6i$ and $(2+5i)/\sqrt{29}$ |
| $1+i$ | $1+i$ | $1+i$ | $\sqrt2$ | $\sqrt2$ | $e^{i\pi/4}$ |
| $i$ | $i$ | $i$ | $1$ | $1$ | $i$ |
| $ij$ | $i$ | $-i$ | $1$ | $1$ | $ij$ |
| $j$ | $1$ | $-1$ | $1$ | $1$ | $j$ |
| $\exp(j\ln2)$ | $2$ | $1/2$ | $2$ | $1/2$ | $1$ |
| $-1$ | $-1$ | $-1$ | $1$ | $1$ | $-1$ |
| $1+j$ | $2$ | $0$ | $2$ | $0$ | — |

The row $1+i$ is the diagonal case: the two circular components are equal, so the modulus is the scalar $\sqrt2$ and the unit factor is the scalar $e^{i\pi/4}$; the reduced biquaternion decomposition reduces to the complex one. The row $ij$ is the pure $ij$-phase. The row $1+j$ is the zero divisor, where the decomposition does not exist.

### The Reconstruction Error

For the generic element, the reconstruction from the displayed data gives

$$
\breve r u-(3+4i+j(1-i))
$$

of Euclidean norm $1.7\times10^{-15}$ in double precision: the displayed scales round-trip to $4+3i$ and $2+5i$ up to the last bit. The reconstruction is exact in exact arithmetic, because it is the complex reconstruction in the two circular components.

## The Other Algebras

The modulus–unit decomposition exists in every algebra of the family, with the unit set of the norm in view.

| algebra | element | norm | modulus | unit set | topology of the unit set |
|---|---|---|---|---|---|
| $\mathbb{R}$ | $q$ | $q^2$ | $\lvert q\rvert$ | $\{\pm1\}$ | two points |
| $\mathbb{C}$ | $Q=q+iq'$ | $q^2+q'^2$, definite | $\sqrt{N}$ | $\mathrm{U}(1)$ | circle, compact and connected |
| $\mathbb{D}$ | $Q=q+jq'$ | $q^2-q'^2$, indefinite | $\sqrt{\lvert N\rvert}$, $N\neq0$ | $\{N=\pm1\}$ | four branches, non-compact |
| $\mathbb{H}$ | $\tilde q$ | sum of four squares, definite | $\sqrt{N}$ | $S^3$ | sphere, compact and connected |
| $\mathbb{B}_{\mathrm{r}}$ | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$, complex, multiplicative | the pair $(\rho_+,\rho_-)$ | $T^2$ | two-torus, compact and connected |

The reduced biquaternion column is the only one in which the modulus is two-dimensional and the unit set is a product of two circles. The reduced norm is complex, so no scalar modulus exists; the Euclidean norm is real but does not give a group; the bar-unitary condition gives the compact torus. The failure set is the union of two real two-planes, of codimension two, as the origin is in $\mathbb{C}$; the split-complex failure set is the null cone, of codimension one.

## Summary

Every unit $\breve Q$ has exactly one modulus–unit polar decomposition

$$
\breve Q=\breve r u,\qquad \breve r=\frac{\rho_++\rho_-}{2}+j\,\frac{\rho_+-\rho_-}{2},\qquad u\bar u=1,
$$

with $\rho_+=|Q_{+}|>0$ and $\rho_-=|Q_{-}|>0$. The modulus is the positive square root $\breve r=\sqrt{\breve Q\bar{\breve Q}}$ in the cone $P=\{x+jy:x>|y|\}$, and the unit factor is $u=\breve r^{-1}\breve Q$ on the torus $T^2=\{u:u\bar u=1\}$. The pair is unique. The decomposition exists exactly on the units and fails exactly on the zero divisors, the union of the two complex lines $Q_{\blacktriangle}=Q_{\blacktriangledown}$ and $Q_{\blacktriangle}=-Q_{\blacktriangledown}$, of real codimension two.

The group of units splits as

$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong P\times T^2\cong\mathbb{R}^2\times T^2,
$$

connected of real dimension four, with fundamental group $\mathbb{Z}^2$. The torus is the maximal compact subgroup and a deformation retract. The compact factor has rank two, the scalar circle and the $ij$-circle, and the two circles meet at $\pm1$.

The modulus is two-dimensional because the reduced norm is complex: it fixes only the product $\rho_+\rho_-=|\langle\breve Q\rangle_{\mathrm{ts}}|$, the Euclidean norm only the sum of squares $\rho_+^2+\rho_-^2$, and the sign of the boost is lost by both. The bar splits the algebra into the scale plane $\mathbb{R}\{1,j\}$ and the angle plane $\mathbb{R}\{i,ij\}$; the modulus lies in $\mathbb{R}\{1,j\}$, the logarithm of the unit factor in $\mathbb{R}\{i,ij\}$, and the algebraic norm has signature $(2,2)$ with $\mathbb{R}\{1,j\}$ positive and $\mathbb{R}\{i,ij\}$ negative.

In the matrix picture the decomposition is the polar decomposition

$$
M_{\breve Q}=M_{\breve r}M_u,
$$

with positive definite $M_{\breve r}$ with eigenvalues $\rho_+,\rho_+,\rho_-,\rho_-$ and orthogonal $M_u\in SO(4)$. The singular values are $\rho_+,\rho_+,\rho_-,\rho_-$, and the matrix is conformal exactly when the two scales are equal.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}$ | the reduced biquaternion algebra, basis $1,i,j,ij$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | an element, $Q_{\blacktriangle}$ the scalar part, $Q_{\blacktriangledown}$ the split part |
| $\bar{\breve Q}=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}$ | the bar |
| $Q_{+}$, $Q_{-}$ | the two circular components |
| $\langle\breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2$ | the reduced norm |
| $\langle\breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2$ | the squared Euclidean norm |
| $P=\{x+jy:x>\lvert y\rvert\}$ | the positive cone of the modulus |
| $\breve r=\sqrt{\breve Q\bar{\breve Q}}$ | the modulus, an element of $P$ |
| $\rho_+=\lvert Q_{+}\rvert$, $\rho_-=\lvert Q_{-}\rvert$ | the two scales |
| $\breve r=\rho(\cosh\phi+j\sinh\phi)$ | the modulus in radius and boost |
| $u=\breve r^{-1}\breve Q$ | the unit factor |
| $T^2=\{u:u\bar u=1\}$ | the unit torus |
| $\mathbb{B}_{\mathrm{r}}^{\times}\cong P\times T^2$ | the polar splitting of the group of units |
| $\mathbb{R}\{1,j\}$, $\mathbb{R}\{i,ij\}$ | the fixed and anti-fixed planes of the bar |
| $M_{\breve Q}$ | the real matrix of multiplication by $\breve Q$ |
| $SO(4)$ | the special orthogonal group of $\mathbb{R}^4$ |

## Further Reading

- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the reduced norm and the unit criterion.
- [Zero Divisors of the Algebra of the Reduced Biquaternions](zero-divisors-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two zero-divisor lines.
- [The Group of Units of the Algebra of the Reduced Biquaternions](the-group-of-units-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the structure of $\mathbb{B}_{\mathrm{r}}^{\times}$.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), for the bar and its fixed planes.
- [Square Roots of a General Element in the Algebra of the Reduced Biquaternions](square-roots-of-a-general-element-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the four square roots.
- [Modulus–Unit Polar Decomposition of Complex Numbers](modulus-unit-polar-decomposition-of-complex-numbers.html), for the complex member of the family.
- [Modulus–Unit Polar Decomposition of Split-Complex Numbers](modulus-unit-polar-decomposition-of-split-complex-numbers.html), for the hyperbolic companion.
- [Rational-Chart Polar Decomposition of Reduced Biquaternions](rational-chart-polar-decomposition-of-reduced-biquaternions.html), for the rational coordinate on the torus.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the Lie-algebra coordinate on the torus.

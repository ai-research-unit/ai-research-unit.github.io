
# __The Quaternion and Antiquaternion Subspaces__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ carries **two** four-dimensional decompositions, not one. The first is the split into the material and informational sectors, $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$, fixed respectively by the anti-Hermitian and the Hermitian conjugation. The second is the split into the **quaternion** and **antiquaternion** subspaces,

$$
\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}},
$$

fixed and anti-fixed by complex conjugation. The articles on $\mathbb{M}_-$ and on $\mathbb{M}_+$ develop the first; this article develops the second, and above all the way the two interact.

The two splits are equally natural, and neither is a refinement of the other: both are four-plus-four, and they **cross**. That crossing is the source of most of the structure collected here — the pattern of the primes, the intersections of the four subspaces, the grading of the algebra, and the fact that although $\mathbb{B}$ is not a division algebra, each half of this second split is definite and free of zero divisors.

A word on the word *real*, which the series uses in two senses. $\mathbb{M}_-$ is called the framework's **real** sector because it is the fixed space of the real structure $\flat$. The subspace $\mathbb{H}_{\mathbb{B}}$ is real in the older and more elementary sense: its coefficients are real numbers. The two usages are both unavoidable and they do not coincide — $\mathbb{M}_-$ and $\mathbb{H}_{\mathbb{B}}$ are different spaces, meeting in three dimensions. Where the ambiguity could bite, this article writes *real-coefficient* for the second sense.

## The Two Splits

Complex conjugation $\tilde{Q}^*$ ($i \mapsto -i$, $e_k$ fixed) and quaternion conjugation $\bar{\tilde{Q}}$ ($e_k \mapsto -e_k$, $i$ fixed) are two commuting involutions, and their product is the Hermitian conjugation,

$$
\tilde{Q}^\dagger = \bar{\tilde{Q}}^{\,*} = \overline{\tilde{Q}^*}, \qquad \tilde{Q}^\flat = -\tilde{Q}^\dagger .
$$

Because they commute, their fixed and anti-fixed spaces fit together as follows.

| involution | space it fixes | condition | name | real dim |
|---|---|---|---|---|
| complex conjugation ${}^*$ | $\mathbb{H}_{\mathbb{B}}$ | ${}^*(\tilde{Q}) = \tilde{Q}$ | the quaternion subspace | 4 |
| $-{}^{*}$ | $i\mathbb{H}_{\mathbb{B}}$ | ${}^*(\tilde{Q}) = -\tilde{Q}$ | the antiquaternion subspace | 4 |
| Hermitian conjugation $\dagger$ | $\mathbb{M}_+$ | $\dagger(\tilde{Q}) = \tilde{Q}$ | the informational sector | 4 |
| anti-Hermitian conjugation $\flat = -\dagger$ | $\mathbb{M}_-$ | $\dagger(\tilde{Q}) = -\tilde{Q}$ | the material sector | 4 |
| quaternion conjugation $\bar{\cdot}$ | $\mathbb{C}_{\mathbb{B}}$ | $\bar{\cdot}(\tilde{Q}) = \tilde{Q}$ | the center | 2 |

So three of the fixed spaces are four-dimensional — $\mathbb{M}_-$, $\mathbb{M}_+$ and $\mathbb{H}_{\mathbb{B}}$ — and the fourth, the center, is two-dimensional; the antiquaternion subspace is not a fixed space but the *anti*-fixed space of complex conjugation, equivalently the fixed space of $-{}^{*}$. Written out with all four coefficients free,

$$
\mathbb{H}_{\mathbb{B}} = \{q_\mu e_\mu\}, \qquad i\mathbb{H}_{\mathbb{B}} = \{iq'_\mu e_\mu\}, \qquad q_\mu, q'_\mu \in \mathbb{R}.
$$

$\mathbb{H}_{\mathbb{B}}$ is the **real half** and $i\mathbb{H}_{\mathbb{B}}$ the **imaginary half**. The first is a subalgebra — a copy of $\mathbb{H}$ inside $\mathbb{B}$, hence a division algebra. The second is *not* a subalgebra: for $a, b \in \mathbb{H}_{\mathbb{B}}$ one has $(ia)(ib) = -ab \in \mathbb{H}_{\mathbb{B}}$, so the product of two elements of the imaginary half returns to the real half. It is a module over $\mathbb{H}_{\mathbb{B}}$ rather than an algebra in its own right.

Neither $\mathbb{M}_-$ nor $\mathbb{M}_+$ is a subalgebra either: for example $(ie_1)(ie_2) = -e_3$, a product of two elements of $\mathbb{M}_+$ lying in $\mathbb{M}_-$. Of the subspaces considered here, only $\mathbb{H}_{\mathbb{B}}$ and $\mathbb{C}_{\mathbb{B}}$ are closed under multiplication.

## The Quaternion Subspace $\mathbb{H}_{\mathbb{B}}$

### Definition and Basis

The quaternion subspace is the fixed space of complex conjugation. With all four coefficients real,

$$
\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^* = \tilde{Q}\} = \{q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3\}, \qquad q_0, q_1, q_2, q_3 \in \mathbb{R},
$$

of real dimension four, with basis $e_0, e_1, e_2, e_3$ over $\mathbb{R}$. In the physical coordinates its general element is

$$
\tilde{Q} = (ct')\,e_0 + x\,e_1 + y\,e_2 + z\,e_3 \in \mathbb{H}_{\mathbb{B}},
$$

so it carries the **informational time** $ct'$ and the **material space** $x, y, z$, and not the other four coordinates. Under the matrix representation it is the set of quaternion matrices,

$$
\Phi(\mathbb{H}_{\mathbb{B}}) = \left\{\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix} : z, w \in \mathbb{C}\right\}, \qquad z = q_0 - iq_3, \quad w = -iq_1 - q_2 .
$$

### Properties

- **A subalgebra.** A product of two elements with real coefficients again has real coefficients, so $\mathbb{H}_{\mathbb{B}}$ is closed under multiplication; it is a copy of the real quaternions, $\mathbb{H}_{\mathbb{B}} \cong \mathbb{H}$, and it is a division algebra.
- **The home of the rotation rotors.** A rotor is a unit quaternion with real coefficients, so it lies here; in the matrix picture unit determinant gives $\mathrm{SU}(2)$. Spatial rotations are carried by this subspace.
- **Positive definite norm form.** $N(\tilde{Q}) = q_0^2 + q_1^2 + q_2^2 + q_3^2$, which vanishes only at $\tilde{Q} = 0$.
- **No zero divisors.** Since $N(\tilde{Q}) = 0$ has no nonzero solution on this subspace.
- **Even part of the grading**, and preserved as a set by all four involutions, with complex conjugation fixing it pointwise.
- **Not a sector.** It takes its temporal block from one sector and its spatial block from the other: $\mathbb{H}_{\mathbb{B}} = T_{\mathrm{i}} \oplus X_{\mathrm{m}}$, with $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = T_{\mathrm{i}}$ and $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = X_{\mathrm{m}}$.

## The Antiquaternion Subspace $i\mathbb{H}_{\mathbb{B}}$

### Definition and Basis

The antiquaternion subspace is the **anti-fixed** space of complex conjugation — the elements it negates:

$$
i\mathbb{H}_{\mathbb{B}} = \{\tilde{Q} \in \mathbb{B} : \tilde{Q}^* = -\tilde{Q}\} = \{iq'_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3\}, \qquad q'_\mu \in \mathbb{R},
$$

also of real dimension four, with basis $ie_0, ie_1, ie_2, ie_3$ over $\mathbb{R}$. It is exactly $i$ times the quaternion subspace, $i\mathbb{H}_{\mathbb{B}} = i\,\mathbb{H}_{\mathbb{B}}$, and in the physical coordinates its general element is

$$
\tilde{Q} = ic\,t\,e_0 + ix'\,e_1 + iy'\,e_2 + iz'\,e_3 \in i\mathbb{H}_{\mathbb{B}},
$$

carrying the **material time** $ict$ and the **informational space** $ix', iy', iz'$ — precisely the four coordinates that $\mathbb{H}_{\mathbb{B}}$ does not carry. In the matrix picture it is $i$ times the quaternion matrices,

$$
\Phi(i\mathbb{H}_{\mathbb{B}}) = i\,\Phi(\mathbb{H}_{\mathbb{B}}) = \left\{\begin{pmatrix} iz & iw \\ -i\bar{w} & i\bar{z}\end{pmatrix}\right\}.
$$

### Properties

- **Not a subalgebra.** For $a, b$ with real coefficients, $(ia)(ib) = -ab$ lies in $\mathbb{H}_{\mathbb{B}}$: the product of two elements of the imaginary half returns to the real half. It is a module over $\mathbb{H}_{\mathbb{B}}$ rather than an algebra in its own right.
- **Odd part of the grading**, which is the structural reason for the failure above.
- **Negative definite norm form.** $N(\tilde{Q}) = -(q'^2_0 + q'^2_1 + q'^2_2 + q'^2_3)$, which vanishes only at $\tilde{Q} = 0$.
- **No zero divisors**, for the same reason.
- **Multiplication by $i$** carries it onto the quaternion subspace and back, $i(i\mathbb{H}_{\mathbb{B}}) = \mathbb{H}_{\mathbb{B}}$; it is preserved as a set by all four involutions, with complex conjugation negating it pointwise.
- **Not a sector**, and it crosses the other way: $i\mathbb{H}_{\mathbb{B}} = T_{\mathrm{m}} \oplus X_{\mathrm{i}}$, with $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = T_{\mathrm{m}}$ and $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = X_{\mathrm{i}}$.

### The Mirror Between the Two Halves

The two halves are mirror images, and their properties are best read in parallel:

| | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ |
|---|---|---|
| under complex conjugation ${}^{*}$ | fixed pointwise | negated pointwise |
| real dimension | $4$ | $4$ |
| basis | $e_0, e_1, e_2, e_3$ | $ie_0, ie_1, ie_2, ie_3$ |
| coordinate content | $ct'$, $x, y, z$ | $ict$, $ix', iy', iz'$ |
| blocks | $T_{\mathrm{i}} \oplus X_{\mathrm{m}}$ | $T_{\mathrm{m}} \oplus X_{\mathrm{i}}$ |
| closed under multiplication | yes — subalgebra, $\cong \mathbb{H}$ | no — a module |
| grading | even | odd |
| norm form | $+\sum_\mu q_\mu^2$, positive definite | $-\sum_\mu q'^2_\mu$, negative definite |
| matrix image | the quaternion matrices | $i$ times the quaternion matrices |
| under multiplication by $i$ | maps to $i\mathbb{H}_{\mathbb{B}}$ | maps to $\mathbb{H}_{\mathbb{B}}$ |

Each half is the image of the other under multiplication by $i$, and together they are the whole algebra. They are not interchangeable, however, because only the real half is closed under multiplication.

## The Four Coordinate Blocks

The eight real parameters of a general element organize into **four blocks**, distinguished by whether the coordinate is material or informational and whether it is temporal or spatial:

$$
T_{\mathrm{m}} = \mathbb{R}(ie_0), \qquad T_{\mathrm{i}} = \mathbb{R}e_0, \qquad X_{\mathrm{m}} = \mathbb{R}(e_1, e_2, e_3), \qquad X_{\mathrm{i}} = \mathbb{R}(ie_1, ie_2, ie_3).
$$

| block | basis | coordinate | parameter | real dimension |
|---|---|---|---|---|
| $T_{\mathrm{m}}$ — material time | $ie_0$ | $ict$ | $q'_0 = ct$ | 1 |
| $T_{\mathrm{i}}$ — informational time | $e_0$ | $ct'$ | $q_0 = ct'$ | 1 |
| $X_{\mathrm{m}}$ — material space | $e_1, e_2, e_3$ | $x, y, z$ | $q_1, q_2, q_3 = x, y, z$ | 3 |
| $X_{\mathrm{i}}$ — informational space | $ie_1, ie_2, ie_3$ | $ix', iy', iz'$ | $q'_1, q'_2, q'_3 = x', y', z'$ | 3 |

The dimensions account for the algebra: $1 + 1 + 3 + 3 = 8$. The blocks are independent coordinate directions, so every element of $\mathbb{B}$ is a unique sum of one element from each.

Two features of this table are worth stating explicitly, because both recur below. First, the **imaginary unit distinguishes the blocks from their partners**: the temporal coordinate of the material sector carries the $i$, the spatial coordinates of the informational sector carry it, and the remaining four — the informational time and the three material spatial coordinates — do not. Second, the **primed parameters are exactly the elements of the imaginary half** $i\mathbb{H}_{\mathbb{B}}$: $q'_0$ spans $T_{\mathrm{m}}$ and the three $q'_k$ span $X_{\mathrm{i}}$, and together they are precisely the coefficients that enter with the factor $i$. This is the origin of the three-and-one pattern of the primes, and it is discussed further in the conventions article.

## The Four Subspaces in Coordinates

Each of the four four-dimensional subspaces is the sum of **one temporal block and one spatial block**. That is the whole of the structure, and it is easiest to see as a table:

| subspace | temporal term | spatial term | coordinate writing | parameters |
|---|---|---|---|---|
| $\mathbb{M}_-$ | $ict\,e_0$ (material time) | $x e_1 + y e_2 + z e_3$ (material space) | $ict\,e_0 + \mathbf{x}$ | $q'_0, q_k$ |
| $\mathbb{M}_+$ | $ct'\,e_0$ (informational time) | $i(x' e_1 + y' e_2 + z' e_3)$ (informational space) | $(ct')\,e_0 + i\mathbf{x}'$ | $q_0, q'_k$ |
| $\mathbb{H}_{\mathbb{B}}$ | $ct'\,e_0$ (informational time) | $x e_1 + y e_2 + z e_3$ (material space) | $(ct')\,e_0 + \mathbf{x}$ | $q_0, q_k$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ict\,e_0$ (material time) | $i(x' e_1 + y' e_2 + z' e_3)$ (informational space) | $ict\,e_0 + i\mathbf{x}'$ | $q'_0, q'_k$ |

In the block notation this is a one-line statement:

$$
\mathbb{M}_- = T_{\mathrm{m}} \oplus X_{\mathrm{m}}, \qquad
\mathbb{M}_+ = T_{\mathrm{i}} \oplus X_{\mathrm{i}}, \qquad
\mathbb{H}_{\mathbb{B}} = T_{\mathrm{i}} \oplus X_{\mathrm{m}}, \qquad
i\mathbb{H}_{\mathbb{B}} = T_{\mathrm{m}} \oplus X_{\mathrm{i}} .
$$

($\mathbb{C}_{\mathbb{B}}$ is not of this form: it combines the two **temporal** blocks, $\mathbb{C}_{\mathbb{B}} = T_{\mathrm{m}} \oplus T_{\mathrm{i}}$, and is therefore two-dimensional rather than four.)

**The four subspaces are the four ways to choose one time and one space.** The sectors pair a time with the space of the **same** sector — material with material, informational with informational. The quaternion and antiquaternion subspaces pair a time with the space of the **other**:

- $\mathbb{H}_{\mathbb{B}}$ is informational **time** together with material **space**;
- $i\mathbb{H}_{\mathbb{B}}$ is material **time** together with informational **space**.

That single observation is the crossing, and most of what follows is a consequence of it.

Written out in full, all four subspaces in both the parameter form and the physical coordinates:

$$
\begin{aligned}
\mathbb{M}_- &: \quad iq'_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = ic\,t\,e_0 + x\,e_1 + y\,e_2 + z\,e_3, \\
\mathbb{M}_+ &: \quad q_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = (ct')\,e_0 + (ix')\,e_1 + (iy')\,e_2 + (iz')\,e_3, \\
\mathbb{H}_{\mathbb{B}} &: \quad q_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 = (ct')\,e_0 + x\,e_1 + y\,e_2 + z\,e_3, \\
i\mathbb{H}_{\mathbb{B}} &: \quad iq'_0e_0 + iq'_1e_1 + iq'_2e_2 + iq'_3e_3 = ic\,t\,e_0 + ix'\,e_1 + iy'\,e_2 + iz'\,e_3 .
\end{aligned}
$$

The dictionary between the two writings is the one of the conventions article: $q'_0 = ct$, $q_k = x_k$ on the material side, and $q_0 = ct'$, $q'_k = x'_k$ on the informational side.

A reader who has followed the articles on the two sectors will recognize the four terms here — $ict\,e_0$, $x e_k$, $ct'\,e_0$, $i x' e_k$ — as exactly the four pieces those articles assemble into $\mathbb{M}_-$ and $\mathbb{M}_+$. The present article assembles the same four pieces the other way.

## The Involutions as Sign Patterns

Because every involution acts by $\pm 1$ on each block, each one is a sign pattern on the four blocks, and its fixed space is the sum of the blocks it leaves alone:

| block | ${}^{*}$ | $\bar{\cdot}$ | $\dagger$ | $\flat$ |
|---|---|---|---|---|
| $T_{\mathrm{m}}$ (material time) | $-$ | $+$ | $-$ | $+$ |
| $T_{\mathrm{i}}$ (informational time) | $+$ | $+$ | $+$ | $-$ |
| $X_{\mathrm{m}}$ (material space) | $+$ | $-$ | $-$ | $+$ |
| $X_{\mathrm{i}}$ (informational space) | $-$ | $-$ | $+$ | $-$ |

Each row is a block, and each of the four deserves its own account, because these sign patterns are what the rest of the article is built on.

**$T_{\mathrm{m}} = \mathbb{R}(ie_0)$ — material time, dimension $1$, coordinate $ict$, parameter $q'_0 = ct$.** Its row in the table is $(-,+,-,+)$. The single generator $ie_0$ is *imaginary*, which makes ${}^{*}$ negate it, and it is a *scalar*, which makes $\bar{\cdot}$ fix it; the remaining two columns then follow, since $\dagger = \bar{\cdot}\circ{}^{*} = {}^{*}\circ\bar{\cdot}$ inherits the minus from the complex conjugation and picks up none from the quaternion one, while $\flat = -\dagger$ undoes it again. The general element of the block is the single term

$$
\tilde{Q}_{T_{\mathrm{m}}} = iq'_0\,e_0 = ict\,e_0, \qquad q'_0 = ct \in \mathbb{R},
$$

a real parameter carrying the $i$ — exactly the primed slot of the coordinate dictionary. On this element the four involutions read

$$
ict \;\xrightarrow{\ *\ }\; -ict, \qquad
ict \;\xrightarrow{\ \bar{\cdot}\ }\; +ict, \qquad
ict \;\xrightarrow{\ \dagger\ }\; -ict, \qquad
ict \;\xrightarrow{\ \flat\ }\; +ict,
$$

so complex conjugation reverses the time coordinate while quaternion conjugation leaves it alone. That is the behaviour required of a scalar: $ie_0$ has no vector part for $\bar{\cdot}$ to reverse, so the reversal falls to ${}^{*}$, which is why this is the one block on which ${}^{*}$ negates and $\bar{\cdot}$ acts trivially — the character $(-,+)$. The line is **central**, $ie_0$ being a multiple of the unit, so its elements commute with every element of $\mathbb{B}$; it is one of the two lines common to three of the subspaces, $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0)$. In the norm form it is the single **negative** direction of the material sector, $N(ie_0) = -1$, against the $+3$ of that sector's space, which is precisely what makes the material sector Lorentzian rather than Euclidean. Under $\Phi$ it is the line $\Phi(ict\,e_0) = ict\,I_2$ of imaginary multiples of the identity, the fibre of the material global phase.

**$T_{\mathrm{i}} = \mathbb{R}(e_0)$ — informational time, dimension $1$, coordinate $ct'$, parameter $q_0 = ct'$.** Its row is $(+,+,+,-)$ — the all-plus row, and the only one. The generator $e_0$ is the algebra's unit: it is *real*, so ${}^{*}$ fixes it; it is a *scalar*, so $\bar{\cdot}$ fixes it; being both at once it is Hermitian, so $\dagger = \bar{\cdot}\circ{}^{*}$ fixes it too. Only $\flat$, which differs from $\dagger$ by the overall sign, acts on it as a negation. This is therefore the unique block on which the three involutions $\{{}^{*}, \bar{\cdot}, \dagger\}$ act as the identity — the trivial character $(+,+)$ — and the line $\mathbb{R}e_0$ is their common fixed space, appearing as the triple intersection $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_0$. Its general element is

$$
\tilde{Q}_{T_{\mathrm{i}}} = q_0\,e_0 = ct'\,e_0, \qquad q_0 = ct' \in \mathbb{R},
$$

a real *unprimed* parameter, the informational time coordinate of the dictionary, and on it ${}^{*}$, $\bar{\cdot}$ and $\dagger$ act as the identity while $\flat$ sends $ct' \mapsto -ct'$. Because $e_0$ is the identity, the line is central and its elements commute with everything. In the norm form it is the single **positive** direction of the informational sector, $N(e_0) = +1$, against the $-3$ of that sector's space, so the informational sector is the mirror of the material one. Under $\Phi$ it is the line $\Phi(ct'\,e_0) = ct'\,I_2$ of real multiples of the identity. This is the block of the **vacuum**: a real multiple of the unit is fixed by every conjugation the algebra has apart from the anti-Hermitian one, which is exactly the sense in which the vacuum is conjugation-invariant, and the reason the articles on the vacuum and on the idempotents single out this line.

**$X_{\mathrm{m}} = \mathbb{R}(e_1,e_2,e_3)$ — material space, dimension $3$, coordinates $x, y, z$, parameters $q_1, q_2, q_3$.** Its row is $(+,-,-,+)$. Each generator $e_k$ is *real*, so ${}^{*}$ fixes it, and each is a *pure quaternion*, so $\bar{\cdot}$ reverses it; $\dagger$ reverses it as well and $\flat$ restores it. The general element is

$$
\tilde{Q}_{X_{\mathrm{m}}} = q_k\,e_k = x\,e_1 + y\,e_2 + z\,e_3 = \mathbf{x},
$$

the ordinary three-dimensional vector part of the algebra, with real unprimed parameters $q_k = x_k$. On this block the four involutions read

$$
\mathbf{x} \;\xrightarrow{\ *\ }\; \mathbf{x}, \qquad
\mathbf{x} \;\xrightarrow{\ \bar{\cdot}\ }\; -\mathbf{x}, \qquad
\mathbf{x} \;\xrightarrow{\ \dagger\ }\; -\mathbf{x}, \qquad
\mathbf{x} \;\xrightarrow{\ \flat\ }\; \mathbf{x},
$$

so quaternion conjugation is the reversal $\mathbf{x} \mapsto -\mathbf{x}$ while complex conjugation does nothing at all. This is why it is $\bar{\cdot}$ and not ${}^{*}$ that isolates the **time-like** directions: $\bar{\cdot}$ is the involution that separates the scalar block from the vector block, and the only one whose action on space is a half-turn. The block is closed under the commutator, $[e_i,e_j] = 2\epsilon_{ijk}e_k$, so it carries the Lie algebra $\mathfrak{su}(2) \cong \mathfrak{so}(3)$ of the rotations that a rotor generates — although it is not closed under the product, since $e_k^2 = -e_0$ leaves the block for $T_{\mathrm{i}}$. It is the **space** of the material sector, $\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}} = X_{\mathrm{m}}$, and in the norm form it contributes $+3$, positive definite, the Euclidean half of that sector. Under $\Phi$ it is the space of traceless anti-Hermitian matrices, $\Phi(X_{\mathrm{m}}) = \{M : M^\dagger = -M,\ \operatorname{Tr}M = 0\}$.

**$X_{\mathrm{i}} = \mathbb{R}(ie_1,ie_2,ie_3)$ — informational space, dimension $3$, coordinates $ix', iy', iz'$, parameters $q'_1, q'_2, q'_3$.** Its row is $(-,-,+,-)$. Each generator $ie_k$ is *imaginary*, so ${}^{*}$ negates it, and each is a *pure quaternion*, so $\bar{\cdot}$ negates it as well; the two minus signs cancel in the composite $\dagger = \bar{\cdot}\circ{}^{*}$, which therefore fixes the block, while $\flat = -\dagger$ negates it. This is the one block carrying the character $(-,-)$ — the only block on which two involutions negate — and that cancellation is exactly why its elements are Hermitian without being real. The general element is

$$
\tilde{Q}_{X_{\mathrm{i}}} = iq'_k\,e_k = i(x'e_1 + y'e_2 + z'e_3) = i\mathbf{x}', \qquad q'_k = x'_k \in \mathbb{R},
$$

literally $i$ times the vector part, with primed real parameters. Indeed $X_{\mathrm{i}} = i\,X_{\mathrm{m}}$ as sets: multiplication by $i$ exchanges the two spatial blocks, just as it exchanges the two temporal ones, $T_{\mathrm{m}} \leftrightarrow T_{\mathrm{i}}$. On this block the four involutions read $i\mathbf{x}' \mapsto -i\mathbf{x}'$ for ${}^{*}$ and for $\bar{\cdot}$, and $\mapsto +i\mathbf{x}'$ for $\dagger$ and for $\flat$. In the norm form the block contributes $-3$, negative definite, the exact counterpart of the $+3$ of material space. Under $\Phi$ it goes to the traceless **Hermitian** matrices — the images $\Phi(ie_k)$ of the Hermitian units — so this is the block of the observables of the informational sector: the spin directions, the traceless part of a density matrix, the Bloch vector. Together with $T_{\mathrm{i}}$ it makes up the Hermitian subspace, $\mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}} = X_{\mathrm{i}}$.

Reading the $+$ signs column by column gives the table of subspaces back, and each column is worth stating in full.

**${}^{*}$ — complex conjugation, the half split.** It conjugates the central imaginary unit and leaves the quaternion units alone, so on a block it acts by $+1$ where the coordinate is real and by $-1$ where the coordinate carries an explicit $i$. Its column is $(-,+,-,-)$: it negates precisely $T_{\mathrm{m}}$ and $X_{\mathrm{i}}$. Its fixed space is therefore $T_{\mathrm{i}} \oplus X_{\mathrm{m}} = \mathbb{H}_{\mathbb{B}}$, the real quaternions, and its anti-fixed space is the complementary pair $T_{\mathrm{m}} \oplus X_{\mathrm{i}} = i\mathbb{H}_{\mathbb{B}}$; the two together are the half split $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$. This is the involution whose fixed space is a division algebra, and the only one of the four whose two eigenspaces are exchanged by multiplication by $i$.

**$\bar{\cdot}$ — quaternion conjugation, the one that separates time from space.** It fixes the scalar unit and negates the three vector units, so it acts by $+1$ on the two temporal blocks and by $-1$ on the two spatial ones; its column is $(+,+,-,-)$. Its fixed space is therefore $T_{\mathrm{m}} \oplus T_{\mathrm{i}} = \mathbb{C}_{\mathbb{B}}$, the center — the only case among the four where the fixed space is not one of the four-dimensional subspaces — and it is the only involution that treats time and space differently at all. That is why it, rather than ${}^{*}$ or $\dagger$, is the one that isolates the time-like directions, and why it is the involution the classical quaternion conjugate is built from.

**$\dagger = \bar{\cdot}\circ{}^{*}$ — Hermitian conjugation, the sector split.** It negates both **material** blocks and fixes both informational ones, its column being $(-,+,-,+)$; its fixed space is $T_{\mathrm{i}} \oplus X_{\mathrm{i}} = \mathbb{M}_+$, the Hermitian elements. Composing the two previous involutions, it inherits the minus of ${}^{*}$ on the scalar and cancels the two minus signs on the imaginary vectors, which is the arithmetic behind the three-and-one structure of the sector. This is the involution the quantum formalism uses: its fixed space is the observables.

**$\flat = -\dagger$ — anti-Hermitian conjugation, the algebra's real structure.** It is $\dagger$ with the overall sign reversed, so its column $(+,-,+,-)$ is the exact negation of the previous one: it fixes $T_{\mathrm{m}} \oplus X_{\mathrm{m}} = \mathbb{M}_-$ and negates the complementary blocks. Its fixed space is the material sector, the Lorentzian one, and it is the involution whose fixed space is a subspace but not a subalgebra. Note that $\dagger$ and $\flat$ together account for both sectors and for both signs of the same involution — which is the sense in which the two sectors are not two independent structures but the two signs of one.

The four involutions $\{1, {}^{*}, \bar{\cdot}, \dagger\}$ commute and form a Klein four-group, and the signs of ${}^{*}$ and $\bar{\cdot}$ on the four blocks are exactly its four characters — the remaining two columns then follow from $\dagger = \bar{\cdot}\circ{}^{*}$ and $\flat = -\dagger$. The block decomposition is therefore the decomposition of $\mathbb{B}$ into the four characters of that group action, which is why it is canonical: four blocks, four characters, each occurring once. Note how the pairing works in that light: $\dagger$ and $\flat$ differ by the overall sign and between them separate the two sectors, while ${}^{*}$ separates the two halves. Quaternion conjugation is the one that isolates the time-like directions.

## The Intersections

Two subspaces $A, B \subseteq \mathbb{B}$ meet in their **intersection**

$$
A \cap B = \{\, \tilde{Q} \in \mathbb{B} \;:\; \tilde{Q} \in A \ \text{and} \ \tilde{Q} \in B \,\},
$$

the set of elements belonging to both. It is again a subspace of $\mathbb{B}$: it contains $0$, and it is contained in each of $A$ and $B$. Its dimension is the quantity worth tabulating, and the block structure fixes it with no case needing separate work. Every element has a unique expansion into the four blocks, $\tilde{Q} = \tilde{Q}_{T_{\mathrm{m}}} + \tilde{Q}_{T_{\mathrm{i}}} + \tilde{Q}_{X_{\mathrm{m}}} + \tilde{Q}_{X_{\mathrm{i}}}$ with each term lying in its own block, and each of the four subspaces is a sum of blocks. A sum of blocks contains $\tilde{Q}$ exactly when it contains each of the block components separately, so

$$
\tilde{Q} \in A \cap B \quad\Longleftrightarrow\quad \tilde{Q}_{\text{block}} = 0 \ \text{ for every block outside } A \ \text{and every block outside } B .
$$

**Hence the intersection of two subspaces is the sum of the blocks they share.** A subspace has two blocks, so two of them share none, one, or both; sharing both means they are the same subspace, whose intersection is itself. For two **distinct** subspaces the dimensions are therefore $0$ (no shared block), $1$ (one shared temporal block) and $3$ (one shared spatial block).

| $\cap$ | $\mathbb{M}_-$ | $\mathbb{M}_+$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ |
|---|---|---|---|---|
| $\mathbb{M}_-$ | $\mathbb{M}_-$ | $0$ | $X_{\mathrm{m}}$ | $T_{\mathrm{m}}$ |
| $\mathbb{M}_+$ | $0$ | $\mathbb{M}_+$ | $T_{\mathrm{i}}$ | $X_{\mathrm{i}}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $X_{\mathrm{m}}$ | $T_{\mathrm{i}}$ | $\mathbb{H}_{\mathbb{B}}$ | $0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $T_{\mathrm{m}}$ | $X_{\mathrm{i}}$ | $0$ | $i\mathbb{H}_{\mathbb{B}}$ |

**In coordinates.**

$$
\begin{aligned}
\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}} &= \mathbb{R}(e_1,e_2,e_3) = X_{\mathrm{m}}, \\
\mathbb{M}_- \cap i\mathbb{H}_{\mathbb{B}} &= \mathbb{R}(ie_0) = T_{\mathrm{m}}, \\
\mathbb{M}_+ \cap \mathbb{H}_{\mathbb{B}} &= \mathbb{R}e_0 = T_{\mathrm{i}}, \\
\mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}} &= \mathbb{R}(ie_1,ie_2,ie_3) = X_{\mathrm{i}} .
\end{aligned}
$$

### Why the table has this shape

Each subspace is one temporal block plus one spatial block, so the four can be arranged by which pair each one takes. Rows are the temporal choice, columns the spatial one, and each cell carries the subspace together with the two blocks that meet there:

| | material space $X_{\mathrm{m}}$ | informational space $X_{\mathrm{i}}$ |
|---|---|---|
| **material time** $T_{\mathrm{m}}$ | $\mathbb{M}_-$<br>$(T_{\mathrm{m}},\,X_{\mathrm{m}})$ | $i\mathbb{H}_{\mathbb{B}}$<br>$(T_{\mathrm{m}},\,X_{\mathrm{i}})$ |
| **informational time** $T_{\mathrm{i}}$ | $\mathbb{H}_{\mathbb{B}}$<br>$(T_{\mathrm{i}},\,X_{\mathrm{m}})$ | $\mathbb{M}_+$<br>$(T_{\mathrm{i}},\,X_{\mathrm{i}})$ |

Two subspaces in the same row share their time, two in the same column share their space, and no two of the four are equal. The two splits appear as the two diagonals of this grid — the sectors pair a time with the space of the same sector, the halves pair a time with the space of the other. The whole intersection table is therefore the grid: **for two distinct subspaces, same row gives dimension $1$, same column gives dimension $3$, and differing in both gives $0$.** The vanishing pairs are exactly those differing in both entries, which is what the two splits are, and the four nonzero off-diagonal entries have the dimension of the shared block, $3$ for a shared space and $1$ for a shared time. The dimensions $\{0,1,3\}$ are the three-and-one pattern of the blocks, read as an intersection.

### $\mathbb{M}_- \cap \mathbb{M}_+ = 0$

*Dimension $0$ — the two sectors meet only at the origin.*

**The eigenvalue argument.** The two sectors are the $+1$ and $-1$ eigenspaces of $\dagger$, so an element lying in both would satisfy $\tilde{Q} = \tilde{Q}^\dagger$ and $\tilde{Q} = -\tilde{Q}^\dagger$ simultaneously, giving $\tilde{Q} = -\tilde{Q}$ and hence $\tilde{Q} = 0$: the two sectors meet only at the origin. **In blocks.** The same conclusion is immediate, because $\mathbb{M}_- = T_{\mathrm{m}} \oplus X_{\mathrm{m}}$ and $\mathbb{M}_+ = T_{\mathrm{i}} \oplus X_{\mathrm{i}}$ have **no block in common**, and an element of an intersection has to vanish on every block outside both subspaces. **Directness.** This vanishing is what makes the sector split *direct*, $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$, so the decomposition of an arbitrary element into its anti-Hermitian and Hermitian parts,

$$
\tilde{Q} = \tfrac12(\tilde{Q} - \tilde{Q}^\dagger) + \tfrac12(\tilde{Q} + \tilde{Q}^\dagger),
$$

is *unique* rather than merely a spanning, the two terms lying in $\mathbb{M}_-$ and $\mathbb{M}_+$ respectively; equivalently, $\tfrac12(1 \mp \dagger)$ are complementary projections onto the two sectors, with $\tfrac12(1 - \dagger) + \tfrac12(1 + \dagger) = 1$ and the two products zero. **Physical content.** No element of the algebra is at once an observable and a four-vector, and the two sectors are disjoint apart from the origin.

### $\mathbb{H}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} = 0$

*Dimension $0$ — the two halves meet only at the origin.*

**The other generator.** The argument repeats with ${}^{*}$ in place of $\dagger$: the halves are the $+1$ and $-1$ eigenspaces of complex conjugation, so an element of both satisfies $\tilde{Q} = \tilde{Q}^{*} = -\tilde{Q}^{*}$ and is again forced to vanish. **In blocks.** $\mathbb{H}_{\mathbb{B}} = T_{\mathrm{i}} \oplus X_{\mathrm{m}}$ and $i\mathbb{H}_{\mathbb{B}} = T_{\mathrm{m}} \oplus X_{\mathrm{i}}$ share no block either. **Directness.** The vanishing is the directness of the real-and-imaginary split $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$, and the unique decomposition it licenses is the split into real and imaginary parts with respect to ${}^{*}$,

$$
\tilde{Q} = \tfrac12(\tilde{Q} + \tilde{Q}^{*}) + \tfrac12(\tilde{Q} - \tilde{Q}^{*}),
$$

the first term in $\mathbb{H}_{\mathbb{B}}$ and the second in $i\mathbb{H}_{\mathbb{B}}$. **Why exactly two zeros.** The two vanishing entries of the intersection table are exactly the two splits, one for each generator of the commuting pair $(\dagger, {}^{*})$; the two remaining involutions, being composites, produce the nonzero entries below.

### $\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}} = X_{\mathrm{m}}$

*Dimension $3$ — the space that the material sector and the quaternion half hold in common.*

**The constraint.** An element of $\mathbb{M}_-$ is anti-Hermitian, so its scalar coefficient $Q_0$ is purely imaginary and its vector coefficients $Q_k$ are real; an element of $\mathbb{H}_{\mathbb{B}}$ is all-real, so every $Q_\mu$ is real. In the intersection $Q_0$ must be both purely imaginary and real, which forces the scalar to vanish, while the three vector coefficients are real under both conditions and survive untouched. What remains is the real vector part,

$$
\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}} = \{\, x\,e_1 + y\,e_2 + z\,e_3 \;:\; x, y, z \in \mathbb{R} \,\} = \mathbb{R}(e_1,e_2,e_3) = X_{\mathrm{m}},
$$

**The largest intersection.** It is the largest entry in the table and the only three-dimensional one involving $\mathbb{M}_-$. **Pure quaternions.** Its elements are the pure quaternions in the classical sense — the vectors of the algebra — and they are exactly the part closed under the commutator, $[e_i,e_j] = 2\epsilon_{ijk}e_k$, so the intersection carries the rotation algebra $\mathfrak{su}(2)$ even though neither $\mathbb{M}_-$ nor $\mathbb{H}_{\mathbb{B}}$ is itself closed under the product. It is the **space** of the material sector and simultaneously the space of the quaternion half: the three spatial directions are what the sector and the half hold in common, which is why a rotor built from these units rotates space and nothing else. **Norm form and matrix image.** In the norm form the block contributes $+3$, positive definite, and under $\Phi$ it is the traceless anti-Hermitian matrices. **Two further remarks.** The intersection is a proper subspace of both factors, so neither condition implies the other: being anti-Hermitian constrains the scalar to be imaginary, being real constrains the vectors to be real, and the two agree precisely on the vector part. And since $\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}} = X_{\mathrm{m}}$ is the *spatial* block of each, the intersection of a sector with the real half is always the Euclidean part of the pair, never the time.

### $\mathbb{M}_- \cap i\mathbb{H}_{\mathbb{B}} = T_{\mathrm{m}}$

*Dimension $1$ — the $ict$ axis, the time that the material sector holds with the imaginary half.*

**The constraint.** Here an element must be anti-Hermitian, as in $\mathbb{M}_-$, and all-imaginary, as in $i\mathbb{H}_{\mathbb{B}}$. The three vector coefficients are real under the first condition and imaginary under the second, so all three must vanish; the scalar coefficient is imaginary under both and survives alone. The intersection is therefore the single line

$$
\mathbb{M}_- \cap i\mathbb{H}_{\mathbb{B}} = \{\, ict\,e_0 \;:\; ct \in \mathbb{R} \,\} = \mathbb{R}(ie_0) = T_{\mathrm{m}},
$$

the $ict$ axis. **Three features distinguish it.** **First**, it lies in the **center**, since $ie_0$ is a multiple of the unit, so its elements commute with every element of $\mathbb{B}$ and cannot generate a rotation: this is why the temporal direction of the material sector enters the algebra as a phase rather than as a generator, and why the line is one of the two directions common to three subspaces, $\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0)$. **Second**, it is the single **negative** direction in the norm form, $N(ie_0) = -1$, the origin of the Lorentzian signature of the material sector. **Third**, it is the only place where that sector reaches into the imaginary half; intersecting $\mathbb{M}_-$ with $i\mathbb{H}_{\mathbb{B}}$ leaves just this line, exactly as intersecting it with $\mathbb{H}_{\mathbb{B}}$ leaves just its space, so the sector meets the two halves in its time and its space respectively.

### $\mathbb{M}_+ \cap \mathbb{H}_{\mathbb{B}} = T_{\mathrm{i}}$

*Dimension $1$ — the vacuum line, shared by the center, the real quaternions and the informational sector.*

**The constraint.** An element of $\mathbb{M}_+$ is Hermitian, so its scalar coefficient is real and its vector coefficients are purely imaginary; an element of $\mathbb{H}_{\mathbb{B}}$ is all-real. In the intersection the vector coefficients must be imaginary and real at once, hence zero, while the scalar coefficient is real under both conditions and survives. The intersection is the line of real multiples of the identity,

$$
\mathbb{M}_+ \cap \mathbb{H}_{\mathbb{B}} = \{\, ct'\,e_0 \;:\; ct' \in \mathbb{R} \,\} = \mathbb{R}e_0 = T_{\mathrm{i}},
$$

**The vacuum direction.** It is the identity, the global phase, the one element of the algebra fixed by every conjugation except $\flat$. It is the **common fixed line** of the three involutions $\{{}^{*}, \bar{\cdot}, \dagger\}$, which is why it also appears as the triple intersection $\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_0$. Like its counterpart $\mathbb{R}(ie_0)$ it is central, hence commutative and rotationless, and it is the single **positive** direction contributed by the informational sector, $N(e_0) = +1$. **The asymmetry.** The block is the temporal counterpart of the previous entry, and it exhibits the same dimensional asymmetry between the two halves: the informational sector shares its **time** with $\mathbb{H}_{\mathbb{B}}$ in this one-dimensional intersection while sharing its **space** with $i\mathbb{H}_{\mathbb{B}}$ in the three-dimensional one below, whereas the material sector does the reverse.

### $\mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}} = X_{\mathrm{i}}$

*Dimension $3$ — the observables that the informational sector and the imaginary half hold in common.*

**The constraint.** The element is Hermitian, so its scalar coefficient is real, and it is all-imaginary, so that same coefficient is imaginary; the scalar therefore vanishes, while the three purely imaginary vector coefficients satisfy both conditions and survive. The intersection is the block of imaginary vectors,

$$
\mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}} = \{\, i(x'e_1 + y'e_2 + z'e_3) \;:\; x', y', z' \in \mathbb{R} \,\} = \mathbb{R}(ie_1,ie_2,ie_3) = X_{\mathrm{i}} .
$$

**Observables.** Its elements are Hermitian and traceless, so under $\Phi$ they are the traceless Hermitian $2 \times 2$ matrices — the spin directions, the traceless part of a density matrix, the Bloch vector — and this is why the intersection is the **observables** of the informational sector, the counterpart of the space $X_{\mathrm{m}}$ of the material one. It is the second of the two three-dimensional entries and the only one contributed by the imaginary half, and in the norm form it is negative definite, contributing $-3$, the exact mirror of the $+3$ of material space. **Pairing under $i$.** The four nonzero intersections pair up under multiplication by $i$: the central imaginary unit exchanges the two sectors and the two halves at once, carrying the space-space pair to the space-space pair and the time-time pair to the time-time pair,

$$
i\,(\mathbb{M}_- \cap \mathbb{H}_{\mathbb{B}}) = \mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}}, \qquad
i\,(\mathbb{M}_- \cap i\mathbb{H}_{\mathbb{B}}) = \mathbb{M}_+ \cap \mathbb{H}_{\mathbb{B}} .
$$

**Crossing of the splits.** That is the algebraic statement that the time and the space of the material sector become the time and the space of the informational sector under multiplication by the central imaginary unit — the crossing of the two splits, seen on the intersections themselves.

**The pattern.** Every pair of distinct subspaces therefore either meets in one block or does not meet at all, and each meets two of the other three. In this sense the two four-plus-four splits are maximally crossed with respect to one another: no piece of either split is contained in a piece of the other, and every cross pair meets — the largest intersections available given that both decompositions must remain direct.

### Each half is assembled from one piece of each sector

The intersections above split $\mathbb{H}_{\mathbb{B}}$ between the two sectors, and the two pieces are complementary within it:

$$
\mathbb{H}_{\mathbb{B}} = (\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+) \oplus (\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-) = T_{\mathrm{i}} \oplus X_{\mathrm{m}},
$$

$$
i\mathbb{H}_{\mathbb{B}} = (i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_-) \oplus (i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+) = T_{\mathrm{m}} \oplus X_{\mathrm{i}} .
$$

So a half is not "inside" a sector at all: it takes its temporal block from one sector and its spatial block from the other, which is the crossing stated at the level of the sectors. Note also the asymmetry of dimension — a sector shares its **space** with one half (three dimensions) and its **time** with the other (one) — and that the two pieces of $\mathbb{H}_{\mathbb{B}}$ are of different dimension, three and one.

### A common line is shared by triples, not pairs

Reading the block memberships, the center, the real quaternions and the Hermitian subspace all contain $T_{\mathrm{i}}$, so

$$
\mathbb{C}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_0, \qquad
\mathbb{C}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0),
$$

while e.g. $\mathbb{H}_{\mathbb{B}} \cap \mathbb{M}_+ \cap i\mathbb{H}_{\mathbb{B}} = 0$. The two lines $\mathbb{R}e_0$ and $\mathbb{R}(ie_0)$ are the only directions common to three of the subspaces, and they are the two central lines. Each of the four subspaces meets the center in exactly one of them: $\mathbb{M}_+$ and $\mathbb{H}_{\mathbb{B}}$ in $\mathbb{R}e_0$, and $\mathbb{M}_-$ and $i\mathbb{H}_{\mathbb{B}}$ in $\mathbb{R}(ie_0)$. The center is the only one of the subspaces with no spatial part at all — which is why it is two-dimensional rather than four, and why every intersection it has with another subspace is a single temporal line. Its two blocks lie one in each sector, $T_{\mathrm{i}} \subset \mathbb{M}_+$ and $T_{\mathrm{m}} \subset \mathbb{M}_-$; but it is not alone in meeting both sectors, since $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ do as well ($T_{\mathrm{i}}$ lies in $\mathbb{M}_+$ while $X_{\mathrm{m}}$ lies in $\mathbb{M}_-$). The matrix-representation article records the two intersections, $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_+ = \mathbb{R}e_0$ and $\mathbb{C}_{\mathbb{B}} \cap \mathbb{M}_- = \mathbb{R}(ie_0)$.

## Which Pairs Span the Algebra

The intersections say how the subspaces overlap; the sums say how much of $\mathbb{B}$ they cover. There are six pairs, and they fall into three kinds:

| pair | dimension | what is missing |
|---|---|---|
| $\mathbb{M}_- + \mathbb{M}_+$ | $8$ | nothing — this is a split |
| $\mathbb{H}_{\mathbb{B}} + i\mathbb{H}_{\mathbb{B}}$ | $8$ | nothing — this is a split |
| $\mathbb{M}_- + \mathbb{H}_{\mathbb{B}}$ | $5$ | $X_{\mathrm{i}}$, the informational space |
| $\mathbb{M}_+ + i\mathbb{H}_{\mathbb{B}}$ | $5$ | $X_{\mathrm{m}}$, the material space |
| $\mathbb{M}_- + i\mathbb{H}_{\mathbb{B}}$ | $7$ | $T_{\mathrm{i}}$, the informational time |
| $\mathbb{M}_+ + \mathbb{H}_{\mathbb{B}}$ | $7$ | $T_{\mathrm{m}}$, the material time |

Only the two genuine splits reach dimension $8$. The $5$-dimensional sums are the two pairs that share a whole space and differ in time; the $7$-dimensional sums are the two that share a time and differ in space. The arithmetic is the intersection dimension: sharing a three-dimensional block leaves $4 + 4 - 3 = 5$, and sharing a one-dimensional block leaves $4 + 4 - 1 = 7$. The practical content is that an arbitrary element **cannot** in general be written as a material part plus a quaternion part: $\mathbb{M}_- + \mathbb{H}_{\mathbb{B}}$ omits the informational space entirely, so any element with a nonzero $i x' e_k$ component lies outside it. Since $\mathbb{M}_-$ and $\mathbb{H}_{\mathbb{B}}$ are both natural choices of "the real part", it is worth being aware that they are not complementary.

## The Grading

Multiplication respects the two halves in the following sense: a product of two elements of the real half is again in the real half, and a product of an element of the real half with one of the imaginary half is in the imaginary half. In full,

$$
\mathbb{H}_{\mathbb{B}}\cdot\mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}}, \qquad
\mathbb{H}_{\mathbb{B}}\cdot i\mathbb{H}_{\mathbb{B}} \subseteq i\mathbb{H}_{\mathbb{B}}, \qquad
i\mathbb{H}_{\mathbb{B}}\cdot\mathbb{H}_{\mathbb{B}} \subseteq i\mathbb{H}_{\mathbb{B}}, \qquad
i\mathbb{H}_{\mathbb{B}}\cdot i\mathbb{H}_{\mathbb{B}} \subseteq \mathbb{H}_{\mathbb{B}} .
$$

This is precisely the statement that $\mathbb{B}$ is **graded by $\mathbb{Z}/2$** with respect to the split, $\mathbb{H}_{\mathbb{B}}$ being the even part and $i\mathbb{H}_{\mathbb{B}}$ the odd part. The grading is the algebraic reason that $i\mathbb{H}_{\mathbb{B}}$ fails to be a subalgebra while $\mathbb{H}_{\mathbb{B}}$ succeeds: the product of two odd elements lands in the even part, so the odd part is only a module. The same computation in coordinates is $(iq'_1)(iq'_2) = -q'_1q'_2e_3$, which lies in $\mathbb{H}_{\mathbb{B}}$ and not in $i\mathbb{H}_{\mathbb{B}}$.

Two consequences are worth recording. First, $\mathbb{H}_{\mathbb{B}}$ is a subalgebra and therefore a division algebra, while $\mathbb{B}$ is not; the failure of division in $\mathbb{B}$ comes entirely from the odd part being present. Second, the grading and the sector split are independent: multiplying by $i$, which is central, interchanges the two halves, while $\mathbb{M}_-$ and $\mathbb{M}_+$ are exchanged by $i$ as well. The two four-plus-four structures are swapped by the same element, which is another view of why they cannot be made to align.

## The Norm Form on Each Half

The norm form of the algebra is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. Separating the real and imaginary parts of the coefficients, $Q_\mu = q_\mu + iq'_\mu$, gives

$$
N(\tilde{Q}) = \left(\sum_\mu q_\mu^2 - \sum_\mu q'^2_\mu\right) + 2i\sum_\mu q_\mu q'_\mu .
$$

On the halves, where one of the two sums vanishes, the form becomes a form in four variables with a **definite** sign:

$$
N(\tilde{Q}) = \sum_\mu q_\mu^2 > 0 \quad \text{on } \mathbb{H}_{\mathbb{B}}, \qquad
N(\tilde{Q}) = -\sum_\mu q'^2_\mu < 0 \quad \text{on } i\mathbb{H}_{\mathbb{B}} .
$$

Restricted to the real half the norm form is the ordinary sum of squares: **positive definite**, vanishing only at the origin. Restricted to the imaginary half it is **negative definite**, likewise vanishing only at the origin. Consequently:

**Neither half contains a zero divisor.** A zero divisor in the algebra is an element with $N(\tilde{Q}) = 0$; on $\mathbb{H}_{\mathbb{B}}$ the norm is positive definite and on $i\mathbb{H}_{\mathbb{B}}$ negative definite, so the only element of either half with zero norm is the zero element. The two halves are, in this precise sense, the parts of the algebra where no degeneracy occurs — consistent with $\mathbb{H}_{\mathbb{B}}$ being a division algebra.

**All the indefiniteness comes from mixing the two halves.** The Lorentzian signature, the light cone, and the entire zero-divisor structure of $\mathbb{B}$ arise from elements having a nonzero component in *both* halves: only then can the two sums in $N$ cancel. An element of $\mathbb{M}_-$ is a mixed element in this sense — its scalar $iq'_0e_0$ comes from the imaginary half and its vectors $q_ke_k$ from the real half — and it is exactly on the light cone $q'^2_0 = q_1^2 + q_2^2 + q_3^2$, where the two contributions to the norm balance, that it becomes a zero divisor. The quaternion and antiquaternion subspaces, taken individually, are the two halves of the algebra on which that cancellation cannot happen.

**The idempotents and the spinor module lie outside both halves.** The rank-one idempotents $\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac12(e_0 \pm i\hat{\boldsymbol\mu})$ have a scalar part in $T_{\mathrm{i}}$ and a vector part in $X_{\mathrm{i}}$, so they lie in $\mathbb{M}_+$ and cross from one half to the other: neither $\tilde{P}_+$ nor $\tilde{P}_-$ belongs to $\mathbb{H}_{\mathbb{B}}$ or to $i\mathbb{H}_{\mathbb{B}}$. This is required, since they are null elements, $N(\tilde{P}) = 0$, and neither half admits one.

## How the Operations Act on the Two Splits

The two splits respond differently to the algebra's own operations, and the contrast is a useful summary of the structure.

**Multiplication by $i$ exchanges both splits.** Since $i$ is central, $i(a + ib) = -b + ia$: the real and imaginary parts are interchanged, with a sign. Hence

$$
i\,\mathbb{H}_{\mathbb{B}} = i\mathbb{H}_{\mathbb{B}}, \qquad i\,(i\mathbb{H}_{\mathbb{B}}) = \mathbb{H}_{\mathbb{B}}, \qquad
i\,\mathbb{M}_+ = \mathbb{M}_-, \qquad i\,\mathbb{M}_- = \mathbb{M}_+ .
$$

So multiplication by $i$ pairs the two halves and pairs the two sectors. In block terms it exchanges $T_{\mathrm{m}} \leftrightarrow T_{\mathrm{i}}$ and $X_{\mathrm{m}} \leftrightarrow X_{\mathrm{i}}$: the material time becomes the informational time, and the material space becomes the informational space.

**Quaternion conjugation preserves everything.** $\bar{\cdot}$ negates the two spatial blocks and leaves the two temporal blocks alone. It therefore maps every one of the subspaces above to itself, and fixes the center pointwise — which is the statement that $\mathbb{C}_{\mathbb{B}}$ is its fixed space.

**Complex conjugation preserves both halves but reverses their roles.** ${}^{*}$ fixes $\mathbb{H}_{\mathbb{B}}$ pointwise and negates $i\mathbb{H}_{\mathbb{B}}$ pointwise; it maps each sector to itself. So of the two splits, the sector split is the one that is *not* detected by complex conjugation, and the half split is the one that is.

## The Matrix Picture

Under the representation $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ of the matrix-representation article, with $\Phi(e_k) = -i\sigma_k$, the two halves are the quaternion matrices and $i$ times them:

$$
\Phi(\mathbb{H}_{\mathbb{B}}) = \left\{\begin{pmatrix} z & w \\ -\bar{w} & \bar{z}\end{pmatrix} : z, w \in \mathbb{C}\right\} \text{ with } z = q_0 - iq_3,\; w = -iq_1 - q_2,
$$

$$
\Phi(i\mathbb{H}_{\mathbb{B}}) = i\,\Phi(\mathbb{H}_{\mathbb{B}}) = \left\{\begin{pmatrix} iz & iw \\ -i\bar{w} & i\bar{z}\end{pmatrix}\right\}.
$$

The determinants are definite and of opposite sign, which is the matrix form of the previous section:

$$
\det\Phi(q_\mu e_\mu) = q_0^2 + q_1^2 + q_2^2 + q_3^2 > 0, \qquad
\det\Phi(iq'_\mu e_\mu) = -\left(q'^2_0 + q'^2_1 + q'^2_2 + q'^2_3\right) < 0 .
$$

Since $\Phi(i\tilde{Q}) = i\,\Phi(\tilde{Q})$, the second is the first multiplied by $i^2 = -1$ in the determinant. And because the real half has $\det > 0$ except at the origin, its matrices are all invertible — the matrix reason that $\mathbb{H}_{\mathbb{B}} \cong \mathbb{H}$ is a division algebra while $\mathbb{B} \cong M_2(\mathbb{C})$ is not.

The crossing appears in the matrices as the placement of the identity and Pauli terms. On the material sector the matrix is

$$
\Phi(\mathbb{M}_-)\ni i\left(q'_0I_2 - q_k\sigma_k\right),
$$

whose coefficient of $I_2$ is the purely imaginary $iq'_0$ — a coefficient from $i\mathbb{H}_{\mathbb{B}}$ — while its coefficients of $\sigma_k$ are the real $q_k$, from $\mathbb{H}_{\mathbb{B}}$. On the informational sector the matrix is $\Phi(\mathbb{M}_+)\ni q_0I_2 + q'_k\sigma_k$, and the two origins are reversed: the identity term comes from $\mathbb{H}_{\mathbb{B}}$ and the Pauli terms from $i\mathbb{H}_{\mathbb{B}}$. In both cases the identity term and the Pauli terms come from different halves, and the two sectors differ only in which half supplies which. This is the crossing, read off the matrices.

## Summary

The biquaternion algebra admits two independent four-plus-four decompositions: the sector split $\mathbb{B} = \mathbb{M}_- \oplus \mathbb{M}_+$ by Hermitian conjugation, and the half split $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ by complex conjugation. The four involutions have as fixed spaces the three four-dimensional subspaces $\mathbb{M}_-$, $\mathbb{M}_+$ and $\mathbb{H}_{\mathbb{B}}$ together with the two-dimensional center $\mathbb{C}_{\mathbb{B}}$; the antiquaternion subspace is the anti-fixed space of complex conjugation. The two splits cross.

- The eight real parameters fall into four blocks: the material time $T_{\mathrm{m}} = \mathbb{R}(ie_0)$, the informational time $T_{\mathrm{i}} = \mathbb{R}e_0$, the material space $X_{\mathrm{m}} = \mathbb{R}(e_1,e_2,e_3)$, and the informational space $X_{\mathrm{i}} = \mathbb{R}(ie_1,ie_2,ie_3)$. The primed parameters $q'_0, q'_k$ are exactly the coefficients that enter with $i$, that is, they span $i\mathbb{H}_{\mathbb{B}}$ — which is the origin of the three-and-one pattern of the primes.
- Each of the four four-dimensional subspaces is one temporal block plus one spatial block: $\mathbb{M}_- = T_{\mathrm{m}}\oplus X_{\mathrm{m}}$, $\mathbb{M}_+ = T_{\mathrm{i}}\oplus X_{\mathrm{i}}$, $\mathbb{H}_{\mathbb{B}} = T_{\mathrm{i}}\oplus X_{\mathrm{m}}$, $i\mathbb{H}_{\mathbb{B}} = T_{\mathrm{m}}\oplus X_{\mathrm{i}}$. So $\mathbb{H}_{\mathbb{B}}$ is informational time with material space, and $i\mathbb{H}_{\mathbb{B}}$ is material time with informational space. The sectors pair a time with the space of the same sector; the halves pair a time with the space of the other. The center is the exception: two temporal blocks and no spatial one.
- The intersections are the shared blocks, so two **distinct** subspaces have dimension $0$, $1$ or $3$ and never $2$ or $4$. Viewed as a two-by-two grid of temporal against spatial block, subspaces in the same row share their time (dimension $1$), those in the same column share their space (dimension $3$), and those differing in both entries — which are exactly the two splits — meet only at $0$. Every pair of distinct subspaces meets except the two split partners: $\mathbb{M}_- \cap \mathbb{M}_+ = 0$ and $\mathbb{H}_{\mathbb{B}} \cap i\mathbb{H}_{\mathbb{B}} = 0$. The two splits are maximally crossed: no piece of either lies inside a piece of the other.
- The center, the real quaternions and $\mathbb{M}_+$ share the line $\mathbb{R}e_0$; the center, the antiquaternions and $\mathbb{M}_-$ share $\mathbb{R}(ie_0)$. Each subspace meets the center in exactly one of these two lines, and the center is the only subspace with no spatial part — two-dimensional where the others are four.
- Only the two splits span: $\mathbb{M}_- + \mathbb{M}_+ = \mathbb{B} = \mathbb{H}_{\mathbb{B}} + i\mathbb{H}_{\mathbb{B}}$, while the mixed pairs span $5$ or $7$ dimensions. An element of $\mathbb{B}$ cannot in general be written as a material part plus a quaternion part.
- The half split is a $\mathbb{Z}/2$-grading: $\mathbb{H}_{\mathbb{B}}$ is the even part and a subalgebra, $i\mathbb{H}_{\mathbb{B}}$ the odd part and only a module. $\mathbb{H}_{\mathbb{B}} \cong \mathbb{H}$ is a division algebra.
- The norm form is positive definite on $\mathbb{H}_{\mathbb{B}}$ and negative definite on $i\mathbb{H}_{\mathbb{B}}$, so neither half contains a zero divisor. The Lorentzian signature and the whole zero-divisor cone of $\mathbb{B}$ come from mixing the two halves.
- Multiplication by $i$ exchanges the halves and exchanges the sectors; quaternion conjugation preserves all four subspaces; complex conjugation fixes the real half and negates the imaginary half, and preserves both sectors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{B}} = \{q_\mu e_\mu\}$ | The quaternion subspace: the real half, fixed space of complex conjugation, all four coefficients real; a subalgebra, isomorphic to $\mathbb{H}$, and a division algebra |
| $i\mathbb{H}_{\mathbb{B}} = \{iq'_\mu e_\mu\}$ | The antiquaternion subspace: the imaginary half, anti-fixed space of complex conjugation, all four coefficients purely imaginary; a module over $\mathbb{H}_{\mathbb{B}}$, not a subalgebra |
| $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$ | The half split; a $\mathbb{Z}/2$-grading, and independent of the sector split |
| $T_{\mathrm{m}} = \mathbb{R}(ie_0)$ | Material time block; coordinate $ict$, parameter $q'_0 = ct$ |
| $T_{\mathrm{i}} = \mathbb{R}e_0$ | Informational time block; coordinate $ct'$, parameter $q_0 = ct'$ |
| $X_{\mathrm{m}} = \mathbb{R}(e_1,e_2,e_3)$ | Material space block; coordinates $x, y, z$, parameters $q_1, q_2, q_3$ |
| $X_{\mathrm{i}} = \mathbb{R}(ie_1,ie_2,ie_3)$ | Informational space block; coordinates $ix', iy', iz'$, parameters $q'_1, q'_2, q'_3$ |
| $\mathbb{M}_- = T_{\mathrm{m}} \oplus X_{\mathrm{m}}$ | The material sector as one time plus one space, both material |
| $\mathbb{M}_+ = T_{\mathrm{i}} \oplus X_{\mathrm{i}}$ | The informational sector as one time plus one space, both informational |
| $\mathbb{H}_{\mathbb{B}} = T_{\mathrm{i}} \oplus X_{\mathrm{m}}$ | Informational time with material space — the crossing |
| $i\mathbb{H}_{\mathbb{B}} = T_{\mathrm{m}} \oplus X_{\mathrm{i}}$ | Material time with informational space — the other crossing |
| $\mathbb{C}_{\mathbb{B}} = T_{\mathrm{m}} \oplus T_{\mathrm{i}}$ | The center, fixed space of quaternion conjugation: the one subspace with no spatial part, of real dimension two |
| ${}^{*}, \bar{\cdot}, \dagger, \flat = -\dagger$ | Complex, quaternion, Hermitian and anti-Hermitian conjugation; the four involutions, with $\dagger = \bar{\cdot}^{\,*}$ |
| $\{1, {}^{*}, \bar{\cdot}, \dagger\}$ | The four involutions commute and form a Klein four-group; $\dagger = \bar{\cdot}\circ{}^{*}$, and the signs of ${}^{*}$ and $\bar{\cdot}$ on the four blocks are its four characters |
| $T_{\mathrm{m}}, T_{\mathrm{i}}, X_{\mathrm{m}}, X_{\mathrm{i}}$ | The four coordinate blocks of $1 + 1 + 3 + 3 = 8$ real parameters |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form; positive definite on $\mathbb{H}_{\mathbb{B}}$, negative definite on $i\mathbb{H}_{\mathbb{B}}$, indefinite on $\mathbb{B}$ |
| $\tilde{P}_\pm(\hat{\boldsymbol\mu}) = \tfrac12(e_0 \pm i\hat{\boldsymbol\mu})$ | Idempotents of $\mathbb{M}_+$ crossing both halves; null elements, hence outside both halves |
| $\Phi(\mathbb{H}_{\mathbb{B}})$, $\Phi(i\mathbb{H}_{\mathbb{B}})$ | The quaternion matrices and $i$ times them; determinants definite and of opposite sign |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (1853), for the original quaternion algebra and the conjugations that give the real and imaginary halves.
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of the complexified algebra and its real subalgebras.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), Chapter 3, for the subspace structure of the biquaternions and the complexified quaternion algebra.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the involutions of the algebra, their fixed spaces and the corresponding matrix forms.
- S. J. Sangwine, T. A. Ell, and N. Le Bihan, "Fundamental representations and algebraic properties of biquaternions or complexified quaternions," *Advances in Applied Clifford Algebras* **21** (2011) 607–636, for the canonical decompositions and the conventions in applied use.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the grading of the algebra and the role of its even part.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the even subalgebra of spacetime algebra and the rotors it carries.

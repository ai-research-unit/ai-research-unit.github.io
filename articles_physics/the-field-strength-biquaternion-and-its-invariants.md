# __The Field-Strength Biquaternion and Its Invariants__

## Introduction

The companion article *Maxwell's Equations in the Biquaternionic Formulation* introduced the **field-strength biquaternion**

$$
\tilde{F} = \mathbf{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}
$$

as the single biquaternionic object that carries the electromagnetic field, and showed that, in a medium with permittivity $\epsilon$ and permeability $\mu$, the four Maxwell equations collapse into the one equation $\tilde{\nabla}\tilde{F} = -\tilde{R}$. In that article $\tilde{F}$ appears as a means to an end: the compact rewriting of the field equations. This article studies $\tilde{F}$ for its own sake.

Two features make the field strength worth treating separately. First, $\tilde{F}$ is *not* a four-vector. Unlike the four-potential $\tilde{A}$, whose scalar part is imaginary and whose vector part is real, the field-strength biquaternion has **vanishing scalar part** and a **mixed real/imaginary vector part**: its imaginary half carries the electric field and its real half the magnetic field. The field strength is therefore a different kind of object from the kinematic four-vectors that live in the material subspace $\mathbb{M}_-$, and its Lorentz transformation law is correspondingly different. Second, the **norm form** evaluated on $\tilde{F}$ is a complex scalar whose real and imaginary parts are the two classical Lorentz invariants, $E^2 - c^2B^2$ and $\mathbf{E}\cdot\mathbf{B}$, up to the medium factors $-\epsilon$ and $-2\epsilon c$. The algebraic apparatus built to describe the Minkowski metric thus delivers the electromagnetic invariants as well.

This article is the declared foundation for three later articles on electromagnetism in media, on the Lorentz force, and on radiation from accelerated charges. It therefore fixes the field-strength notation once and for all. The **canonical objects** are: the field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$; the electric and magnetic fields $\mathbf{E}$ and $\mathbf{H}$, together with the magnetic induction $\mathbf{B} = \mu\mathbf{H}$; the medium speed of light $c = 1/\sqrt{\epsilon\mu}$; the Riemann–Silberstein vector $\mathbf{V} = \mathbf{E} + ic\mathbf{B}$; the two invariants $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$ and $I_2 = \mathbf{E}\cdot\mathbf{B}$; and the energy density $W$ and Poynting vector $\mathbf{S}$. Nothing in this list is new notation; the first three come unchanged from the Maxwell article, and the rest are assembled from them.

The conventions are those of the read-list articles throughout. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$, and scalar imaginary $i$ commuting with the quaternion units. The three-dimensional complex **vector part** of $\mathbb{B}$ is denoted by its components $\mathbf{F} = \sum_k F_k e_k$, with the usual quaternion product $\mathbf{F}\mathbf{G} = -\mathbf{F}\cdot\mathbf{G} + \mathbf{F}\times\mathbf{G}$ for pure vectors. The conjugations are the quaternion conjugate $\bar{\cdot}$, the complex conjugate ${}^*$, and the Hermitian conjugate ${}^\dagger = \bar{\cdot}^{\,*} = {}^{*}\bar{\cdot}$, with the four real fixed-point subspaces $\mathbb{C}_{\mathbb{B}}$ (scalars), $\mathbb{H}_{\mathbb{B}}$ (real quaternions), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector) and $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector). The symbol $c$ always denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$; in vacuum it reduces to $c_0 = 1/\sqrt{\epsilon_0\mu_0}$.

## The Field-Strength Biquaternion

The definition is the one of the Maxwell article, repeated here because everything that follows depends on it:

$$
\tilde{F} = \mathbf{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}
= \sum_{k=1}^{3} F_k\, e_k,
\qquad
F_k = i\sqrt{\epsilon}\,E_k - \sqrt{\mu}\,H_k .
$$

Its scalar part vanishes identically,

$$
\mathrm{Sc}(\tilde{F}) = 0,
$$

so $\tilde{F}$ is a **pure-vector** biquaternion. Its three complex components $F_k$ each combine an electric and a magnetic piece: the electric contribution $i\sqrt{\epsilon}\,E_k$ is **purely imaginary** and the magnetic contribution $-\sqrt{\mu}\,H_k$ is **real**. The factor of $i$ on the electric part is the same factor that appears in the complex time coordinate $ict$. In the $ict$ convention the time direction is the imaginary direction, and the electric field carries the time index of the field tensor, so it is the electric part that acquires the factor $i$ while the magnetic part remains real. This is the algebraic reason for the asymmetric appearance of $\tilde{F}$.

The normalization factors $\sqrt{\epsilon}$ and $\sqrt{\mu}$ are the natural ones for a medium. Each term has the dimension of the square root of an energy density, since $\epsilon E^2$ and $\mu H^2$ are both energy densities; consequently $\tilde{F}$ has dimension $\sqrt{\text{energy density}}$, and the norm form calculated below has dimension of an energy density. With the constitutive relation $\mathbf{B} = \mu\mathbf{H}$ the magnetic term may also be written $\sqrt{\mu}\,\mathbf{H} = \mathbf{B}/\sqrt{\mu}$, so the field strength can equally be regarded as the pair $(\sqrt{\epsilon}\,\mathbf{E}, \mathbf{B}/\sqrt{\mu})$.

The field strength is not an independent object: it is obtained from the potential biquaternion $\tilde{A} = i\phi/c + \mathbf{A}$ by differentiation. In the biquaternion algebra the construction is

$$
\tilde{F} = \bar{\tilde{\nabla}}\tilde{A} - \mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{A}\right),
$$

the vector part of $\bar{\tilde{\nabla}}\tilde{A}$, where $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ is the biquaternionic gradient and $\bar{\tilde{\nabla}}$ its quaternion conjugate. In tensor language the same object is the antisymmetric rank-two tensor

$$
F^{\mu\nu} = \partial^\mu A^\nu - \partial^\nu A^\mu,
\qquad
F^{\mu\nu} =
\begin{pmatrix}
0 & iE_x/c & iE_y/c & iE_z/c \\
-iE_x/c & 0 & B_z & -B_y \\
-iE_y/c & -B_z & 0 & B_x \\
-iE_z/c & B_y & -B_x & 0
\end{pmatrix}.
$$

The tensor has six independent components — three electric and three magnetic — which is exactly the information carried by the three complex components $F_k$ of the pure-vector biquaternion. As the Maxwell article notes, the precise identification of $\mathbf{F}$ with the vector part of $\bar{\tilde{\nabla}}\tilde{A}$ depends on the normalization of the potential and on the sign convention for the fields; the unambiguous definition used here is the tensor formula together with the component combination $F_k = i\sqrt{\epsilon}E_k - \sqrt{\mu}H_k$.

## The Place of the Field Strength in the Algebra

The biquaternion algebra decomposes in several ways, and it is worth locating $\tilde{F}$ precisely in these decompositions, because its peculiar properties are consequences of its position.

**The vector part.** The pure-vector biquaternions form the complex three-dimensional subspace

$$
\mathrm{Vect}(\mathbb{B}) = \mathbb{C}e_1 \oplus \mathbb{C}e_2 \oplus \mathbb{C}e_3,
$$

of real dimension six. It is *not* one of the four fixed-point subspaces $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}, \mathbb{M}_+$ and $\mathbb{M}_-$; those are real subspaces containing a scalar direction, of which three are four-dimensional, whereas the vector subspace contains no scalar at all. The field strength lies entirely in this subspace, and the classical statement that the electromagnetic field has six independent components is exactly the statement that $\tilde{F}$ is a general element of $\mathrm{Vect}(\mathbb{B})$.

**The Hermitian decomposition.** The vector part intersects the two complementary subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ in the three-dimensional real subspaces

$$
\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_+ = \mathrm{span}_{\mathbb{R}}\{ie_1, ie_2, ie_3\},
\qquad
\mathrm{Vect}(\mathbb{B}) \cap \mathbb{M}_- = \mathrm{span}_{\mathbb{R}}\{e_1, e_2, e_3\}.
$$

The first consists of the pure **imaginary** vectors and the second of the pure **real** vectors. The two pieces of $\tilde{F}$ fall into these two intersections:

$$
\tilde{F} = \underbrace{i\sqrt{\epsilon}\,\mathbf{E}}_{\in\,\mathbb{M}_+} \;+\; \underbrace{\left(-\sqrt{\mu}\,\mathbf{H}\right)}_{\in\,\mathbb{M}_-}.
$$

The electric part is therefore **Hermitian** and the magnetic part **anti-Hermitian**, and $\tilde{F}$ is neither. Explicitly,

$$
\tilde{F}^\dagger = -\mathbf{F}^* = i\sqrt{\epsilon}\,\mathbf{E} + \sqrt{\mu}\,\mathbf{H},
$$

so that the Hermitian and anti-Hermitian parts of the field strength are

$$
\tfrac{1}{2}\left(\tilde{F} + \tilde{F}^\dagger\right) = i\sqrt{\epsilon}\,\mathbf{E},
\qquad
\tfrac{1}{2}\left(\tilde{F} - \tilde{F}^\dagger\right) = -\sqrt{\mu}\,\mathbf{H}.
$$

This expresses a familiar fact: the electric field transforms like the Hermitian sector and the magnetic field like the anti-Hermitian sector. It also shows why $\tilde{F}$ cannot lie in $\mathbb{M}_-$: the material subspace contains the real vectors but not the imaginary ones, and the electric half of the field strength uses the imaginary vector directions.

**The real/complex decomposition.** Equivalently, with respect to the complex conjugation ${}^*$ that fixes $\mathbb{H}_{\mathbb{B}}$,

$$
\tilde{F} = \underbrace{\left(-\sqrt{\mu}\,\mathbf{H}\right)}_{\in\,\mathbb{H}_{\mathbb{B}}} \;+\; \underbrace{i\sqrt{\epsilon}\,\mathbf{E}}_{\in\,i\mathbb{H}_{\mathbb{B}}},
$$

The scalar subspace $\mathbb{C}_{\mathbb{B}}$ receives no contribution, which is again $\mathrm{Sc}(\tilde{F}) = 0$; the decomposition used is $\mathbb{B} = \mathbb{H}_{\mathbb{B}} \oplus i\mathbb{H}_{\mathbb{B}}$. Thus the field strength uses the vector parts of $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ and the electric and magnetic halves of $\mathbb{M}_+$ and $\mathbb{M}_-$ respectively, and it touches $\mathbb{C}_{\mathbb{B}}$ not at all.

## The Norm Form and the Two Invariants

The norm form on $\mathbb{B}$ is

$$
N(\tilde{Q}) = \tilde{Q}\,\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2 .
$$

For a pure-vector biquaternion the quaternion conjugate is $\bar{\tilde{F}} = -\mathbf{F}$, and the quaternion product of two pure vectors is $\mathbf{F}\mathbf{G} = -\mathbf{F}\cdot\mathbf{G} + \mathbf{F}\times\mathbf{G}$. Hence

$$
\tilde{F}\,\bar{\tilde{F}} = \mathbf{F}(-\mathbf{F}) = \mathbf{F}\cdot\mathbf{F} = \sum_{k=1}^{3} F_k^2,
$$

because $\mathbf{F}\times\mathbf{F} = 0$. The cross term drops out for the norm form of a vector, and one is left with the **complex bilinear form**

$$
N(\tilde{F}) = \sum_{k=1}^{3} F_k^2,
$$

which is a complex scalar. Substituting $F_k = i\sqrt{\epsilon}E_k - \sqrt{\mu}H_k$ and expanding,

$$
N(\tilde{F}) = \sum_{k=1}^{3}\left(i\sqrt{\epsilon}E_k - \sqrt{\mu}H_k\right)^2
= -\epsilon\,\mathbf{E}^2 + \mu\,\mathbf{H}^2 - 2i\sqrt{\epsilon\mu}\,\mathbf{E}\cdot\mathbf{H}.
$$

This is the central computation of the article. Written with the magnetic induction $\mathbf{B} = \mu\mathbf{H}$ and the medium speed of light $c = 1/\sqrt{\epsilon\mu}$, the real and imaginary parts become

$$
\mathrm{Re}\,N(\tilde{F}) = -\epsilon\left(\mathbf{E}^2 - c^2\mathbf{B}^2\right),
\qquad
\mathrm{Im}\,N(\tilde{F}) = -2\epsilon c\,\mathbf{E}\cdot\mathbf{B}.
$$

The two real quantities appearing here are the two classical **Lorentz invariants** of the electromagnetic field, up to the factors $-\epsilon$ and $-2\epsilon c$:

$$
\boxed{\;I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2\;},
\qquad
\boxed{\;I_2 = \mathbf{E}\cdot\mathbf{B}\;}
$$

so that

$$
N(\tilde{F}) = -\epsilon\left[\,I_1 + 2ic\,I_2\,\right],
\qquad
I_1 = -\frac{1}{\epsilon}\,\mathrm{Re}\,N(\tilde{F}),
\qquad
I_2 = -\frac{1}{2\epsilon c}\,\mathrm{Im}\,N(\tilde{F}).
$$

The norm form is a single complex number, and it carries exactly two real invariants. It is the *fully contracted* object built from the field strength with no derivatives and no extra vectors, so these are the only two independent invariants of the field; any other algebraic invariant is a function of $I_1$ and $I_2$.

**The conjugate norm form.** The quaternion norm form is not the only natural quadratic object here. Because quaternion conjugation fixes the scalar part, conjugation acts on the vector components by $\bar{\tilde{F}} = -\mathbf{F}$; complex conjugation, by contrast, acts on the coefficients, $\tilde{F}^* = \mathbf{F}^*$. For the norm form of the complex-conjugate field,

$$
N(\tilde{F}^*) = N(\tilde{F})^*,
$$

so the norm form and its conjugate carry the same two real invariants. Equivalently, the reverse product is $\bar{\tilde{F}}\tilde{F} = \tilde{F}\bar{\tilde{F}} = N(\tilde{F})$ for a pure vector. The two invariants are therefore the two real components of the complex norm form.

**Vanishing of the norm form.** Because $\tilde{F}$ is a pure vector,

$$
\tilde{F}^2 = -\mathbf{F}\cdot\mathbf{F} = -N(\tilde{F}),
$$

so the norm form vanishes if and only if $\tilde{F}$ squares to zero. A nonzero element of $\mathbb{B}$ whose norm form vanishes is a **zero divisor**, and $\tilde{F}$ is nilpotent in that case. Thus

$$
N(\tilde{F}) = 0
\quad\Longleftrightarrow\quad
I_1 = 0 \ \text{ and }\ I_2 = 0
\quad\Longleftrightarrow\quad
\tilde{F} \text{ is a zero divisor}.
$$

The vanishing of the norm form is therefore the algebraic statement that the field is a **null (radiative) field**: $\mathbf{E}\perp\mathbf{B}$ and $|\mathbf{E}| = c|\mathbf{B}|$ pointwise. This is the same zero-divisor cone that underlies the light cone of $\mathbb{M}_-$, now realized inside the field-strength space. It is the algebraic seed of the radiation theory and will reappear in the later article on radiation from accelerated charges.

## Lorentz Invariance of the Invariants

The claim that $I_1$ and $I_2$ are Lorentz invariants is standard and can be checked directly. Under a boost with velocity $\mathbf{v}$ and Lorentz factor

$$
\gamma = \frac{1}{\sqrt{1 - \mathbf{v}^2/c^2}},
$$

the fields transform as

$$
\mathbf{E}' = \gamma\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right) - \frac{\gamma-1}{\mathbf{v}^2}\left(\mathbf{v}\cdot\mathbf{E}\right)\mathbf{v},
$$

$$
\mathbf{B}' = \gamma\left(\mathbf{B} - \frac{1}{c^2}\,\mathbf{v}\times\mathbf{E}\right) - \frac{\gamma-1}{\mathbf{v}^2}\left(\mathbf{v}\cdot\mathbf{B}\right)\mathbf{v}.
$$

The components parallel to the boost are unchanged, while the transverse components acquire a contribution from the other field. Substituting these expressions into $I_1$ and $I_2$, the cross terms cancel and the factors combine to $1/\gamma^2$ in precisely the way required, giving

$$
\mathbf{E}'^2 - c^2\mathbf{B}'^2 = \mathbf{E}^2 - c^2\mathbf{B}^2,
\qquad
\mathbf{E}'\cdot\mathbf{B}' = \mathbf{E}\cdot\mathbf{B}.
$$

Both invariants are therefore unchanged. This is consistent with, and can be derived from, the rotor-conjugation transformation of the four-potential established in the Maxwell article: the field strength is built from $\tilde{A}$ by differentiation, and differentiating a quantity that transforms by rotor conjugation produces a field that transforms in the antisymmetric-tensor representation, whose two independent scalar contractions are exactly $I_1$ and $I_2$.

There is a discrete subtlety worth recording. Under the **proper orthochronous** Lorentz group both $I_1$ and $I_2$ are invariant. Under **parity**, however, the electric field is a polar vector and the magnetic induction an axial vector, so $\mathbf{E}\to-\mathbf{E}$ and $\mathbf{B}\to\mathbf{B}$. Hence

$$
I_1 \to I_1,
\qquad
I_2 \to -I_2 .
$$

The quantity $I_1$ is an ordinary scalar and $I_2$ is a **pseudoscalar**. Both are invariants of the proper orthochronous group; only $I_1$ is invariant under parity.

## The Riemann–Silberstein Vector

The two real fields can be combined into one complex three-vector, and this combination is the form in which the invariants look simplest. Define the **Riemann–Silberstein vector**

$$
\mathbf{V} = \mathbf{E} + ic\,\mathbf{B}.
$$

The field-strength biquaternion is an overall constant multiple of it. Indeed, using $\mathbf{B} = \mu\mathbf{H}$ and $c = 1/\sqrt{\epsilon\mu}$,

$$
i\sqrt{\epsilon}\,\mathbf{V} = i\sqrt{\epsilon}\left(\mathbf{E} + ic\mathbf{B}\right)
= i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\epsilon}\,c\,\mathbf{B}
= i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}
= \tilde{F},
$$

because $\sqrt{\epsilon}\,c\,\mu = \sqrt{\mu}$. Thus

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{V}.
$$

This is the sense in which the Riemann–Silberstein vector and the field-strength biquaternion are **the same object**: they differ only by the constant $i\sqrt{\epsilon}$, so they carry identical information and have proportional invariants. The complex vector was introduced by Ludwik Silberstein in 1907, and the biquaternion formulation is its natural algebraic home: the complex vector is the vector part of a biquaternion with vanishing scalar part.

The norm form is now immediate. Since $\mathbf{V}$ is a complex three-vector,

$$
\mathbf{V}\cdot\mathbf{V} = \left(\mathbf{E} + ic\mathbf{B}\right)\cdot\left(\mathbf{E} + ic\mathbf{B}\right)
= \mathbf{E}^2 - c^2\mathbf{B}^2 + 2ic\,\mathbf{E}\cdot\mathbf{B}
= I_1 + 2ic\,I_2,
$$

and therefore

$$
N(\tilde{F}) = \left(i\sqrt{\epsilon}\right)^2 \mathbf{V}\cdot\mathbf{V} = -\epsilon\left(I_1 + 2ic\,I_2\right),
$$

in agreement with the direct computation. The two invariants are the real and imaginary parts of the complex number $\mathbf{V}\cdot\mathbf{V}$, up to constant factors.

The Riemann–Silberstein vector also linearizes the source-free field equations. In vacuum or in a homogeneous medium with no free sources, Maxwell's equations give $\mathrm{rot}\,\mathbf{E} = -\partial_t\mathbf{B}$ and $\mathrm{rot}\,\mathbf{B} = c^{-2}\partial_t\mathbf{E}$, and combining these,

$$
i\,\partial_t \mathbf{V} = c\,\mathrm{rot}\,\mathbf{V},
\qquad
\mathrm{div}\,\mathbf{V} = 0 .
$$

The first equation has the form of a Schrödinger equation whose Hamiltonian is $c\,\mathrm{rot}$; the second is the transverse (divergence-free) condition inherited from $\mathrm{div}\,\mathbf{D} = 0$ and $\mathrm{div}\,\mathbf{B} = 0$. This is the form in which the radiative content of the field is most transparent, and the null condition $\mathbf{V}\cdot\mathbf{V} = 0$ is precisely the condition that the complex vector be a null vector of the complexified spatial metric. A field whose Riemann–Silberstein vector is null, i.e. for which $N(\tilde{F}) = 0$, is a radiation field.

Finally, the antisymmetric field tensor decomposes into its **self-dual and anti-self-dual parts**. Define the Hodge dual by its action on the fields,
$$
\star:\ (\mathbf{E},\mathbf{B}) \mapsto (c\,\mathbf{B}, -\mathbf{E}/c),
\qquad
\star^2 = -1,
$$
which is the $\theta = \pi/2$ case of the duality rotation below. On the Riemann–Silberstein vector the dual is multiplication by $-i$,
$$
\mathbf{V}(\star F) = -i\,\mathbf{V},
\qquad
\mathbf{V}^*(\star F) = +i\,\mathbf{V}^* .
$$
The two combinations $F \pm i\star F$ are therefore the two parts, of opposite chirality,
$$
F + i\,\star F \ \longleftrightarrow\ 2\mathbf{V} = 2(\mathbf{E} + ic\mathbf{B}),
\qquad
F - i\,\star F \ \longleftrightarrow\ 2\mathbf{V}^* = 2(\mathbf{E} - ic\mathbf{B}),
$$
with $\star(F \pm i\star F) = \mp i\,(F \pm i\star F)$. The $\mathbf{V}$ part ($\star F = -iF$) is the **self-dual** half and the $\mathbf{V}^*$ part ($\star F = +iF$) the **anti-self-dual** half; the two halves are the two helicities of the radiation field. For a real field the two parts are complex conjugates of one another, so $\mathbf{V}^*$ adds no new data: $\mathbf{V}$ alone already carries the six real field components of $(\mathbf{E},\mathbf{B})$. On the complexified field space they are instead independent, and transform separately under the Lorentz group in the two three-dimensional complex representations — the two chiralities.

*Convention.* The dual is defined here by its action on $(\mathbf{E},\mathbf{B})$, the real-time convention with $\star^2 = -1$, which is the form in which the self-dual/anti-self-dual split is standard. Two sign conventions are in circulation for the star. We use the one in which $\star$ is the $\theta = \pi/2$ duality rotation, giving $\star\mathbf{V} = -i\mathbf{V}$; the **self-dual** half is then the $\mathbf{V}$ combination $F + i\star F$ ($\star$-eigenvalue $-i$) and the **anti-self-dual** half the $\mathbf{V}^*$ combination $F - i\star F$ ($\star$-eigenvalue $+i$). With the opposite sign of $\epsilon^{\mu\nu\rho\sigma}$ the two names are exchanged and nothing else changes. The component-wise dual read off from the $ict$ tensor above, $(\star F)_{0k} = B_k$, is $-i$ times this one and has $\star^2 = +1$; it is the same decomposition, with the two parts appearing as the real $\pm1$ eigenfields $F \pm \star F$ instead of the complex ones $F \pm i\star F$.

## Duality Rotation

Maxwell's equations in a homogeneous medium possess a continuous symmetry that rotates the electric and magnetic parts into one another. For a real angle $\theta$, define

$$
\mathbf{E} \mapsto \mathbf{E}\cos\theta + c\,\mathbf{B}\sin\theta,
\qquad
\mathbf{B} \mapsto \mathbf{B}\cos\theta - \frac{1}{c}\,\mathbf{E}\sin\theta .
$$

In terms of the Riemann–Silberstein vector this is a phase rotation,

$$
\mathbf{V} \mapsto e^{-i\theta}\,\mathbf{V},
\qquad
\mathbf{V}^* \mapsto e^{+i\theta}\,\mathbf{V}^*,
$$

as one checks by expanding $e^{-i\theta}(\mathbf{E} + ic\mathbf{B})$. The object that transforms with $e^{+i\theta}$ is the complex conjugate $\mathbf{V}^* = \mathbf{E} - ic\mathbf{B}$, not the quaternion conjugate $\bar{\mathbf{V}}$, which for a pure vector is $\bar{\mathbf{V}} = -\mathbf{V}$ and therefore transforms with $e^{-i\theta}$. The special case $\theta = \pi/2$,

$$
\mathbf{E} \mapsto c\,\mathbf{B},
\qquad
\mathbf{B} \mapsto -\frac{1}{c}\,\mathbf{E},
$$

is the classical **electric–magnetic duality** transformation.

The transformation is a symmetry of the **source-free** Maxwell equations. Under it, $\mathrm{rot}\,\mathbf{E}' = -\partial_t\mathbf{B}'$ and $\mathrm{rot}\,\mathbf{B}' = c^{-2}\partial_t\mathbf{E}'$ are preserved, the two terms of each equation matching after use of $c^2 = 1/(\epsilon\mu)$. With free electric charges and currents present, the transformation is *not* a symmetry: it would map an electric charge into a magnetic charge. Duality relates solutions of the source-free equations, and it relates the electric and magnetic parts of a given solution.

The effect of the duality rotation on the invariants is clean. Writing $\mathbf{V}\cdot\mathbf{V} = I_1 + 2icI_2$, the phase rotation gives

$$
\mathbf{V}\cdot\mathbf{V} \mapsto e^{-2i\theta}\,\mathbf{V}\cdot\mathbf{V},
$$

so that

$$
I_1 \mapsto I_1\cos 2\theta + 2c\,I_2\sin 2\theta,
\qquad
2c\,I_2 \mapsto 2c\,I_2\cos 2\theta - I_1\sin 2\theta .
$$

In other words, the pair $(I_1,\,2cI_2)$ rotates by the doubled angle $2\theta$; the quantity

$$
I_1^2 + 4c^2 I_2^2 = \left|\mathbf{V}\cdot\mathbf{V}\right|^2 = \frac{1}{\epsilon^2}\left|N(\tilde{F})\right|^2
$$

is invariant under duality as well as under Lorentz transformations. Each of $I_1$ and $I_2$ is separately Lorentz invariant, but duality mixes them; only the combination above is invariant under both. Equivalently, in biquaternion language,

$$
N(\tilde{F}) \mapsto e^{-2i\theta}\,N(\tilde{F}),
$$

since the scalar $e^{-i\theta}$ commutes with quaternion conjugation, which fixes scalars. Duality is not a Lorentz transformation: it is an independent $U(1)$ symmetry of the source-free equations that rotates the complex norm form.

## How the Invariants Constrain the Field

The two invariants are the complete set of local, derivative-free invariants of the electromagnetic field, and they classify the field into a small number of types. The classification is Lorentz invariant, because $I_1$ and $I_2$ are.

**Null fields.** If $I_1 = 0$ and $I_2 = 0$, then $\mathbf{E}\perp\mathbf{B}$ and $|\mathbf{E}| = c|\mathbf{B}|$ at every event. Both invariants vanish, the norm form vanishes, and the field-strength biquaternion is a zero divisor. No Lorentz transformation can remove either field, because killing one would force the other to vanish as well by the invariant relation; the field is a pure radiation field in every frame. This is the case of greatest interest for the later article on radiation.

**Electric and magnetic types.** Suppose $I_2 = 0$ but $I_1 \neq 0$. Then $\mathbf{E}$ and $\mathbf{B}$ are perpendicular. If $I_1 > 0$, the electric magnitude dominates, and there is a Lorentz frame in which $\mathbf{B} = 0$: the field is purely electric, with $\mathbf{E}^2 = I_1$ in that frame. If instead $I_1 < 0$, there is a frame in which $\mathbf{E} = 0$: the field is purely magnetic, with $c^2\mathbf{B}^2 = -I_1$. In either case the invariant fixes the magnitude of the surviving field in its rest frame.

**Generic fields.** If $I_2 \neq 0$, no frame can make either field vanish, because $I_2$ would then vanish too. Instead there is a frame in which $\mathbf{E}$ and $\mathbf{B}$ are **parallel**. In that frame $I_2 = E_0 B_0$ (with signs) and $I_1 = E_0^2 - c^2B_0^2$, and eliminating $B_0$ gives a quadratic equation for $E_0^2$,

$$
E_0^4 - I_1 E_0^2 - c^2 I_2^2 = 0,
$$

whose positive root is

$$
E_0^2 = \frac{I_1 + \sqrt{I_1^2 + 4c^2 I_2^2}}{2},
\qquad
B_0 = \frac{I_2}{E_0}.
$$

The magnitudes are therefore completely determined by the two invariants. This is the precise sense in which the invariants constrain the field: they do not determine the field, but they determine the *type* of its Lorentz orbit and the field magnitudes in the frame in which that type is displayed.

**What the invariants do not constrain.** The invariants are two functions of the six real field components, so many distinct fields share the same pair $(I_1, I_2)$: they determine the local Lorentz type but not the field. They are pointwise kinematical quantities, not dynamical ones, and they are not in general conserved by the free-field evolution — a field that is null at one instant need not be null at the next.

**Contrast with the energy density.** The norm form is indefinite and complex: it can vanish, and it gives the Lorentz invariants. The **Hermitian form** is a different quadratic object, and it gives the positive energy. For the pure vector $\tilde{F}$,

$$
\tilde{F}\tilde{F}^\dagger = 2W\,e_0 + \frac{2i}{c}\,\mathbf{S},
\qquad
\tilde{F}^\dagger\tilde{F} = 2W\,e_0 - \frac{2i}{c}\,\mathbf{S},
$$

with the energy density and Poynting vector

$$
W = \frac{1}{2}\left(\epsilon\,\mathbf{E}^2 + \mu\,\mathbf{H}^2\right) = \frac{1}{2}\left\|\tilde{F}\right\|_E^2,
\qquad
\mathbf{S} = \mathbf{E}\times\mathbf{H}.
$$

The scalar part of $\tilde{F}\tilde{F}^\dagger$ is $2W$, twice the (non-negative) energy density, and its vector part is $\frac{2i}{c}\mathbf{S}$, $\frac{2}{c}$ times the imaginary unit times the Poynting vector; the result is an element of $\mathbb{M}_+$, as every Hermitian form must be. The contrast is instructive: the norm form is a Lorentz-invariant complex scalar that can vanish, while the Hermitian form is an $\mathbb{M}_+$-valued object whose scalar part is strictly positive and whose transformation law is not that of a scalar. The first classifies the field; the second measures it. This is the biquaternion expression of the familiar fact that the electromagnetic energy density is positive-definite, whereas the invariant $I_1$ is indefinite.

## Summary

The field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ is a pure-vector biquaternion with vanishing scalar part. It lies in the six-dimensional real vector part of $\mathbb{B}$, decomposed into an imaginary electric piece in the Hermitian subspace $\mathbb{M}_+$ and a real magnetic piece in the anti-Hermitian subspace $\mathbb{M}_-$. This is why the field strength is neither a four-vector nor an element of $\mathbb{M}_-$: it is an antisymmetric rank-two tensor, whose two halves occupy the two complementary sectors of the algebra.

The norm form of the field strength is the complex scalar

$$
N(\tilde{F}) = \tilde{F}\bar{\tilde{F}} = \sum_{k=1}^{3} F_k^2
= -\epsilon\left(I_1 + 2ic\,I_2\right),
\qquad
I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2,
\qquad
I_2 = \mathbf{E}\cdot\mathbf{B}.
$$

Its real and imaginary parts are the two Lorentz invariants of the field; the norm form and its complex conjugate carry the same pair. Both are invariant under the proper orthochronous Lorentz group, $I_1$ is parity-even and $I_2$ is a pseudoscalar. The norm form vanishes exactly when the field is null, in which case the field-strength biquaternion is a zero divisor.

The same object is, up to the constant $i\sqrt{\epsilon}$, the Riemann–Silberstein vector $\mathbf{V} = \mathbf{E} + ic\mathbf{B}$, whose self-product $\mathbf{V}\cdot\mathbf{V} = I_1 + 2icI_2$ is the complex number whose real and imaginary parts are the invariants, and which obeys the source-free equation $i\partial_t\mathbf{V} = c\,\mathrm{rot}\,\mathbf{V}$ with $\mathrm{div}\,\mathbf{V} = 0$.

Duality is the rotation $\mathbf{V}\mapsto e^{-i\theta}\mathbf{V}$; at $\theta = \pi/2$ it is the classical electric–magnetic duality. It is a symmetry of the source-free Maxwell equations, and it rotates the pair $(I_1, 2cI_2)$ by the angle $2\theta$, leaving $I_1^2 + 4c^2I_2^2$ invariant. Finally, the invariants classify the field into null, electric, magnetic, and generic types, and fix the field magnitudes in the frame that displays each type; they are the complete set of local, derivative-free invariants, but they are not a complete description of the field.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}}$ | Complex (scalar) subspace |
| $\mathrm{Vect}(\mathbb{B})$ | Complex three-dimensional vector part |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}$ | Biquaternionic gradient and its quaternion conjugate |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion (pure vector) |
| $\mathbf{E}, \mathbf{H}, \mathbf{B} = \mu\mathbf{H}$ | Electric field, magnetic field, magnetic induction |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $N(\tilde{F}) = \tilde{F}\bar{\tilde{F}}$ | Norm form (complex scalar) |
| $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$ | First Lorentz invariant (scalar) |
| $I_2 = \mathbf{E}\cdot\mathbf{B}$ | Second Lorentz invariant (pseudoscalar) |
| $\mathbf{V} = \mathbf{E} + ic\mathbf{B}$ | Riemann–Silberstein vector, $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{V}$ |
| $\star$ | Hodge dual, $\star(\mathbf{E},\mathbf{B}) = (c\mathbf{B}, -\mathbf{E}/c)$, $\star^2 = -1$ |
| $W = \tfrac{1}{2}(\epsilon\mathbf{E}^2 + \mu\mathbf{H}^2)$ | Electromagnetic energy density |
| $\mathbf{S} = \mathbf{E}\times\mathbf{H}$ | Poynting vector |
| $\mathbf{v}$ | Boost (frame) velocity |

## Further Reading

- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, and 24 (1907) 783–784, for the original complex-vector formulation of the electromagnetic field.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for a modern account of the complex-vector and duality structure.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard treatment of the field invariants and the transformation of the fields.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the invariant classification of the field and the existence of frames in which the fields are parallel or one vanishes.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the spacetime-algebra treatment of the field strength and its invariants.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of Lorentz transformations and the bivector structure of the field.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time* (Cambridge, 1984), for the self-dual and anti-self-dual decomposition of the field tensor.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the representation theory of the Lorentz group and its two three-dimensional complex representations.
- L. A. Alexeyeva, "Maxwell Equations, Their Hamiltonian and Biquaternionic Forms and Properties of Their Solutions" (2016), for the biquaternionic formulation of the field equations.
- A. Waser, "Application of Bi-Quaternions in Physics" (2000, updated 2007), for the biquaternionic treatment of the field and its energy–momentum.

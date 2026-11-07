# __The Spin–Statistics Theorem in Biquaternionic Form__

## Introduction

The **spin–statistics theorem** is the statement that the spin of a field and the bracket that quantizes it are not independent. In a relativistic quantum field theory on Minkowski space whose inner product is positive definite and whose Hamiltonian is bounded below, a field of integer spin must be quantized with **commutators** and a field of half-integer spin with **anticommutators**: integer-spin fields are bosons, half-integer-spin fields are fermions. The theorem is a statement about the *choice of bracket*, not about the representation of the Lorentz group; the representation fixes the spin, and the theorem says that locality, positivity and Lorentz invariance together fix the bracket that goes with it.

The theorem is not among the results the companion articles derive. *Canonical Quantization of the Biquaternion Dirac Field* imposes anticommutation relations on the free biquaternion field and lists the boundedness of the energy, together with microcausality and positivity, among the reasons the anticommutator is the appropriate one; it explicitly leaves the theorem itself to a dedicated article. *Fock Space and Creation/Annihilation Operators in Biquaternionic Form* finds that the algebra $\mathbb{B}$ hosts exactly one fermionic mode and no bosonic mode, and is careful to say that this is a *realization* and not a derivation of fermionic statistics. *The KMS Condition and the Biquaternion Framework* identifies a $\mathbb{Z}/2$ grading of the operator algebra as an additional structure that the biquaternion algebra does not by itself supply. This article is the dedicated treatment those three forward references call for. It does not rederive the parents' quantizations, plane waves or spin sums, which are used unchanged.

The division between what is established and what is only transcribed is stated at the outset and kept explicit.

- **Established, and recomputed below.** The rotation group acts inside $\mathbb{B}$ through the rotor group of unit real quaternions, which is the double cover of $SO(3)$; the rotor through $2\pi$ about any axis is $-e_t$. Under the rotor action the half-integer-spin representations are the odd tensor powers of the defining module, on which $-e_t$ acts as $-\mathrm{id}$, while the integer-spin representations — the material sector and the even tensor powers — are the ones that descend to the Lorentz group, on which $-e_t$ acts as $+\mathrm{id}$. For the free spin-$\tfrac12$ field the equal-time **anticommutator** is a delta and the equal-time **commutator** is not: the former receives a $\delta^{(3)}(\vec\Delta)$ from the even time term of the spin sum, the latter only a Bessel kernel that is nonzero at every spatial separation. In the single-mode truncation of the algebra the spin ladder operators *are* the mode ladder operators, $\vec\Upsilon_x=\frac{k_m\,\tilde{S}_{+}}{m\,c}$, with $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$, and the fermion-parity grading is the inner automorphism by the Hermitian involution $(-1)^F=i\vec e_z=\frac{2\,k_m\,\tilde{S}_{z}}{m\,c}$. The algebra hosts one such fermionic mode and no bosonic mode, for a reason that is a trace identity.
- **Transcribed, not derived.** The force of the theorem — that among the four pairings of spin class with bracket only two survive — is imported from relativistic quantum field theory. What the biquaternion presentation adds is that the two surviving pairings are the two *inequivalent structures the algebra actually carries*: the double-valued module for half-integer spin and the single-valued rotations of the material sector for integer spin, together with the trace identity that decides which bracket the finite algebra can host.
- **Gap, left visible.** The article does not *derive* spin–statistics from the biquaternion algebra. The one-mode coincidence is exact but finite-dimensional, and it does not lift to the field. This gap is stated in the sections where it arises and collected in the open questions.

## The Theorem and Its Ingredients

The theorem has three independent inputs, and it is useful to record which of them the biquaternion framework supplies.

1. **The Lorentz representation.** Spin is the intrinsic angular momentum of a particle: in the rest frame it is the label $s$ of the $SU(2)$ little-group representation, with $S^2=\frac{m^{2}\,c^{2}\,s\,(s+1)}{k_m^{2}}$ and $S_z=\frac{m\,c\,m_{s}}{k_m}$, and for a massless particle it is helicity. In the biquaternion framework that label is carried by the representation of the double cover $SL(2,\mathbb{C})$ of the restricted Lorentz group. The covering homomorphism has kernel $\{\pm e_t\}$, so a representation either descends to $SO^+(1,3)$ — the integer-spin case — or is a genuine two-valued representation of the cover — the half-integer-spin case.
2. **Locality (microcausality).** Observables at spacelike separation must commute. The field is not an observable; its bilinears are. If $\tilde{Ξ}_{\mathrm{sp}}$ anticommutes with itself at spacelike separation the bilinears commute, while if it commutes the bilinears do not, because the field's commutator is then a nonzero kernel. Locality therefore bears on the bracket, but only through the bilinears, and it is one of two constraints that must agree.
3. **Positivity.** The inner product on the state space must be positive definite and the Hamiltonian bounded below. For a half-integer-spin field, commuting modes give negative-norm states and a Hamiltonian unbounded below; anticommuting modes give the positive-definite fermionic Fock space and a bounded Hamiltonian.

The third ingredient is what makes the theorem non-trivial: the two-valuedness of the field makes $\tilde{Ξ}_{\mathrm{sp}}$ and $-\tilde{Ξ}_{\mathrm{sp}}$ physically indistinguishable, so the sign that separates commuting from anticommuting quantization is invisible in the classical field, and it has to be recovered from the bilinear $\bar{\tilde{Ξ}}_{\mathrm{sp}}\tilde{Ξ}_{\mathrm{sp}}$, that is from the norm. Locality and positivity are logically independent, and the theorem is the assertion that they always select the same bracket; for spin $\tfrac12$ both exclude the commuting one, and both exclusions are computed below.

The biquaternion framework supplies the first ingredient geometrically and the third ingredient only at the level of the finite single-mode algebra; it transcribes the second with the parents' plane-wave fields. The five sections that follow take them up in the order representation, mode, locality, positivity.

## Spin as a Representation of the Rotor Group

Rotations are realised in $\mathbb{B}$ by rotor conjugation. A rotation through $\theta$ about the unit axis $\vec u$ is generated by the unit real quaternion

$$
\tilde u(\theta,\vec u)=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\sum_k \vec u_k\vec e_k\in\mathbb{B}_{H},\qquad \tilde u\tilde u^{*}=e_t .
$$

It is the exponential of the spin angular momentum along $\vec u$. With the spin operators $\tilde S_k$ of *Special Element Conventions*,

$$
\tilde u(\theta,\vec u)=\exp\Big(-i\theta\sum_k\frac{k_m\,\vec u_{k}\,\tilde{S}_{k}}{m\,c}\Big)=\exp\Big(\tfrac{\theta}{2}\sum_k\vec u_k\vec e_k\Big),
$$

the second form following from the first because $\tilde S_k$ is $\frac{m\,c}{2\,k_m}i\vec e_k$ there, so $-i\tilde S_k/\hbar=\tfrac12\vec e_k$: the two imaginary units cancel, one from the exponent and one from $\tilde S_k$, by $i^2=-1$. Conjugation by $\tilde u$ rotates the vectors of the material sector $\mathbb{B}_{\Phi}$, while left multiplication by $\tilde u$ acts on the algebra read as a left module, and hence on states; the map $\tilde{Q}\mapsto\tilde u\tilde{Q}\tilde u^{*}$ on $\mathbb{B}_{\Phi}$ has kernel $\{\pm e_t\}$ and is the covering homomorphism onto the rotation group. The rotation group is the quotient of the rotor group, which is $SU(2)$, by $\{\pm e_t\}$. These facts are established in the companion articles on angular momentum and on the Lorentz group, and are recalled here because the spin–statistics dichotomy is a statement about which side of the cover a representation lives on.

The representations of the cover split into two classes, and the theorem's spin input is exactly that split. The algebra acts on itself by left multiplication, and that action is where its irreducible modules live. Read as a left module over itself, $\mathbb{B}$ affords only $s=\tfrac12$: since $\mathbb{B}\cong M_2(\mathbb{C})$ is simple, the algebra is two copies of the defining module $S$, so the half-integer-spin structure is **native to the algebra as a module**, and it is double-valued, because $-e_t$ acts on every element as $-\mathrm{id}$. The integer-spin representations are not modules of the algebra. $s=0$ is the centre under conjugation, where every rotor acts trivially; $s=1$ is the **adjoint action** on the three vector units $\vec e_k$ — equivalently on the three imaginary units $i\vec e_k$, since the central $i$ passes through a conjugation unchanged; and conjugation on the four-dimensional $\mathbb{B}_{\Phi}$ is the direct sum $0\oplus1$ under rotations, the scalar $e_t$ fixed and the vector $\vec e_k$ rotating, which is the four-vector once the boosts are included. Tensor powers fill the rest. The $n$-fold tensor power of $S$ splits into spins $s=\tfrac{n}{2},\tfrac{n}{2}-1,\dots$, down to $\tfrac12$ for odd $n$ and to $0$ for even $n$, and on every summand $-e_t$ acts as $(-1)^{n}$, one factor of $-1$ from each of the $n$ factors. So the odd powers carry only half-integer spins and the even powers only integer ones, and the dichotomy is the parity of the power.

| Representation | Carrier | Action of the rotor | Action of $-e_t$ | Spin |
|---|---|---|---|---|
| Defining module | $\mathbb{B}$ as a left module, two copies of $S$ | left multiplication $X\mapsto\tilde uX$ | $-\mathrm{id}$ | $\tfrac12$ |
| Odd tensor powers | tensor powers of $S$ | left multiplication | $-\mathrm{id}$ | half-integer |
| Vector (adjoint) | the vector units $\vec e_k$ | conjugation $\vec Q\mapsto\tilde u\vec Q\tilde u^{*}$ | $+\mathrm{id}$ | $1$ |
| Even tensor powers | tensor powers of $S$ | tensor action | $+\mathrm{id}$ | integer |

On a representation of the cover with spin $s$ the nontrivial kernel element $-e_t$ acts as $(-1)^{2s}$, which is $+1$ for integer $s$ and $-1$ for half-integer $s$, and the table lists the elementary instances. This is the representation-theoretic content of the theorem's spin input, and it is the content of the companion article on the Lorentz group's classification, where the descent condition $m+n\in\mathbb{Z}$ separates the two cases.

## The Sign of the Two-Pi Rotation

Evaluate the rotor at $\theta=2\pi$ and $\theta=4\pi$:

$$
\boxed{\;\tilde u(2\pi,\vec u)=\cos\pi\,e_t=-e_t,\qquad \tilde u(4\pi,\vec u)=\cos 2\pi\,e_t=e_t\;}.
$$

The $2\pi$ rotation is the nontrivial element of the kernel $\{\pm e_t\}$ of the covering, whatever the axis. Its action therefore separates the two classes of the table above in the sharpest possible way.

- On a **four-vector** $\tilde{Q}\in\mathbb{B}_{\Phi}$, conjugation by $-e_t$ is trivial, $(-e_t)\tilde{Q}(-e_t)^{*}=\tilde{Q}$. A rotation by $2\pi$ returns a vector to itself; the vector representation is single-valued.
- On an **element** $X$ of $\mathbb{B}$ read as a left module, $2\pi$ means left multiplication by $-e_t$, so $X\mapsto-X$. The left action of the cover is double-valued; only a rotation by $4\pi$ returns the element to itself.

The sign is not an artefact of a basis. It is the image of the nontrivial element of $\pi_1(SO^+(1,3))\cong\mathbb{Z}/2$ under the covering homomorphism, and it is why the left action of the cover has no single-valued representative on the algebra.

For an **observable** the sign cancels. The gauge-invariant bilinears of the field are quadratic, $\bar{\tilde{Ξ}}_{\mathrm{sp}}\,\mathcal{O}\,\tilde{Ξ}_{\mathrm{sp}}$ with $\mathcal{O}$ a fixed element of the algebra and $\bar{\tilde{Ξ}}_{\mathrm{sp}}X=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x)$ the Dirac adjoint, and under $\tilde{Ξ}_{\mathrm{sp}}\mapsto-\tilde{Ξ}_{\mathrm{sp}}$ they are unchanged. This is the precise sense in which $\tilde{Ξ}_{\mathrm{sp}}$ and $-\tilde{Ξ}_{\mathrm{sp}}$ are physically indistinguishable, and it is why the classical field contains no information about whether its quanta are bosons or fermions. The $2\pi$ sign is a representation-theoretic fact about the defining module; it is *half* of the spin–statistics connection, not the whole of it.

At the level of the operator algebra the two signs are worth distinguishing, because they act on different objects. A rotation by $2\pi$ multiplies the field by $-e_t$, so $\tilde{Ξ}_{\mathrm{fop}}\mapsto-\tilde{Ξ}_{\mathrm{fop}}$. The parity element $(-1)^F$ acts by inner automorphism on the algebra of the single mode, and it flips exactly the odd elements: $(-1)^F\vec\Upsilon_x(-1)^F=-\vec\Upsilon_x$ and likewise $\vec\Upsilon_y$, while $\tilde\Pi_-$ and $e_t$ are fixed. Both operations are $-\mathrm{id}$ on the odd part and $+\mathrm{id}$ on the even part, and that is the operator-level form of $(-1)^{2s}=(-1)^F$ at $s=\tfrac12$. It is a consistency of two structures; it does not yet say that the bracket *must* anticommute.

## The Algebra's Own One Fermionic Mode

The finite-dimensional algebra contains one fermionic mode, and the mode operators are the spin ladder operators. This is the finding of the Fock-space article, and it is the one place where the spin-$\tfrac12$ structure and the fermionic canonical relation are the same elements of $\mathbb{B}$ rather than two structures placed side by side.

The spin operators are the elements $\tilde S_k\in\mathbb{B}_{\Psi}$ of *Special Element Conventions*, with the ladder combinations $\tilde S_\pm=\frac{m\,c}{2\,k_m}(i\vec e_x\mp \vec e_y)$. The Fock-space article's truncated ladder is the standard pair $\vec\Upsilon_x,\vec\Upsilon_y$ of the same convention, §*The Nilpotent Convention*,

$$
\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)=\frac{k_m\,\tilde{S}_{+}}{m\,c},\qquad
\vec\Upsilon_y=\tfrac12(i\vec e_x+\vec e_y)=\frac{k_m\,\tilde{S}_{-}}{m\,c},
$$

and direct computation gives

$$
\boxed{\;\vec\Upsilon_x^2=0,\qquad (\vec\Upsilon_y)^2=0,\qquad
\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t,\qquad
[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z\ne e_t\;}.
$$

So the truncated ladder satisfies the **fermionic** canonical anticommutation relations exactly, with no truncation error, while its commutator fails the bosonic relation by a nonzero, non-central element. The number operator and the fermion-parity element are

$$
\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12(e_t-i\vec e_z),\qquad
(-1)^F=e_t-2\tilde\Pi_-=i\vec e_z=\frac{2\,k_m\,\tilde{S}_{z}}{m\,c},
$$

with $\tilde\Pi_-^2=\tilde\Pi_-$ and spectrum $\{0,1\}$, so the single-mode occupation is valued in $\{0,1\}$. The parity element is Hermitian, squares to $e_t$, and gives the $\mathbb{Z}/2$ grading by inner automorphism,

$$
(-1)^F\vec\Upsilon_x\,(-1)^F=-\vec\Upsilon_x,\qquad
(-1)^F\tilde\Pi_-\,(-1)^F=\tilde\Pi_-.
$$

This is a sharp statement about the $\mathbb{Z}/2$ grading that the KMS article identifies as missing: for one mode it is not missing at all. It is realized **inside** $\mathbb{B}$ as conjugation by a Hermitian involution of the informational sector, and its odd subspace is the two-complex-dimensional span of $\vec\Upsilon_x$ and $\vec\Upsilon_y$. What the KMS article requires for a field is a grading on the *operator algebra of all modes*; the single-mode element above is not that, and the field grading is not an element of $\mathbb{B}$ by the dimension count. The two statements are compatible: the grading is algebraic for one mode and external for the field.

The bosonic counterpart fails for a sharper reason, a trace identity, worth recording separately from the dimension count. In $\mathbb{B}$ a canonical commutator would have to be central, $[\vec\Upsilon_x,\vec\Upsilon_y]=c\,e_t$ with $c\in\mathbb{C}$, since the centre is $\mathbb{B}_{C}=\mathbb{C}e_t$. It is not central: the computed value is $i\vec e_z$, which anticommutes with $\vec e_x$ and with $\vec e_y$ and so lies outside the centre. That alone rules the relation out. The trace argument then rules out a central value independently, and it uses nothing but linearity: the scalar part annihilates every commutator, $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$, while $\mathrm{Sc}(c\,e_t)=c$, so

$$
0=\mathrm{Sc}\big([\vec\Upsilon_x,\vec\Upsilon_y]\big)=c,
$$

and hence $c=0$. No pair in $\mathbb{B}$ realizes the Heisenberg relation. The algebra hosts one fermionic mode and no bosonic mode; the second relation, $\vec\Upsilon_x\vec\Upsilon_y=e_t-\vec\Upsilon_y\vec\Upsilon_x$, which a fermionic mode satisfies and a bosonic mode cannot, is the identity that decides it.

The dimension count makes the same point. $\dim_\mathbb{C}M_2(\mathbb{C})=4=\dim_\mathbb{C}\mathbb{B}$, and the four elements $e_t,\vec\Upsilon_x,\vec\Upsilon_y,\vec\Upsilon_x\vec\Upsilon_y=\tilde\Pi_+$ span the algebra; one mode saturates it, so no second mode can be added, since $m$ fermionic modes generate $M_{2^m}(\mathbb{C})$, of dimension $4^m$, which exceeds four as soon as $m\ge2$. Whether the framework *selects* the fermionic structure, or merely has room for exactly one instance of it, is the open question the Fock-space article raises and this article does not decide. The single-mode coincidence is exact; it is a coincidence of dimensions until something more is said.

## Microcausality: The Equal-Time Brackets

The operator-level content of the theorem is a computation with the parents' free field. Every derivative of the field in this article is the corpus gradient $\tilde\nabla$ or its conjugate $\tilde\nabla^{\natural}$ of *Operator and Calculus Conventions*, §*The Gradient*, with $\Box=\tilde\nabla\tilde\nabla^{\natural}$ the d'Alembertian there; on the material sector $\partial/\partial R_t=-(i/c)\,\partial/\partial r'_t$, so $\Box=\Delta_Q-c^{-2}\partial^2/\partial {r'_t}^2$. No other derivative operator is written.

The field is the element-valued map $\tilde{Ξ}_{\mathrm{fop}}:\mathbb{R}^{1,3}\to\mathbb{B}$ of *Canonical Quantization of the Biquaternion Dirac Field*, with the mode expansion

$$
\tilde{Ξ}_{\mathrm{fop}}(X,r'_t)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{\sqrt{2E_{\vec p}}}
\sum_{r=1}^{2}\Big[a_{\mathrm{fop},r}(\vec p)\,\tilde{Ξ}_{\mathrm{sp},+}^{(r)}(\vec p)\,\exp(-ip\cdot x)
+b_{\mathrm{fop},r}^{\dagger}(\vec p)\,\tilde{Ξ}_{\mathrm{sp},-}^{(r)}(\vec p)\,\exp(+ip\cdot x)\Big],
$$

where $\tilde{Ξ}_{\mathrm{sp},\pm}^{(r)}(\vec p)$ are the parent's positive- and negative-frequency amplitudes, elements of $\mathbb{B}$, and $\tilde{Ξ}_{\mathrm{fop}}^{\dagger}$ is the Hermitian conjugate.

The corpus's Dirac equation is one equation per chirality, both acting from the left,

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$

the mass being the off-diagonal coupling of the two halves. On the single element that carries the four complex components of the field it is one two-sided action, written with both elements in position:

$$
\mathbb{D}:\ \tilde X\longmapsto-\frac{\partial\tilde X}{\partial r'_t}\vec e_x-\sum_k\vec e_k\frac{\partial\tilde X}{\partial R_k}\vec e_y .
$$

Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The time term carries $e_t$ on the left, and $e_t$ is the unit, so that term is a single right multiplication by $\vec e_x$; each spatial term carries $\vec e_k$ on the left and $\vec e_y$ on the right, so the spatial part is genuinely two-sided and is the multiplication by no single element. Both elements stand in position in the display, and the operator is never written as a product of two one-sided symbols: a single glyph for the pair of one-sided factors would hide exactly the information the computation below uses. On a plane wave the same operator has the symbol

$$
\mathbb{D}_p:\ \tilde X\longmapsto iE_{\vec p}\,\tilde X\vec e_x-i\sum_k  p_k\,\vec e_k\tilde X\vec e_y,
\qquad
\mathbb{D}_p^2=\frac{p_0^2-|\vec p|^2}{\frac{m^{2}\,c^{2}}{k_m^{2}}}=k_m^{2},
$$

because $\exp(-ip\cdot x)$ gives $-iE_{\vec p}$ to the time derivative and $+ip_k$ to the spatial ones. The glyph is the pair operator's, of *Operator and Calculus Conventions*: on the pair it is $\mathbb{D}(\tilde{Ξ}_{\mathrm{sp},R},\tilde{Ξ}_{\mathrm{sp},L})=(\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R},\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L})$ with $\mathbb{D}^2=\Box I$, and on one element, which is how the equal-time computation uses it, it is the coordinate form above with $\mathbb{D}^2=\Box$. The square is scalar: the cross terms cancel because left and right multiplications commute, the time term contributes $-\partial^2/\partial {r'_t}^2$, and the spatial terms contribute $+\Delta_Q$ because $\vec e_y^2=-e_t$ and $\vec e_k\vec e_l+\vec e_l\vec e_k=-2\delta_{kl}e_t$. Verified on the symbol at random momenta, with $p^2=p_0^2-|\vec p|^2$: $\mathbb{D}_p^2-p^2I$ to $2.7\times10^{-15}$.

The parents' spin sums are the two completeness identities

$$
\sum_{r=1}^{2}\tilde{Ξ}_{\mathrm{sp},+}^{(r)}\,\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},+}^{(r)*}\tilde{Ξ}\big)=(\mathbb{D}_p+m)\big(\tilde{Ξ}\,i\vec e_x\big),\qquad
\sum_{r=1}^{2}\tilde{Ξ}_{\mathrm{sp},-}^{(r)}\,\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},-}^{(r)*}\tilde{Ξ}\big)=(\mathbb{D}_p-m)\big(\tilde{Ξ}\,i\vec e_x\big)
$$

for every $\tilde{Ξ}\in\mathbb{B}$. The right multiplication by $i\vec e_x$ is the factor that the Dirac adjoint carries, moved onto the argument: $\bar{\tilde{Ξ}}_{\mathrm{sp}}X=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x)$, and here it multiplies the test element, not the field, so the identity stays an identity of operators on one element. The identities are operator statements and not statements about solutions, and the second carries the opposite mass sign because the negative-frequency branch has the covariant norm $-2m$. Verified with the parent's covariant normalizations $\langle\tilde{Ξ}_{\mathrm{sp},\pm}^{(r)},\tilde{Ξ}_{\mathrm{sp},\pm}^{(s)}\rangle_{\mathrm D}=\pm2m\delta_{rs}$ at random momenta: the norms to $1.8\times10^{-15}$ and the two identities to $2.1\times10^{-14}$.

The field is element-valued; the biquaternion content is the algebra on which it is built and the notation, and the mode algebra is imposed. Two choices are available. The **Fermi choice** imposes

$$
\{a_{\mathrm{fop},r}(\vec p),a_{\mathrm{fop},s}^{\dagger}(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k),\qquad
\{b_{\mathrm{fop},r}(\vec p),b_{\mathrm{fop},s}^{\dagger}(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k),
$$

with all other brackets vanishing, and the **Bose choice** replaces both braces by brackets.

**The anticommutator (Fermi choice).** At equal times the two branches enter with opposite phases, and with $\theta=\vec p\cdot\vec\Delta$, where $\vec\Delta=X-Y$ is the separation and $X=r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, $Y$ likewise (the sign of $\theta$ is fixed by the mode-expansion convention and drops out of the anticommutator, only $\cos\theta$ surviving there), the completeness identities give

$$
\sum_r\Big[\tilde{Ξ}_{\mathrm{sp},+}^{(r)}\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},+}^{(r)*}\tilde{Ξ}\big)\exp(+i\theta)
+\tilde{Ξ}_{\mathrm{sp},-}^{(r)}\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},-}^{(r)*}\tilde{Ξ}\big)\exp(-i\theta)\Big]
=2\cos\theta\,\mathbb{D}_p\big(\tilde{Ξ}\,i\vec e_x\big)+2im\sin\theta\,\big(\tilde{Ξ}\,i\vec e_x\big).
$$

The time part of $\mathbb{D}_p$ gives $iE_{\vec p}(\tilde{Ξ} i\vec e_x)\vec e_x=E_{\vec p}\tilde{Ξ}$, because $i\vec e_x\,i\vec e_x=i^2\vec e_x^2=e_t$; it is even in $\vec p$, and so is $\cos\theta$. The spatial part $-i\sum_kp_k\vec e_k(\tilde{Ξ} i\vec e_x)\vec e_y$ and the mass term $2im\sin\theta(\tilde{Ξ} i\vec e_x)$ are odd, because $\sin\theta$ and $p_k$ are. The odd terms vanish under symmetric integration. Division by $2E_{\vec p}$ leaves $\cos\theta$ times the identity on the test element, which integrates to $\delta^{(3)}(\vec\Delta)$, so the equal-time relation is the component statement

$$
\boxed{\;\{\tilde{Ξ}_{\mathrm{fop},\mu}(X,r'_t),\tilde{Ξ}_{\mathrm{fop},\nu}^{\dagger}(Y,r'_t)\}=\delta_{\mu\nu}\,\delta^{(3)}(\vec\Delta)\;},
$$

the indices $\mu,\nu$ running over the four units, and the anticommutator is local. Parity in $\vec p$ decides what survives: the time part of $\mathbb{D}_p$ is even and remains, the spatial part and the mass term are odd and cancel.

**The commutator (Bose choice for the same field).** Replacing the plus between the branches by a minus, the same completeness identities give

$$
\sum_r\Big[\tilde{Ξ}_{\mathrm{sp},+}^{(r)}\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},+}^{(r)*}\tilde{Ξ}\big)\exp(+i\theta)
-\tilde{Ξ}_{\mathrm{sp},-}^{(r)}\mathrm{Sc}\big(\tilde{Ξ}_{\mathrm{sp},-}^{(r)*}\tilde{Ξ}\big)\exp(-i\theta)\Big]
=2i\sin\theta\,\mathbb{D}_p\big(\tilde{Ξ}\,i\vec e_x\big)+2m\cos\theta\,\big(\tilde{Ξ}\,i\vec e_x\big).
$$

Here the time part of $\mathbb{D}_p$ multiplies the odd factor $2i\sin\theta$ and drops, while the mass term and the spatial part of $\mathbb{D}_p$ survive, the odd $p_k$ cancelling the odd $\sin\theta$:

$$
\frac{1}{2E_{\vec p}}\Big[2m\cos\theta\,\big(\tilde{Ξ}\,i\vec e_x\big)+2\sin\theta\sum_k p_k\,\vec e_k\big(\tilde{Ξ}\,i\vec e_x\big)\vec e_y\Big].
$$

Integrating with $\int\frac{d^3p}{(2\pi)^3}\,\frac{\cos\theta}{E_{\vec p}}=F(\vec\Delta)$ and $\int\frac{d^3p}{(2\pi)^3}\,\frac{p_k\sin\theta}{E_{\vec p}}=-\nabla_kF$, and using $(\tilde{Ξ}\,i\vec e_x)\vec e_y=i\tilde{Ξ}\vec e_z$, leaves

$$
[\tilde{Ξ}_{\mathrm{fop}}(X,r'_t),\tilde{Ξ}_{\mathrm{fop}}^{\dagger}(Y,r'_t)]\,\tilde{Ξ}
=i\,mF(\vec\Delta)\,\tilde{Ξ}\vec e_x-i\sum_k\vec e_k\,\tilde{Ξ}\vec e_z\,\nabla_kF(\vec\Delta),
\qquad
F(\vec\Delta)=\int\!\frac{d^3p}{(2\pi)^3}\,\frac{1}{E_{\vec p}}\cos(\vec p\cdot\vec\Delta),
$$

with $\nabla_k=\partial/\partial\Delta_k$. For $m>0$ the kernel is $F(\vec\Delta)=\dfrac{m}{2\pi^2|\vec\Delta|}\,K_1\!\big(m|\vec\Delta|\big)$, the modified Bessel function of the second kind. The identity $\int_0^\infty\frac{p}{E}\sin(p\Delta)\,dp=mK_1(m\Delta)$ is the derivative in $\Delta$ of $\int_0^\infty\frac{\cos(p\Delta)}{E}\,dp=K_0(m\Delta)$, and both were checked numerically for $m=1$ and $\Delta=0.5,2,5,10$ to thirty digits. Nothing cancels: $F$ is positive and decaying, and $\nabla_kF$ vanishes only where $\Delta_k$ does, so the kernel is nonzero for **every** $\vec\Delta\ne 0$. It decays exponentially for large separations, but it does not vanish. So at equal times and spatial separation $\vec\Delta\ne 0$ — a spacelike separation — the commutator of the spin-$\tfrac12$ field is nonzero, while the anticommutator is zero. The Bose choice fails microcausality for a half-integer-spin field.

The chiral pair has a compact covariant form. With the gradient and its conjugate fixed above, $\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\Box$, and the mass couples the two chiralities through the pair of the preceding section. Each member is a one-sided action: $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$ is the left action of the gradient on the right-handed half, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ the left action of its conjugate on the left-handed half. The pair is kept as two equations because the two act on different objects, both from the left, and the conjugate gradient $\natural$ is what separates them. Together they are the pair operator $\mathbb{D}$ acting on $(\tilde{Ξ}_{\mathrm{sp},R},\tilde{Ξ}_{\mathrm{sp},L})$, with $\mathbb{D}^2=\Box I$, and the mass is the off-diagonal coupling of the two halves rather than a term inside either. With the field quantized by anticommutators, the general two-point functions are

$$
\{\tilde{Ξ}_{\mathrm{fop}}(x),\bar{\tilde{Ξ}}_{\mathrm{sp},\mathrm{fop}}(y)\}=(\mathbb{D}+k_m)\,\Delta_{\mathrm{A}}(x-y),
\qquad
\langle0|[\tilde{Ξ}_{\mathrm{fop}}(x),\bar{\tilde{Ξ}}_{\mathrm{sp},\mathrm{fop}}(y)]|0\rangle=(\mathbb{D}+k_m)\,G_{\mathrm{S}}(x-y),
$$

with $\bar{\tilde{Ξ}}_{\mathrm{sp},\mathrm{fop}}(y)=\tilde{Ξ}_{\mathrm{fop}}^{\dagger}(y)\,i\vec e_x$ the Dirac adjoint written with its right multiplication in position. Here $\Delta_{\mathrm{A}}$ is the antisymmetric combination of the two branch phases — the Pauli–Jordan-type kernel, supported inside the light cone and vanishing for spacelike separation — and $G_{\mathrm{S}}$ is the symmetric combination, which does not vanish there. The anticommutator is a $c$-number and equals its own vacuum expectation; under anticommutation relations the commutator is not a $c$-number, and the second identity is its vacuum expectation, whose $c$-number part is what carries $G_{\mathrm{S}}$. The anticommutator inherits the vanishing of $\Delta_{\mathrm{A}}$; the commutator's vacuum expectation inherits the non-vanishing of $G_{\mathrm{S}}$. At equal times these reduce to the delta and to the Bessel kernel computed above. The exact normalizations of $\Delta_{\mathrm{A}}$ and $G_{\mathrm{S}}$ carry the conventional factor of $i$; the covariant form is the standard textbook identity and is recorded as such, and the equal-time form is what was recomputed here.

## The Energy and the Norm

The third ingredient is positivity, and it is where the finite algebra has a native statement. With the mode expansion, the Hamiltonian of the free field is

$$
H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}\,
\big(a_{\mathrm{fop},r}^{\dagger}a_{\mathrm{fop},r}-b_{\mathrm{fop},r}b_{\mathrm{fop},r}^{\dagger}\big).
$$

The sign of the antiparticle term is decided by the bracket. With the **Fermi choice**, $b_{\mathrm{fop}}b_{\mathrm{fop}}^{\dagger}=1-b_{\mathrm{fop}}^{\dagger}b_{\mathrm{fop}}$, so after normal ordering

$$
H=\sum_r\int\!\frac{d^3p}{(2\pi)^3}\,E_{\vec p}\,
\big(a_{\mathrm{fop},r}^{\dagger}a_{\mathrm{fop},r}+b_{\mathrm{fop},r}^{\dagger}b_{\mathrm{fop},r}\big)+E_0,
$$

which is non-negative on the Fock space up to the c-number $E_0$ that normal ordering removes. With the **Bose choice**, $b_{\mathrm{fop}}b_{\mathrm{fop}}^{\dagger}=1+b_{\mathrm{fop}}^{\dagger}b_{\mathrm{fop}}$, and the antiparticle contribution enters with the opposite sign, $a_{\mathrm{fop}}^{\dagger}a_{\mathrm{fop}}-b_{\mathrm{fop}}^{\dagger}b_{\mathrm{fop}}$: the energy is unbounded below as antiparticle number grows, and the vacuum is unstable. The same sign appears in the norm: the anticommutator gives the positive-definite fermionic Fock space, the commutator gives an indefinite metric. This is the parent quantization article's argument, and it is stated here because it is half of the theorem's force.

The finite algebra shows the same identity in miniature. The single fermionic mode satisfies $\vec\Upsilon_x\vec\Upsilon_y=e_t-\vec\Upsilon_y\vec\Upsilon_x$, so the normal-ordered Hamiltonian of one mode is $\frac{m\,c\,\omega\,\vec \Upsilon_{y}\,\vec \Upsilon_{x}}{k_m}\ge  0$ on the algebra, with spectrum $\{0,\frac{m\,c\,\omega}{k_m}\}$ because $\tilde\Pi_-^2=\tilde\Pi_-$. Its would-be bosonic partner would need $\vec\Upsilon_x\vec\Upsilon_y=e_t+\vec\Upsilon_y\vec\Upsilon_x$, i.e. $[\vec\Upsilon_x,\vec\Upsilon_y]=e_t$, which the trace identity excludes. The positivity of the energy and the fermionic bracket are the same statement about the sign in $\vec\Upsilon_x\vec\Upsilon_y=e_t\mp\vec\Upsilon_y\vec\Upsilon_x$.

## The Four Quantizations

Collecting the two spin classes and the two brackets, four pairings are possible, and the theorem is the statement that two of them fail.

| Spin class | Bracket | Representation of the cover | Outcome |
|---|---|---|---|
| Integer | Commutator | descends, $-e_t\mapsto+1$ | consistent: scalar field, Maxwell field |
| Half-integer | Anticommutator | genuine two-valued representation, $-e_t\mapsto-1$ | consistent: Dirac field, positive norm, bounded energy |
| Half-integer | Commutator | genuine two-valued representation | fails microcausality (Bessel kernel above) and has unbounded energy |
| Integer | Anticommutator | descends | fails microcausality: the field itself is an observable, so its **commutator** must vanish at spacelike separation, but under anticommutation relations the commutator is no longer the $c$-number antisymmetric (Pauli–Jordan) kernel and does not vanish |

The integer-spin row is the parents' integer-spin case. The biquaternion Maxwell field lives in $\mathbb{B}_{\Phi}$, the vector representation, on which $-e_t$ acts trivially, and its canonical quantization uses commutators; the scalar (Klein–Gordon) field has a commutator equal to the antisymmetric Pauli–Jordan kernel, which vanishes for spacelike separation, while its symmetric kernel does not. The half-integer rows are the defining-module case computed above. The two surviving pairings are precisely the two inequivalent structures the algebra carries: the double-valued module paired with anticommutators, and the single-valued material-sector representation paired with commutators.

The table also displays what the framework does and does not explain. The *spin class* column is algebraic: integer versus half-integer is the descent condition for the rotor action, and the $2\pi$ sign is the action of $-e_t$, both recomputed in $\mathbb{B}$. The *bracket* column is transcribed from field theory; the algebra does not, at the level developed here, force the pairing. And the two columns are tied together only through the theorem, which is why the one-mode coincidence of *The Algebra's Own One Fermionic Mode* is suggestive but not decisive: it exhibits one entry of the table — half-integer spin, anticommutator — inside $\mathbb{B}$, and says nothing about the other three.

## What the Framework Establishes and What It Only Transcribes

**Established, and recomputed.**

- The rotor group of unit real quaternions is the double cover of the rotation group; the rotor through $2\pi$ about any axis is $-e_t$, and through $4\pi$ is $e_t$.
- Under the rotor action, the half-integer-spin representations live on the odd tensor powers of the defining module, where $-e_t$ acts as $(-1)^{2s}=-1$, while the integer-spin representations live on the material sector $\mathbb{B}_{\Phi}$ and on the even tensor powers, where $-e_t$ acts as $+1$. The algebra affords $s=\tfrac12$ as a module, $s=0$ on the centre under conjugation, and $s=1$ through the adjoint action on the three vector units $\vec e_k$, the spatial part of $\mathbb{B}_{\Phi}$.
- The single-mode ladder operators are the spin ladder operators, $\vec\Upsilon_x=\frac{k_m\,\tilde{S}_{+}}{m\,c}$, and satisfy $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$; the number operator is $\tilde\Pi_-$, with $\tilde\Pi_-^2=\tilde\Pi_-$; and the fermion-parity grading is the inner automorphism by $(-1)^F=i\vec e_z=\frac{2\,k_m\,\tilde{S}_{z}}{m\,c}$, an element of $\mathbb{B}_{\Psi}$.
- No bosonic mode exists in $\mathbb{B}$. The target relation $[\vec\Upsilon_x,\vec\Upsilon_y]=e_t$ has $\mathrm{Sc}=1$, while the scalar part of any commutator is $0$; and the computed commutator $i\vec e_z$ is not central, so no rescaling of it can produce a central value either.
- For the free spin-$\tfrac12$ field built on the algebra, the equal-time anticommutator is $\delta_{\mu\nu}\delta^{(3)}(\vec\Delta)$ and the equal-time commutator is a nonzero kernel at every $\vec\Delta\ne 0$. The spatial part of $\mathbb{D}_p$ and the mass term are odd in $\vec p$ and cancel, while the time part is even and survives.
- The sign in $\vec\Upsilon_x\vec\Upsilon_y=e_t\mp\vec\Upsilon_y\vec\Upsilon_x$ is the sign of the antiparticle term in the Hamiltonian and the sign that decides positivity of the norm.

**Transcribed, not derived.**

- That the bracket is *forced* by the conjunction of locality, positivity and Lorentz invariance. The article exhibits the failure of the wrong choices; it does not prove that no other structure evades it.
- The covariant identities $\{\tilde{Ξ}_{\mathrm{fop}},\bar{\tilde{Ξ}}_{\mathrm{sp},\mathrm{fop}}\}=(\mathbb{D}+k_m)\Delta_{\mathrm{A}}$ and $[\tilde{Ξ}_{\mathrm{fop}},\bar{\tilde{Ξ}}_{\mathrm{sp},\mathrm{fop}}]=(\mathbb{D}+k_m)G_{\mathrm{S}}$, and the Pauli–Jordan-type and symmetric kernels.
- The scalar-field and Maxwell-field contrast, and the standard microcausality argument for integer spin.

**Gap, left visible.**

- The framework does not *derive* spin–statistics. The spin dichotomy is algebraic; the bracket pairing is imposed. The one-mode coincidence that relates the spin ladder to the fermionic mode is exact but finite-dimensional, and the field algebra is infinite-dimensional, where both the exterior and the symmetric algebra are available on the same footing.
- Higher spin is not algebraic in the same sense. The $s=1$ representation is the adjoint action, not a module, and higher spins need tensor products; whether the framework's integer-spin structure has a native quantization of its own is not established here.

## Open Questions

**1. Does the framework derive spin–statistics or only transcribe it?** The central question. The spin dichotomy is algebraic and the $2\pi$ sign is an element of the algebra; the bracket pairing is imported. The single-mode realization is the only place where the two meet inside $\mathbb{B}$, and it is finite-dimensional. Whether some structure of the algebra — a graded extension, a crossed product, or the full tensor algebra of the module — forces the pairing is open and is not decided here.

**2. Is the one-mode coincidence structural or dimensional?** The four elements $e_t,\vec\Upsilon_x,\vec\Upsilon_y,\vec\Upsilon_x\vec\Upsilon_y$ span $\mathbb{B}$, so the single fermionic mode fits exactly, and the same element that is the spin ladder is the fermionic mode ladder. Is this a reflection of the spin-$\tfrac12$ structure of the module, or a coincidence of dimensions? The article's honest answer is that it is a coincidence until something more is said.

**3. What is the grading for a field?** The single-mode parity $(-1)^F=i\vec e_z$ is an element of $\mathbb{B}$; the field grading is not, by the dimension count, and the KMS article's requirement of a $\mathbb{Z}/2$ grading on the field algebra stands. Can an extension of $\mathbb{B}$ carry it, and does that extension have a biquaternion interpretation?

**4. Integer-spin quantization in the algebra.** The vector representation appears through the adjoint action on the vector units, and its quantization is standard and imported. Is there a native construction of the integer-spin Fock space from the algebra that mirrors the single-mode fermionic one, and if not, what obstructs it beyond the trace identity?

**5. The massless limit and chirality.** The microcausality failure of the commutator was computed at $m>0$, where the surviving function is built on the Bessel kernel $K_1$. As $m\to 0$ the function $F$ becomes $1/(2\pi^2|\vec\Delta|^2)$ and still does not vanish, so the massless case is not qualitatively different. At $m=0$ the chiral pair decouples into the two Weyl equations $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$, each carrying one helicity; how the chiral pair and the helicity–chirality locking enter the theorem is not developed here.

**6. Empirical content.** The construction reproduces standard field theory. Any deviation would have to appear where the algebra is used beyond transcription — for example in a modification of the one-mode identification or in the coupling to the material sector; none is visible at the level developed here.

## Summary

The spin–statistics theorem pairs half-integer spin with anticommutators and integer spin with commutators. In the biquaternion framework the spin half of the theorem is algebraic and exact: the rotor group of unit real quaternions is the double cover of the rotation group, the rotor through $2\pi$ is $-e_t$, half-integer-spin representations live on the odd tensor powers of the defining module, where $-e_t$ acts as $-\mathrm{id}$, and integer-spin representations live on the material sector $\mathbb{B}_{\Phi}$ and on the even tensor powers, where it acts as $+\mathrm{id}$. The framework's finite algebra also contains one fermionic mode, whose ladder operators are the spin ladder operators, $\vec\Upsilon_x=\frac{k_m\,\tilde{S}_{+}}{m\,c}$, and whose parity grading is the Hermitian element $(-1)^F=i\vec e_z=\frac{2\,k_m\,\tilde{S}_{z}}{m\,c}$; no bosonic mode exists, because a canonical commutator would be central and traceless.

The statistics half is transcribed with the parents' field. For the free spin-$\tfrac12$ field, the equal-time anticommutator is $\delta_{\mu\nu}\delta^{(3)}(\vec\Delta)$, the spatial part of $\mathbb{D}_p$ and the mass term cancelling as odd functions of $\vec p$; the equal-time commutator, by contrast, leaves the kernel $i\,mF(\vec\Delta)\,\vec e_x-i\sum_k\vec e_k\vec e_z\,\nabla_kF(\vec\Delta)$ and fails to vanish at any spatial separation. The same sign that selects the anticommutator selects the positive sign in $\vec\Upsilon_x\vec\Upsilon_y=e_t-\vec\Upsilon_y\vec\Upsilon_x$, and hence a bounded Hamiltonian and a positive-definite norm.

What the framework establishes is that the two pairings which survive the theorem are the two inequivalent structures the algebra actually carries, and that the $2\pi$ sign which distinguishes them is an element of the algebra. What it does not establish is that the algebra forces the pairing; spin–statistics is exhibited in biquaternionic form, not derived from it. The one-mode coincidence is the visible edge of the question, and it is left as the article's central open problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_j \vec e_k=\epsilon_{jkl}\vec e_l$ $(j\ne k)$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{B}_{H}$, $\mathbb{B}_{C}$ | Real-quaternion subspace; centre $\mathbb{C}e_t$ |
| $\mathrm{Sc}(X)=X_t$ | Scalar part of an element; it annihilates every commutator, $\mathrm{Sc}(XY)=\mathrm{Sc}(YX)$ |
| $\tilde u(\theta,\vec u)=\cos\tfrac{\theta}{2}e_t+\sin\tfrac{\theta}{2}\sum_k \vec u_k\vec e_k$ | Rotation rotor (unit real quaternion), $\vec u$ the unit axis |
| $\tilde u(2\pi,\vec u)=-e_t$, $\tilde u(4\pi,\vec u)=e_t$ | The two-valued sign of the left action on the algebra |
| $\tilde S_k=\frac{m\,c}{2\,k_m}i\vec e_k$, $\tilde S_\pm=\frac{m\,c}{2\,k_m}(i\vec e_x\mp \vec e_y)$ | Spin operators in $\mathbb{B}_{\Psi}$ ($k=x,y,z$); ladders in $\mathbb{B}$ (they are not Hermitian) |
| $\vec\Upsilon_x=\tfrac12(i\vec e_x-\vec e_y)=\frac{k_m\,\tilde{S}_{+}}{m\,c}$, $\vec\Upsilon_y=\frac{k_m\,\tilde{S}_{-}}{m\,c}$ | Single fermionic mode ladder |
| $\tilde\Pi_-=\vec\Upsilon_y\vec\Upsilon_x=\tfrac12(e_t-i\vec e_z)$ | Single-mode number operator, with $\tilde\Pi_-^2=\tilde\Pi_-$ |
| $(-1)^F=i\vec e_z=e_t-2\tilde\Pi_-=\frac{2\,k_m\,\tilde{S}_{z}}{m\,c}$ | Fermion parity; Hermitian involution in $\mathbb{B}_{\Psi}$ |
| $\{\vec\Upsilon_x,\vec\Upsilon_y\}=e_t$, $[\vec\Upsilon_x,\vec\Upsilon_y]=i\vec e_z$ | Fermionic mode relation; failure of the bosonic relation |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$, $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | Corpus gradient, its quaternion conjugate and the d'Alembertian (*Operator and Calculus Conventions*, §*The Gradient*) |
| $\mathbb{D}\tilde X=-\partial\tilde X/\partial r'_t\,\vec e_x-\sum_k\vec e_k\,\partial\tilde X/\partial R_k\,\vec e_y$ | Pair operator on one element (coordinate form); the time term is a single right multiplication, the spatial terms two-sided; $\mathbb{D}^2=\Box$ |
| $\mathbb{D}_p\tilde X=iE_{\vec p}\tilde X\vec e_x-i\sum_k p_k\vec e_k\tilde X\vec e_y$ | Symbol of the same operator on a plane wave; $\mathbb{D}_p^2=p_0^2-\lvert\vec p\rvert^2=m^2$ |
| $\nabla_k=\partial/\partial\Delta_k$ | Gradient with respect to the spatial separation |
| $\tilde{Ξ}_{\mathrm{fop}}$, $\bar{\tilde{Ξ}}_{\mathrm{sp},\mathrm{fop}}=\tilde{Ξ}_{\mathrm{fop}}^{\dagger}i\vec e_x$ | Quantized element-valued Dirac field and its Dirac adjoint, $\bar{\tilde{Ξ}}_{\mathrm{sp}}X=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*iX\vec e_x)$ |
| $a_{\mathrm{fop},r}(\vec p),b_{\mathrm{fop},r}^{\dagger}(\vec p)$ | Annihilation and antiparticle creation operators |
| $\tilde{Ξ}_{\mathrm{sp},\pm}^{(r)}(\vec p)$ | Positive- and negative-frequency amplitudes, elements of $\mathbb{B}$ (from the parents) |
| $\sum_r\tilde{Ξ}_{\mathrm{sp},\pm}^{(r)}\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp},\pm}^{(r)*}\tilde{Ξ})=(\mathbb{D}_p\pm m)(\tilde{Ξ}\,i\vec e_x)$ | Spin sums as completeness identities, for every $\tilde{Ξ}\in\mathbb{B}$ |
| $\theta=\vec p\cdot\vec\Delta$, $\vec\Delta=X-Y$, $X=r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ | Phase and spatial separation in the equal-time brackets |
| $\{\tilde{Ξ}_{\mathrm{fop},\mu},\tilde{Ξ}_{\mathrm{fop},\nu}^{\dagger}\}=\delta_{\mu\nu}\delta^{(3)}(\vec\Delta)$ | Local equal-time anticommutator |
| $[\tilde{Ξ}_{\mathrm{fop}},\tilde{Ξ}_{\mathrm{fop}}^{\dagger}]\,\tilde{Ξ}=i\,mF\,\tilde{Ξ}\vec e_x-i\sum_k\vec e_k\,\tilde{Ξ}\vec e_z\,\nabla_kF$ | Nonlocal equal-time commutator acting on a test element $\tilde{Ξ}$ |
| $F(\vec\Delta)=\frac{m}{2\pi^2|\vec\Delta|}K_1(m|\vec\Delta|)$ | Surviving commutator kernel ($m>0$) |
| $\Delta_{\mathrm{A}}(x-y)$, $G_{\mathrm{S}}(x-y)$ | Antisymmetric (Pauli–Jordan-type) and symmetric two-point kernels |
| $H=\sum_r\int\frac{d^3p}{(2\pi)^3}E_{\vec p}(a_{\mathrm{fop},r}^{\dagger}a_{\mathrm{fop},r}+b_{\mathrm{fop},r}^{\dagger}b_{\mathrm{fop},r})+E_0$ | Normal-ordered Hamiltonian (Fermi choice) |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_1,\tilde{Q}_1\rangle_{*}=\sum_\mu\lvert Q_{1\mu}\rvert^{2}$ |

## Further Reading

- W. Pauli, "The Connection Between Spin and Statistics," *Physical Review* **58** (1940) 716–722, for the original theorem and the positivity argument.
- M. Fierz, "Über die relativistische Theorie kräftefreier Teilchen mit beliebigem Spin," *Helvetica Physica Acta* **12** (1939) 3–37, for the antecedent representation-theoretic analysis.
- G. Lüders and B. Zumino, "Connection between Spin and Statistics," *Physical Review* **110** (1958) 1450–1453, for the general proof in the axiomatic setting.
- R. F. Streater and A. S. Wightman, *PCT, Spin and Statistics, and All That* (Benjamin, 1964), for the Wightman-axiomatic treatment and the locality–positivity hypotheses.
- R. Haag, *Local Quantum Physics* (2nd ed., Springer, 1996), for the algebraic formulation and the role of the grading.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), and M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the standard equal-time and covariant two-point functions used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Fields* (McGraw–Hill, 1965), for the spin sums, the Pauli–Jordan function and the microcausality computation.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the origin of the spin group and its double cover.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor realization of rotations and its two-valuedness.
- Companion articles: [Canonical Quantization of the Biquaternion Dirac Field](canonical-quantization-of-the-biquaternion-dirac-field.html); [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html); [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html); [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html); [The Spinor Representation of the Lorentz Group in Biquaternionic Form](the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html); [The KMS Condition and the Biquaternion Framework](the-kms-condition-and-the-biquaternion-framework.html); [Canonical Quantization of the Biquaternion Maxwell Field](canonical-quantization-of-the-biquaternion-maxwell-field.html); [The Klein–Gordon Equation in Biquaternionic Form](the-klein-gordon-equation-in-biquaternionic-form.html).

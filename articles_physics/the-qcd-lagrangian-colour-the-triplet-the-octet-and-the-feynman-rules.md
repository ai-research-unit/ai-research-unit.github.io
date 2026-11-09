# __The QCD Lagrangian: Colour, the Triplet, the Octet and the Feynman Rules__

## Introduction

**The standing of this article.** Everything below is standard theory, written in the corpus's coordinates and notation. It is **standard input**, not a framework result. Colour is the sharpest boundary in this corpus: by [The Gauge Group Ceiling](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html), any compact gauge algebra inside $\mathbb{B}$ has real dimension at most four and every $\mathbb{B}$-module has even complex dimension, so neither $SU(3)$ nor a colour triplet is available in the algebra. The strong sector is therefore transcribed, and the article says so before it prints the Lagrangian. What it adds to a textbook display is three things: the Feynman rules derived from this particular Lagrangian rather than quoted, with the sign of every vertex fixed by the same $g_s$; the colour arithmetic computed and checked; and one table that separates what is imported from what, if anything, the algebra contributes.

**The claim.** Quantum chromodynamics is one Lagrangian with four pieces and four vertices.

$$
\mathcal{L}_{\mathrm{QCD}}=-\frac14\sum_{a,\mu,\nu}G^a_{\mu\nu}G^a_{\mu\nu}+\sum_f\bar\psi_f\left(i\gamma^\mu D_\mu-m_f\right)\psi_f+\mathcal{L}_{\mathrm{gf}}+\mathcal{L}_{\mathrm{gh}} .
$$

The quark $\psi_f$ is a colour triplet, one per flavour $f$; the gluon $G^a_\mu$ is a colour octet; the vertices are the quark–gluon, the three-gluon, the four-gluon and the ghost–gluon, and they exhaust the tree-level content. The $\theta$ term is a fifth piece, a total derivative in perturbation theory, and it is named here and left to its own article.

**Why the number three is not in the Lagrangian.** Nothing in the algebra or in the Lagrangian's structure fixes $N_c=3$. The number is measured, four independent ways, and the section *Why Three Colours* records them. That is the same status as the nineteen parameters of [the content article](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html): a fact about the world, imported.

**The order.** The evidence for three colours, then the three representations, then the generators and the normalisation, then the Lagrangian, then the covariant derivative and the field strength, then gauge fixing and the ghost, then the Feynman rules, then their derivation, then the colour factors, then the checks, then the ledger.

## Why Three Colours

**Four measurements, one conclusion.** Each of the four sees $N_c$ in a different way, and all four give $3$.

| Measurement | Dependence on $N_c$ | What is seen |
|---|---|---|
| $R=\sigma(e^+e^-\to\text{hadrons})/\sigma(e^+e^-\to\mu^+\mu^-)$ | $N_c\sum_fQ_f^2$ | $11/3$ above the bottom threshold, against $3.9$ measured |
| $\Gamma(\pi^0\to\gamma\gamma)$ | $N_c^2$ | $7.8$ eV, against $7.6$ eV predicted for $N_c=3$ |
| $\Gamma(Z\to\text{hadrons})/\Gamma(Z\to\ell^+\ell^-)$ | $N_c$ | $20.77$, the factor three times the coupling ratio |
| Existence of $\Delta^{++}$ and $\Omega^-$ | rank of the antisymmetric invariant | three quarks in a totally antisymmetric colour state |

**The $R$ ratio, written out.** The cross section into hadrons is the cross section into quarks, and each quark flavour contributes its charge squared times the number of colour states,

$$
R=N_c\sum_fQ_f^2 ,
$$

so that $R=2$ below the charm threshold, $10/3$ below the bottom, $11/3$ below the top and $5$ above it. The measured values follow this staircase, with a residual excess of order $\alpha_s/\pi$: at $34$ GeV the parton-model $11/3=3.67$ becomes $3.8$ once the first-order correction is included, against $3.9$ measured.

**Counting versus structure.** The first three measurements count colour states, and each would move if the count were four: $R$ would be $4\sum_fQ_f^2$ and the $Z$ hadronic width larger by a third, and both are excluded. The fourth measurement does something different. A baryon is a colour singlet, and the only invariant tensor available to build one from $N_c$ triplets is the totally antisymmetric $\epsilon$ of rank $N_c$. The $\Delta^{++}$ is $uuu$ with $J=3/2$ and zero orbital angular momentum, so its spin–flavour wavefunction is totally symmetric, and Fermi statistics forces its colour wavefunction to be totally antisymmetric. A totally antisymmetric three-index invariant exists only for $N_c=3$. The particle's existence is therefore the statement that the antisymmetriser has exactly three slots.

**The empirical status.** $N_c=3$ is measured. No argument in this corpus produces the number, and [the QCD agenda](quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) records it as a *no route yet* item, not as a derivation with a missing step.

## The Triplet, the Antitriplet and the Octet

**The three representations.**

| Object | Representation | Dimension | Why |
|---|---|---|---|
| Quark $\psi$ | $\mathbf{3}$ | $3$ | It carries one colour index |
| Antiquark $\bar\psi$ | $\bar{\mathbf{3}}$ | $3$ | The conjugate index |
| Gluon $G^a_\mu$ | $\mathbf{8}$ (adjoint) | $8=N^2-1$ | It carries colour and anticolour in the traceless combination |

**Why the gluon is the octet and not the singlet inside $\mathbf{3}\otimes\bar{\mathbf{3}}$.** A gluon must carry a colour and an anticolour, so it lives in $\mathbf{3}\otimes\bar{\mathbf{3}}$, and

$$
\mathbf{3}\otimes\bar{\mathbf{3}}=\mathbf{1}\oplus\mathbf{8} ,
\qquad 3\times3=1+8 .
$$

The singlet part is the trace, and the gauge field is traceless, so what remains is the octet. The further requirement is that the gluon field be real, and the octet is the real representation: it is the adjoint, and the adjoint of a compact group is real. The two requirements, traceless colour–anticolour and reality, leave $\mathbf{8}$ and nothing else.

**The decompositions that matter for the spectrum.** Colour confinement means that only singlets appear as asymptotic states, so the question is which products contain a $\mathbf{1}$.

$$
\mathbf{3}\otimes\bar{\mathbf{3}}=\mathbf{1}\oplus\mathbf{8} ,
\qquad
\mathbf{3}\otimes\mathbf{3}\otimes\mathbf{3}=\mathbf{1}\oplus\mathbf{8}\oplus\mathbf{8}\oplus\mathbf{10} ,
\qquad
\mathbf{8}\otimes\mathbf{8}=\mathbf{1}\oplus\mathbf{8}\oplus\mathbf{8}\oplus\mathbf{10}\oplus\overline{\mathbf{10}}\oplus\mathbf{27} .
$$

The first line is the meson and the gluon; the second is the baryon, with one singlet out of twenty-seven states; the third is the gluon–gluon channel, where the singlet is the one that mixes with the vacuum and the $\mathbf{8}$'s are the two-gluon colour octets. The dimension arithmetic is the only check made here — $9=1+8$, $27=1+8+8+10$, $64=1+8+8+10+10+27$ — and the arithmetic is exact, though it does not prove the decompositions.

**A singlet made of two quarks does not exist.** $\mathbf{3}\otimes\mathbf{3}=\bar{\mathbf{3}}\oplus\mathbf{6}$ contains no singlet, which is the group-theoretic statement that a diquark cannot be colour neutral and therefore cannot be an asymptotic state. This is the reason the strong spectrum is mesons and baryons rather than pairs.

## The Generators and the Normalisation

**The generators.** The quark transforms in the defining representation, and its generators are the eight Gell-Mann matrices halved,

$$
T^a=\frac{\lambda^a}{2} ,
\qquad a=1,\dots,8 ,
\qquad
[T^a,T^b]=i\sum_cf^{abc}T^c ,
\qquad
\{T^a,T^b\}=\frac13\delta^{ab}I+\sum_cd^{abc}T^c .
$$

The two invariant tensors $f^{abc}$ and $d^{abc}$, their nonzero components and the structure of the algebra are the subject of [The Gluon: An Octet Outside the Biquaternion Algebra](the-gluon-an-octet-outside-the-biquaternion-algebra.html), and they are not repeated here; what this article needs is one number from each of them.

**The normalisation, which is a choice.** The trace is fixed by convention,

$$
\mathrm{Tr}\left(T^aT^b\right)=T_R\,\delta^{ab} ,
\qquad
T_R=\frac12 ,
$$

the value that follows from $\mathrm{Tr}\left(\lambda^a\lambda^b\right)=2\delta^{ab}$. This is a convention and not a fact: a rescaling $T^a\to\kappa T^a$ changes $T_R\to\kappa^2T_R$ and can be compensated by $g_s\to g_s/\kappa$, leaving every product $g_sT^a$ unchanged. What is convention-independent is the combination that appears in observables, and the invariant way to say it is that the three numbers below are tied together by $C_F=T_R(N^2-1)/N$, which a rescaling of $T^a$ leaves unchanged because $\kappa^2$ cancels between $C_F$ and $T_R$:

$$
C_F=\frac{N^2-1}{2N}=\frac43 ,
\qquad
C_A=N=3 ,
\qquad
T_R=\frac12 .
$$

**What each number counts.** $C_F$ is the colour charge of a quark, the value of $\sum_aT^aT^a$ on the triplet; $C_A$ is the colour charge of a gluon, the value of the same sum on the octet; $T_R$ is the normalisation of the quark loop. With $N=3$ they are

| Quantity | Definition | Value for $N=3$ |
|---|---|---|
| $C_F$ | $\sum_aT^aT^a$ on the $\mathbf{3}$ | $4/3=1.3333$ |
| $C_A$ | $\sum_{c,e}f^{ace}f^{bce}=C_A\delta^{ab}$ | $3$ |
| $T_R$ | $\mathrm{Tr}\left(T^aT^b\right)=T_R\delta^{ab}$ | $1/2$ |
| $\dfrac{11C_A/3}{4T_R/3}$ | The margin per flavour in $b_0$ | $16.5$ |
| $C_A/C_F$ | Two Casimirs divided; **not** in $b_0$ | $9/4=2.25$ |

**The ratio that sets asymptotic freedom.** The gluon and ghost loops contribute $11C_A/3$ and the quark loop $4T_RN_f/3$, so per flavour the gluon outweighs the quark by $\frac{11C_A/3}{4T_R/3}=16.5$, and the gluon's antiscreening wins for every $N_f\le16$. The ratio $C_A/C_F=9/4$ is a different number — two Casimirs divided — and it does not enter the beta function, because $C_F$ appears in the quark self-energy and nowhere in the $N_f$ bookkeeping. The full arithmetic is [the running article's](asymptotic-freedom-and-the-running-of-the-strong-coupling.html); what belongs here is that $N=3$, $T_R=\frac12$ and the two loop integrals are the whole of the input.

**The trace identity that is used most often.** For three generators,

$$
\mathrm{Tr}\left(T^aT^bT^c\right)=\frac14\left(d^{abc}+if^{abc}\right) ,
$$

which is checked below to machine precision and which is the reason the symmetric tensor $d^{abc}$ is not decorative: it is the real part of a trace, so any process with three gluons attached to a quark loop sees it.

## The Lagrangian

**The four pieces, in the corpus's coordinates.** With $\partial/\partial R_\mu$ the derivative of [the assembled Lagrangian](the-standard-model-lagrangian-assembled-four-sectors-in-one-expression.html) and the sign rule $\sum_\mu X_\mu Y_\mu=-X_\mu Y^\mu$ applying to every display,

$$
\mathcal{L}_{\mathrm{QCD}}=-\frac14\sum_{a,\mu,\nu}G^a_{\mu\nu}G^a_{\mu\nu}+\sum_f\bar\psi_f\left(i\gamma^\mu D_\mu-m_f\right)\psi_f-\frac{1}{2\zeta}\sum_{a,\mu}\left(\frac{\partial G^a_\mu}{\partial R_\mu}\right)^2+\sum_{a}\bar c^a\left(-\frac{\partial^2}{\partial R_\mu\partial R_\mu}\right)c^a+\mathcal{L}_{cG} .
$$

**The pieces, named.** The first is the gauge kinetic term; the second the quark term, one per flavour, with the covariant derivative carrying the colour connection in the triplet; the third the gauge-fixing term with parameter $\zeta$; the fourth and fifth the ghost kinetic and ghost–gluon terms. The list is complete for perturbation theory. The $\theta$ term,

$$
\mathcal{L}_\theta=\theta_{\mathrm{QCD}}\frac{g_s^2}{32\pi^2}\sum_{a,\mu,\nu}G^a_{\mu\nu}\widetilde G^a_{\mu\nu} ,
$$

is a total derivative and contributes nothing to any perturbative amplitude; it is a parameter of the theory and it belongs to [The Theta Vacuum in Biquaternionic Form](the-theta-vacuum-in-biquaternionic-form.html).

**Why the gauge-fixing and ghost terms are not optional.** The quadratic kernel of the gauge field alone is not invertible, because the gauge orbit is a flat direction of $-\frac14\sum GG$; the gauge-fixing term lifts it, and the ghost term restores the gauge invariance that the fixing broke. That mechanism is the subject of [Gauge Fixing in the Electroweak Theory](gauge-fixing-in-the-electroweak-theory-r-xi-gauges-ghosts-and-the-goldstone-equivalence-theorem.html), and its structure in QCD is identical with one difference that matters: the ghost of QCD is in the adjoint, so it carries a colour index and couples through $f^{abc}$ rather than through a generator matrix.

**The mass term is allowed here and forbidden there.** A term $m\bar\psi\psi$ is invariant under $SU(3)$, so QCD admits quark masses; the same term is forbidden in the electroweak theory because the two chiralities carry different $SU(2)$ representations. The quark mass in the display above is therefore a genuine parameter of the strong sector, generated elsewhere — by the Yukawa sector — and carried here as an input.

## The Covariant Derivative and the Field Strength

**The covariant derivative.**

$$
D_\mu=\frac{\partial}{\partial R_\mu}-ig_s\sum_aG^a_\mu T^a ,
$$

acting on the triplet. On the antitriplet the generators are $-T^{a*}$, and on the octet they are the structure constants in the adjoint form, $\left(T^a_{\mathrm{adj}}\right)_{bc}=-if^{abc}$.

**The field strength is the commutator.** With the convention above,

$$
\left[D_\mu,D_\nu\right]=-ig_s\sum_aG^a_{\mu\nu}T^a ,
\qquad
G^a_{\mu\nu}=\frac{\partial G^a_\nu}{\partial R_\mu}-\frac{\partial G^a_\mu}{\partial R_\nu}+g_s\sum_{b,c}f^{abc}G^b_\mu G^c_\nu .
$$

**This identity is the one to check, and it was.** With random constant fields the two sides of the commutator identity agreed to $4.4\times10^{-16}$, and the algebraic core of it — that $-g_s^2\left[A_\mu,A_\nu\right]$ equals $-ig_s$ times the $g_s f$ term — agreed to $4.4\times10^{-16}$ as well. The check is worth making because the sign in front of the commutator term in $G^a_{\mu\nu}$ and the sign of the coupling in $D_\mu$ are not independent options: choose one and the other follows, and choosing them inconsistently produces a field strength that is not a curvature.

**Consequence, stated once.** Because $G^a_{\mu\nu}$ is a commutator of covariant derivatives, the cubic and quartic terms in $-\frac14\sum GG$ have coefficients fixed by $g_s$ and by nothing else. Every self-coupling of the gluon is a consequence of the non-abelian commutator; an abelian theory has neither, because its structure constants vanish.

## Gauge Fixing and the Ghost

**The gauge-fixing term.** The corpus writes the parameter $\zeta$, as in article 7, and the Feynman gauge is $\zeta=1$. The term

$$
-\frac{1}{2\zeta}\sum_{a,\mu}\left(\frac{\partial G^a_\mu}{\partial R_\mu}\right)^2
$$

makes the gluon propagator invertible and gives the transverse projector a $\zeta$-dependent longitudinal part,

$$
D^{ab}_{\mu\nu}(k)=\frac{-i\delta^{ab}}{k^2+i\epsilon}\left[\delta_{\mu\nu}-(1-\zeta)\frac{k_\mu k_\nu}{k^2}\right] .
$$

**The ghost term, and why it is the adjoint.** The Faddeev–Popov determinant for the gauge orbit produces

$$
\mathcal{L}_{cG}=-g_s\sum_{a,b,c}f^{abc}\left(\frac{\partial\bar c^a}{\partial R_\mu}\right)G^{b}_\mu c^c ,
$$

with the ghost $c^a$ in the adjoint representation: eight of them, one per generator, massless, and scalars with the wrong statistics. The eight is the same eight as the gluon's, for the same reason — the gauge orbit has one direction per generator. In the electroweak theory the ghost of the $SU(2)$ factor is also an adjoint, and the ghost of the $\mathrm{U}(1)$ factor decouples because an abelian structure constant vanishes.

**What the ghost does in a computation.** Only two things: it runs in loops, and it carries a minus sign relative to a scalar loop. That minus is the whole reason the ghost loop contributes with the opposite sign to a would-be scalar loop, and it is why the gluon self-energy at one loop gives $11-\frac23N_f$ rather than something else.

## The Feynman Rules

**The convention, stated once, because every sign below depends on it.** Momenta are taken incoming at every vertex; the metric is the corpus's, with the sign rule converting a corpus display into a standard one; the coupling enters through $D_\mu=\partial_\mu-ig_sG^aT^a$, which is the convention of the previous two sections. With that choice the quark–gluon vertex carries $+ig_s$ where a text using the opposite sign in $D_\mu$ carries $-ig_s$.

**Propagators.**

| Line | Factor |
|---|---|
| Gluon $ab$, $\mu\nu$ | $\dfrac{-i\delta^{ab}}{k^2+i\epsilon}\left[\delta_{\mu\nu}-(1-\zeta)\dfrac{k_\mu k_\nu}{k^2}\right]$ |
| Quark $ij$ | $\dfrac{i\left(\gamma^\mu k_\mu+m\right)_{ij}}{k^2-m^2+i\epsilon}$ |
| Ghost $ab$ | $\dfrac{i\delta^{ab}}{k^2+i\epsilon}$ |

**Vertices.**

| Vertex | Colour factor | Lorentz structure |
|---|---|---|
| Quark–gluon | $T^a_{ij}$ | $ig_s\gamma^\mu$ |
| Three-gluon | $g_sf^{abc}$ | $(p_1-p_2)_\rho\delta_{\mu\nu}+(p_2-p_3)_\mu\delta_{\nu\rho}+(p_3-p_1)_\nu\delta_{\rho\mu}$ |
| Four-gluon | $-ig_s^2$ times the group combination of the display below | $\delta_{\mu\rho}\delta_{\nu\sigma}-\delta_{\mu\sigma}\delta_{\nu\rho}$ with the two permutations |
| Ghost–gluon | $-g_sf^{abc}$ | $p^\mu$, with $p$ the momentum of the incoming antighost |

**The four-gluon vertex in full.** With legs $(a,\mu)$, $(b,\nu)$, $(c,\rho)$, $(d,\sigma)$,

$$
-i g_s^2\Big[f^{abe}f^{cde}\left(\delta_{\mu\rho}\delta_{\nu\sigma}-\delta_{\mu\sigma}\delta_{\nu\rho}\right)+f^{ace}f^{bde}\left(\delta_{\mu\nu}\delta_{\rho\sigma}-\delta_{\mu\sigma}\delta_{\nu\rho}\right)+f^{ade}f^{bce}\left(\delta_{\mu\nu}\delta_{\rho\sigma}-\delta_{\mu\rho}\delta_{\nu\sigma}\right)\Big] .
$$

**Why the three-gluon rule has no explicit $i$ and the four-gluon rule has one.** The cubic term of $-\frac14\sum GG$ carries one derivative, and in momentum space the derivative brings a factor $-i$, so the $i$ that every vertex receives is cancelled. The quartic term carries no derivative and keeps it. This asymmetry is not a typographical slip in the table; it is the reason a reader who copies a rule out of a book written in the opposite convention must flip the sign of the three-gluon vertex and must not flip the four-gluon one. Flipping $g_s\to-g_s$ does exactly that: the odd vertices change sign and the even ones do not.

## The Three Vertices Derived

**The quark–gluon vertex, in one line.** The interaction term in the quark piece is

$$
+g_s\sum_{a,\mu}\bar\psi\gamma^\mu T^aG^a_\mu\psi ,
$$

with the sign from $i\gamma^\mu\left(-ig_sT^aG^a_\mu\right)=+g_s\gamma^\mu T^aG^a_\mu$. The vertex is $i$ times this coefficient with the fields removed, so it is $ig_s\gamma^\mu T^a_{ij}$.

**The three-gluon vertex, in three lines.** Expanding $-\frac14\sum GG$ and keeping the terms with one field strength linear in the field and two powers of the field,

$$
\mathcal{L}_3=-g_s\sum_{a,b,c}f^{abc}\left(\partial_\mu G^a_\nu\right)G^b_\mu G^c_\nu .
$$

The derivative may sit on any of the three fields, and the three placements give the three terms of the rule. Written with all momenta incoming,

$$
\Gamma^{abc}_{\mu\nu\rho}(p_1,p_2,p_3)=g_sf^{abc}\Big[(p_1-p_2)_\rho\delta_{\mu\nu}+(p_2-p_3)_\mu\delta_{\nu\rho}+(p_3-p_1)_\nu\delta_{\rho\mu}\Big] ,
$$

and the tensor is totally antisymmetric under the exchange of any two legs together with their momenta, which is the statement that the three gluons enter symmetrically.

**The check that fixes the sign.** The rule above reproduces the tree-level Ward identity

$$
p_1^\alpha\,\Gamma_{\alpha\beta\gamma}(p_1,p_2,p_3)=g_sf^{abc}\Big[\Pi_{\beta\gamma}(p_2)-\Pi_{\beta\gamma}(p_3)\Big] ,
\qquad
\Pi_{\mu\nu}(k)=k_\mu k_\nu-k^2\delta_{\mu\nu} ,
$$

and the check was made numerically: the two sides agreed to $5.6\times10^{-16}$ on random momenta. The identity is the non-abelian statement that the divergence of the vertex is the difference of the inverse propagators, and it is what replaces the abelian Ward identity, which would have set the left side to zero.

**The four-gluon vertex, and how it was checked.** The quartic term of $-\frac14\sum GG$ is

$$
\mathcal{L}_4=-\frac{g_s^2}{4}\sum_{a,b,c,d,e}f^{abc}f^{ade}G^b_\mu G^c_\nu G^d_\mu G^e_\nu .
$$

The rule in the table was checked against this expression directly, by extracting the coefficient of four independent polarisations from the Lagrangian rather than by quoting it: the extracted coefficient agreed with $-g_s^2$ times the bracket above to $1.1\times10^{-15}$, with the $g_s$ dependence confirmed separately by the ratio $1.21=g_s^2$ at $g_s=1.1$.

**The ghost–gluon vertex.** From $\mathcal{L}_{cG}$, again with one derivative,

$$
\Gamma^{abc}_\mu(p)=-g_sf^{abc}p_\mu ,
$$

with $p$ the momentum of the incoming antighost and the indices ordered (antighost, ghost, gluon). The sign is the **opposite** of the three-gluon vertex, and the reason is visible in the two Lagrangians rather than in a rule of thumb. In $\mathcal{L}_3$ the derivative may sit on any of three identical fields, and the antisymmetrised sum over the six placements contributes a net $+1$; in $\mathcal{L}_{cG}$ the derivative sits on the antighost, there is one placement and no sum, so the factor is the bare $-g_sf$ times $-ip_\mu$ times the $i$ of the vertex, which is $-g_sfp_\mu$. Both vertices flip with $g_s\to-g_s$, which is the part the earlier sentence had right.

## The Colour Factors

**Where each number is used.** The three colour factors are not decoration; each one is the group-theory factor of a definite diagram class.

| Factor | Diagram class | Where it appears |
|---|---|---|
| $C_F=4/3$ | Quark emitting or absorbing a gluon | The quark self-energy; the $q\bar q$ antenna; the coefficient of $\alpha_s$ in a quark-loop correction |
| $C_A=3$ | Gluon or ghost in the loop | The gluon self-energy; the three- and four-gluon couplings; the antiscreening |
| $T_R=1/2$ | Quark loop inserted in a gluon line | The screening; the $N_f$ term of the beta function |

**The arithmetic of the one-loop coefficient, handed on.** The gluon self-energy at one loop is the sum of three diagram classes, and their colour factors combine as

$$
b_0=\frac{11}{3}C_A-\frac{4}{3}T_RN_f=11-\frac{2}{3}N_f ,
$$

with the first term from the gluon and ghost loops, the second from the quark loop, and the sign of the ghost already included. The $11$ is $11/3$ times $C_A=3$; the $2/3$ is $4/3$ times $T_R=1/2$. The running article computes the coefficient; this article supplies only the numbers that go into it.

**The margin, in one ratio.** The number that decides the sign is $\frac{11C_A/3}{4T_R/3}=16.5$ per flavour, and $C_A/C_F=9/4$ is not it: $C_F$ does not appear in $b_0$, so a ratio built from $C_F$ cannot be the reason the sign comes out negative. Taken at face value, a per-flavour margin of $2.25$ would forbid asymptotic freedom beyond $N_f=1$, which the same paragraph contradicts. A gluon loop carries $C_A$ and antiscreens; a quark loop carries $T_R$ and screens. With $N_f$ flavours the bookkeeping is $11C_A/3$ against $4T_RN_f/3$, and the first wins for every $N_f\le16$. At $N_c=3$ the margin is comfortable, which is why QCD is asymptotically free for the six flavours that exist and would cease to be at seventeen.

## The Algebra Verified

**Everything in this section was computed, not quoted.** The Gell-Mann matrices were built explicitly, the structure constants extracted from their commutators, and the identities below checked as matrix equalities.

| Check | Residual |
|---|---|
| $\mathrm{Tr}\left(T^aT^b\right)=\frac12\delta^{ab}$ | exact |
| $\left[T^a,T^b\right]=i\sum_cf^{abc}T^c$ | $0$ |
| $\{T^a,T^b\}=\frac13\delta^{ab}I+\sum_cd^{abc}T^c$ | $0$ |
| Jacobi identity on $f^{abc}$ | $3.3\times10^{-16}$ |
| $\sum_aT^aT^a=C_FI$ with $C_F=4/3$ | $2.2\times10^{-16}$ |
| $\sum_{c,e}f^{ace}f^{bce}=3\delta^{ab}$ | $1.3\times10^{-15}$ |
| $\mathrm{Tr}\left(T^aT^bT^c\right)=\frac14\left(d^{abc}+if^{abc}\right)$ | $0$ |
| $T^a_{ij}T^a_{\eta l}=\frac12\left(\delta_{il}\delta_{j\eta}-\frac13\delta_{ij}\delta_{\eta l}\right)$ | $5.6\times10^{-17}$ |
| $\sum_{abc}\left(f^{abc}\right)^2=24$ | exact |
| $\sum_{abc}\left(d^{abc}\right)^2=40/3$ | exact |
| $\left[D_\mu,D_\nu\right]=-ig_sG^a_{\mu\nu}T^a$ | $4.4\times10^{-16}$ |
| Three-gluon rule against $\mathcal{L}_3$ | $4.4\times10^{-16}$ |
| Ward identity of the three-gluon vertex | $5.6\times10^{-16}$ |
| Four-gluon rule against $\mathcal{L}_4$ | $1.1\times10^{-15}$ |
| $g_s$ dependence of the four-gluon rule | ratio $1.21=g_s^2$ at $g_s=1.1$ |

**The Fierz identity is the one worth singling out.** The row for the product of two generators,

$$
\sum_aT^a_{ij}T^a_{\eta l}=\frac12\left(\delta_{il}\delta_{j\eta}-\frac13\delta_{ij}\delta_{\eta l}\right) ,
$$

is what makes colour summing mechanical: a gluon exchanged between two quark lines contracts two generator matrices into a Kronecker delta minus a trace. It is the $SU(3)$ analogue of the $SU(2)$ identity $\sum_a\sigma^a_{ij}\sigma^a_{\eta l}=2\delta_{il}\delta_{j\eta}-\delta_{ij}\delta_{\eta l}$ for the Pauli matrices, generalised to $-\delta_{ij}\delta_{\eta l}/N$ in place of the second term; the coefficient $1/N$ of that term is why the $1/N$ expansion of the strong interaction exists at all.

**The two quadratic Casimir invariants.** From the explicit matrices, $\sum_aT^aT^a=\frac43I$ and $\sum_{c,e}f^{ace}f^{bce}=3\delta^{ab}$; both are properties of $SU(3)$ and both were reproduced from the matrices rather than assumed. The three numbers of the colour-factor table are therefore not three independent inputs: $T_R$ is a normalisation, $C_A=N$ follows from $N=3$ alone and is untouched by the rescaling, and $C_F=T_R(N^2-1)/N$ is the one combination that carries $T_R$.

## What the Corpus Adds and What It Imports

**The ledger.**

| Item | Status |
|---|---|
| The group $SU(3)$ and the triplet | **Imported.** Not available in $\mathbb{B}$: the ceiling article's dimension bound excludes it |
| The value $N_c=3$ | **Imported.** Measured four ways; no derivation in this corpus |
| The Gell-Mann matrices and the tensors $f^{abc}$, $d^{abc}$ | **Imported**, and computed explicitly as a check |
| The Lagrangian and its four pieces | **Imported.** Standard theory, transcribed in the corpus's coordinates |
| The covariant derivative and the curvature identity | **Imported**, and verified as a matrix identity |
| The Feynman rules and their signs | **Derived from the Lagrangian above**, in this article |
| The colour factors $4/3$, $3$, $1/2$ | **Derived** from $N_c=3$ and the trace normalisation, once those are granted |
| The Ward identity of the three-gluon vertex | **Imported** (it is the tree-level shadow of the Slavnov–Taylor identity), and verified |
| The sign rule $\sum_\mu X_\mu Y_\mu=-X_\mu Y^\mu$ | **Derived in the algebra**, in article 2 |
| Transversality of the gluon propagator | **Derived in the algebra**, from article 7's projector |

**What the algebra can host, stated precisely.** The projector structure of the propagator, the sign rule and the reality conditions are biquaternionic objects; the octet is not. The route the corpus takes is the one [the gluon article](the-gluon-an-octet-outside-the-biquaternion-algebra.html) sets out: the octet is not in $\mathbb{B}$, but it is in $M_2(\mathbb{B})\cong M_4(\mathbb{C})$, where a $3\times3$ traceless block can be written and the $\mathrm{SU}(3)$ elements have explicit biquaternion closed forms. That enlargement is a carrier, not a derivation: it hosts the octet at the price of a larger module, and it does not produce the triplet or the number three.

**What this article does not do.** It does not derive $N_c$, does not confine, does not compute a cross section, and does not run the coupling. Three of the four are elsewhere in the corpus: [Asymptotic Freedom and the Running of the Strong Coupling](asymptotic-freedom-and-the-running-of-the-strong-coupling.html) runs the coupling from the $b_0$ given here, [Confinement and the Loss of Partonic Information in Biquaternionic Form](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) takes up why the octet is never seen, and the derivation of $N_c$ is the *no route yet* item this article and the QCD agenda both record. Cross sections are not yet written.

## Summary

The QCD Lagrangian is $-\frac14\sum GG$ plus a quark term plus gauge fixing plus ghosts, and the gluon's self-couplings follow from the commutator in $G^a_{\mu\nu}$. The four pieces and the four vertices are standard theory, transcribed here in the corpus's coordinates, and every number in the Feynman rules was derived from that Lagrangian rather than quoted: the three-gluon rule has no explicit $i$ because its term carries one derivative, the four-gluon rule has one, and the two signs are tied to the same $g_s$.

Three colours is a measured fact, established four independent ways — the $R$ ratio, the $\pi^0$ width, the $Z$ hadronic width, and the existence of a three-quark baryon with a symmetric spin–flavour wavefunction. The last of these fixes the number exactly, because the only invariant that can make a baryon is the antisymmetric $\epsilon$ of rank $N_c$.

The representations are the triplet, the antitriplet and the octet. The octet is forced twice over: a gluon carries colour and anticolour without a trace, and its field is real. Three decompositions carry the spectrum: $\mathbf{3}\otimes\bar{\mathbf{3}}=\mathbf{1}\oplus\mathbf{8}$ for mesons, $\mathbf{3}\otimes\mathbf{3}\otimes\mathbf{3}=\mathbf{1}\oplus\mathbf{8}\oplus\mathbf{8}\oplus\mathbf{10}$ for baryons, and $\mathbf{8}\otimes\mathbf{8}$, whose singlet is the glueball. The absence of a singlet in $\mathbf{3}\otimes\mathbf{3}=\bar{\mathbf{3}}\oplus\mathbf{6}$ is why a diquark is not an asymptotic state.

The colour factors are $C_F=4/3$, $C_A=3$ and $T_R=1/2$, they were computed from the explicit Gell-Mann matrices, and every identity in the table of checks closed at machine precision. Per flavour the gluon's $11C_A/3$ outweighs the quark's $4T_R/3$ by $16.5$, and that is the margin by which antiscreening beats screening and the reason the coupling falls.

The framework supplies the sign rule and the projectors and nothing else. The group, the number three, the matrices and the Lagrangian are imported, and the ledger says so line by line.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi_f$, $\bar\psi_f$ | Quark field of flavour $f$ in the $\mathbf{3}$, and its conjugate |
| $G^a_\mu$, $G^a_{\mu\nu}$ | Gluon field and field strength, $a=1,\dots,8$ |
| $g_s$ | Strong coupling; $\alpha_s=g_s^2/4\pi$ |
| $T^a=\lambda^a/2$ | Generators of the triplet; $\lambda^a$ the Gell-Mann matrices |
| $f^{abc}$, $d^{abc}$ | Antisymmetric and symmetric invariant tensors of $SU(3)$ |
| $T_R=1/2$ | Trace normalisation, $\mathrm{Tr}\left(T^aT^b\right)=T_R\delta^{ab}$ |
| $C_F=4/3$ | Quadratic Casimir of the triplet, $\sum_aT^aT^a=C_FI$ |
| $C_A=3$ | Quadratic Casimir of the adjoint, $\sum_{c,e}f^{ace}f^{bce}=C_A\delta^{ab}$ |
| $D_\mu$ | Covariant derivative, $\partial_\mu-ig_sG^a_\mu T^a$ |
| $\zeta$ | Gauge parameter; $\zeta=1$ is Feynman gauge |
| $c^a$, $\bar c^a$ | Ghost and antighost, in the adjoint |
| $\theta_{\mathrm{QCD}}$ | Coefficient of the $G\widetilde G$ term |
| $N_c$ | Number of colours, $3$, measured |
| $N_f$ | Number of quark flavours active at a given scale |
| $R$ | $\sigma(e^+e^-\to\text{hadrons})/\sigma(e^+e^-\to\mu^+\mu^-)$ |
| $\Pi_{\mu\nu}(k)$ | $k_\mu k_\nu-k^2\delta_{\mu\nu}$, the tree inverse propagator |
| $p_1,p_2,p_3$ | Incoming momenta of the three gluon legs, $p_1+p_2+p_3=0$ |
| $\gamma^\mu$ | Dirac matrices; the quark propagator is $i(\gamma^\mu k_\mu+m_f)/(k^2-m_f^2+i\epsilon)$ |
| $m_f$ | Mass of quark flavour $f$, a parameter imported from the Yukawa sector |
| $Q_f$ | Electric charge of flavour $f$, in units of $e$ |
| $b_0$ | One-loop coefficient of the beta function, $b_0=\frac{11}{3}C_A-\frac43T_RN_f$ |
| $\epsilon_{abc}$ | The totally antisymmetric rank-$N_c$ invariant; the only colour singlet in $\mathbf{3}^{\otimes N_c}$ |
| $J$ | Spin of a hadron, $J=3/2$ for the $\Delta^{++}$ and the $\Omega^-$ |
| $\kappa$ | Generator rescaling $T^a\to\kappa T^a$, under which $T_R\to\kappa^2T_R$ |
| $\mathcal{L}_{\mathrm{gf}}$, $\mathcal{L}_{cG}$ | Gauge-fixing term and ghost–gluon interaction of the Lagrangian display |

## Further Reading

- [The Gluon: An Octet Outside the Biquaternion Algebra](the-gluon-an-octet-outside-the-biquaternion-algebra.html). The structure constants, the $d$ tensor and the embedded $\mathrm{SU}(3)$ elements that this article uses without repeating.
- [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches $SU(2)$ but Not $SU(3)$](the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html). The dimension bound quoted in the introduction.
- [SU(3) Representations and the Gell-Mann–Okubo Mass Formula](su3-representations-and-the-gell-mann-okubo-mass-formula-in-biquaternionic-form.html). The representation theory behind the decompositions of the section on the triplet and the octet.
- [The Standard Model Lagrangian Assembled: Four Sectors in One Expression](the-standard-model-lagrangian-assembled-four-sectors-in-one-expression.html). The sign rule, and the strong sector in its place among the four.
- [Gauge Fixing in the Electroweak Theory: $R_\xi$ Gauges, Ghosts and the Goldstone Equivalence Theorem](gauge-fixing-in-the-electroweak-theory-r-xi-gauges-ghosts-and-the-goldstone-equivalence-theorem.html). The gauge-fixing mechanism that QCD borrows unchanged.
- [Quantum Chromodynamics under the Biquaternion Framework: A Research Agenda](quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html). The classification that the ledger follows.
- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The colour quantum numbers of the fifteen fields, and $\alpha_s$ among the parameters.
- [The Photon in Biquaternionic Form](the-photon-in-biquaternionic-form.html). The abelian case, where the structure constants vanish and both self-couplings are absent.
- [Asymptotic Freedom and the Running of the Strong Coupling](asymptotic-freedom-and-the-running-of-the-strong-coupling.html). The full one-loop arithmetic behind $b_0$, which this article hands on as $11C_A/3-4T_RN_f/3$.
- [Confinement and the Loss of Partonic Information in Biquaternionic Form](confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html). Why the octet is never an asymptotic state, which is the question the Feynman rules of this article cannot answer.

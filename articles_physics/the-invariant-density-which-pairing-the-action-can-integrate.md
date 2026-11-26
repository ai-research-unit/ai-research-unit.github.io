# __The Invariant Density: Which Pairing the Action Can Integrate__

## Introduction

**The claim.** An action is a number. Under the integral it therefore needs a density that is a real scalar, that a local transformation cannot move, and that has one sign. Three requirements, and one functional supplies all three: the matrix trace. This article states why, and it states the criterion that decides *which* trace — the module the field lives on. **The pairing is not chosen by taste; it is read off the transformation law of the field.**

**What is established.** Four things. First, the cyclicity of the trace is the whole of the invariance of the curvature's square, and a pairing that is not cyclic has no invariant square to offer. Second, reality and the sign come from the Hermiticity type of the field, so the printed sign and the printed coefficient are one statement and not two. Third, on the biquaternion algebra, $2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ and the matrix trace are the *same functional*, so there is no conflict at the algebra's own size, and the reason the density is a trace is a statement about the module and not about a symmetry. Fourth, the coefficient $\tfrac12$ in the element form and $\tfrac14$ in the component form are forced by the normalisation of the basis, and a basis whose arrays carry two different trace norms forces a rescaling per array.

**What is not new.** The Yang–Mills density is four lines in any field-theory text. **What the corpus adds is the ordering of the argument**: the requirements first, the functional second, the module third, and the coefficient last. The three fragments existed before this article, in the [non-abelian Lagrangian](the-lagrangian-and-the-non-abelian-connections.html), in [the machinery under the primordial action](the-machinery-under-the-primordial-action-trace-curvature-ghosts-and-one-loop.html) and in [the connection carrier](the-connection-carrier-of-the-material-sector-why-the-action-is-one-sided.html), each stated where it was used and none stated before its use. This article puts the three in one place, in the order a reader needs them, and it resolves the one point where the three fragments read differently.

**Why it comes before the forces.** Every force block writes an action, and every action needs this page. A reader who meets the trace argument inside a sector has to accept it from a position in which the sector's own notation is already doing work. **The argument is six paragraphs long and it belongs to no sector.**

## The Three Requirements

**A density is integrated, so it must be a number.** The action is

$$
S=\int d^4r\;\mathcal{L}, \qquad \mathcal{L}\in\mathbb{R},
$$

with $d^4r$ the measure of the frame article and $\mathcal{L}$ a real scalar function. **A biquaternion carries eight real numbers**, so a candidate density that is an element and not a scalar is eight densities at once, and nothing in the theory says how to add them. **Only the scalar part, and only its real part, survives the requirement**, and that is why the corpus writes every Lagrangian as a scalar part or a trace and never as a bare element.

**It must be invariant, because a local transformation is a redundancy and not a change.** If $\tilde Q(R)$ is a group element that depends on the point, then the field's representative moves,

$$
F_{\imath\jmath}\longmapsto F_{\imath\jmath}^{\mathrm g}=\tilde QF_{\imath\jmath}\tilde Q^{-1},
$$

and the physical configuration does not. **A density that changed under that map would make the action depend on the description**, so the stationarity condition would select a representative and not a field. This is the same requirement the [covariant derivative](the-covariant-derivative-and-connection-in-biquaternionic-form.html) meets by construction: the derivative was built so that $D_{\imath}\tilde{Ξ}$ transforms as $\tilde{Ξ}$ does, and the density is built so that the product of two such objects does not transform at all.

**It must have one sign, because the energy is a square.** In the Minkowski section the statement is that the Hamiltonian is bounded below; on the Euclidean section it is that $e^{-S_E}$ converges. **Both are statements about the sign of a sum of squares**, and both fail if the density is indefinite.

**Why the quadratic and nothing else.** Locality, invariance and dimension four leave one functional of the curvature alone. A cubic term vanishes because the trace of an odd number of generators is zero; a term with a derivative of the curvature has dimension five; a term with no curvature is a constant. **So the density is the square, and the whole question is which square.**

## Cyclicity Is the Whole of the Invariance

**The computation is one line, and it is worth writing because it is the entire argument.**

$$
\operatorname{tr}\Bigl(\sum_{\imath,\jmath}F^{\mathrm g}_{\imath\jmath}F^{\mathrm g}_{\imath\jmath}\Bigr)
=\operatorname{tr}\Bigl(\sum_{\imath,\jmath}\tilde QF_{\imath\jmath}\tilde Q^{-1}\tilde QF_{\imath\jmath}\tilde Q^{-1}\Bigr)
=\operatorname{tr}\Bigl(\tilde Q\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr)\tilde Q^{-1}\Bigr)
=\operatorname{tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr).
$$

**Three steps and each is a different fact.** The first is the transformation law of the curvature. The second is that $\tilde Q^{-1}\tilde Q=e_t$, so the four factors collapse to two around the square. The third is cyclicity, $\operatorname{tr}(XY)=\operatorname{tr}(YX)$.

**Only the third is at risk in a general pairing.** The first two are properties of the group action and of associativity, and they hold in any associative algebra. **The invariance of the square therefore rests entirely on the pairing being cyclic**, and a pairing that is symmetric but not cyclic has no invariant square.

**A pairing that fails, written out.** Take the bilinear form that reads the scalar part of each factor separately,

$$
p(X,Y)=\operatorname{Sc}(X)\,\operatorname{Sc}(Y).
$$

It is bilinear, symmetric, real on real elements, and it has no invariant square. **The reason is not subtle**: $\operatorname{Sc}(\tilde QF\tilde Q^{-1})$ is not $\operatorname{Sc}(F)$ when $\tilde Q$ is not central, so the product of two such readings moves under the transformation even though each factor is built from the curvature. **The failure is in the pairing and nowhere else**, which is what makes cyclicity the operative property rather than a technical convenience.

**The general statement.** A pairing $p$ gives an invariant square under the adjoint action exactly when $p(\tilde QX\tilde Q^{-1},\tilde QY\tilde Q^{-1})=p(X,Y)$. **That is the defining property of an invariant bilinear form on a Lie algebra**, and on a matrix algebra the trace supplies it while the scalar part of each factor does not.

## Reality, and Where the Sign Comes From

**The density must be real, and no extra condition is needed for it.** Let $F$ be anti-Hermitian, $F^{\dagger}=-F$, which is the case in the material sector where the connection takes values in $\mathbb{B}_\Phi$. Then $F^2$ is Hermitian, $(F^2)^{\dagger}=F^{\dagger}F^{\dagger}=F^2$, so its trace is real. **Hermiticity of the field is inherited by its square, and the trace of a Hermitian matrix is real.** Nothing was added.

**Positivity is the same fact read one step further.** An anti-Hermitian $F$ has purely imaginary eigenvalues $i\lambda$ with $\lambda$ real, so $F^2$ has eigenvalues $-\lambda^2\le 0$. Equivalently $-F^2=(-iF)^{\dagger}(-iF)$, the product of an operator with its adjoint. **So $\operatorname{tr}(F^2)\le 0$, with equality only for $F=0$, and $-\operatorname{tr}(F^2)\ge 0$**, and the density

$$
\mathcal{L}=-\tfrac12\operatorname{tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr)
$$

is non-negative. **The minus sign is not a convention independent of the field's Hermiticity**: it is the sign that turns the square of an anti-Hermitian object into a positive number.

**The same number in the other convention.** Let $t_a$ be Hermitian generators and $F_{a,\imath\jmath}$ real, and put $\mathbb{F}_{\imath\jmath}=\sum_a F_{a,\imath\jmath}t_a$. Then $\mathbb{F}$ is Hermitian and $\operatorname{tr}(\mathbb{F}^2)\ge0$, so the positive density is written with a plus,

$$
-\tfrac12\operatorname{tr}\Bigl(\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}\Bigr)
=\tfrac12\operatorname{tr}\Bigl(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath}\Bigr)
$$

with $\mathbb{F}=iF$, the two differing by one factor of $i$ and by nothing else.

**The rule this yields, and it is the rule the corpus needs.** The printed sign belongs to the Hermiticity type of the object it multiplies. **A density written $-\tfrac12\operatorname{tr}(FF)$ is a positive density for anti-Hermitian $F$; a density written $-\tfrac12\operatorname{tr}(\mathbb{FF})$ is a positive density for anti-Hermitian $\mathbb{F}$, and a negative one for Hermitian $\mathbb{F}$.** Every display in the corpus that carries $\operatorname{tr}$ must therefore be read together with the line that fixes the Hermiticity of its generators, and the two displays that print $-\tfrac12\operatorname{tr}(\sum\mathbb{FF})$ and $-\tfrac14\sum_aF_aF_a$ with Hermitian $t_a$ are the second form. **This is the one inconsistency between the three fragments, and it is a sign stated in one convention and read in the other.**

**Where positivity is a statement at all.** In the Minkowski section the contraction $\sum_{\imath,\jmath}F_{\imath\jmath}F_{\imath\jmath}$ carries $\varepsilon_{\imath}=(1,-1,-1,-1)$ and is not positive definite: for a solution with $\vec E$ and $\vec B$ it reads $\vec E^2-\vec B^2$. **So positivity is not a property of the Minkowski density**; it is a property of the Euclidean section, where the contraction is with $\delta_{\imath\jmath}$ and the sum is a sum of squares. In Minkowski signature the correct requirement is the weaker one, that the Hamiltonian built from the density be bounded below, and the two requirements agree after the [Wick rotation](interpretation-of-the-wick-rotation-in-the-biquaternion-universe.html). **Every positivity claim in the corpus is a Euclidean claim, and it is worth saying so once rather than in each sector.**

## The Element Pairing and the Trace Are One Functional at Two by Two

**The corpus carries two pairings, and at the algebra's own size they coincide.** The informational reduction is $2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$, the coefficient of $e_t$ in the product doubled. The matrix trace is $\operatorname{tr}$. On $\mathbb{B}\cong M_2(\mathbb{C})$ the three imaginary units are traceless, so

$$
\operatorname{tr}\tilde Q=2\operatorname{Sc}\tilde Q
\quad\Longrightarrow\quad
\operatorname{tr}(\tilde Q_1\tilde Q_2)=2\operatorname{Sc}(\tilde Q_1\tilde Q_2).
$$

**One functional, two notations.** So the sentence "the density is a trace and not the corpus's pairing" cannot mean that the two disagree on $2\times2$ matrices; on that size they are equal term by term, and their cyclicity is one and the same property.

**What the sentence does mean, stated precisely.** The field whose density is wanted is a matrix over $\mathbb{C}^4$ — fifteen $4\times4$ generators, or a quartets-valued spinor — and the biquaternion pairing has no argument of that size. **The obstruction is the dimension of the module and not the symmetry of the pairing.** The corpus's own machinery article says this in one line, and this section is the reason that line holds.

**Two failures that a reader should be able to tell apart.**

| Failure | What it looks like | What it is |
|---|---|---|
| Symmetry | the density moves when $\tilde Q$ depends on the point | the pairing is not invariant under the adjoint action |
| Definition | the pairing has no argument | the module is larger than the pairing's domain |

**The corpus's case is the second, and only the second.** A reader who conflates them will look for a symmetry violation where there is none, and will miss the real statement, which is that the algebra's pairing is available *on the algebra* and unavailable *on the module the force acts on*.

**A partial trace is not a way out.** One can take a $2\times2$ sub-block of a $4\times4$ matrix and trace over it. The result is not invariant: a transformation that mixes the sub-block with its complement moves the sub-block's trace while leaving the full trace alone. **So the shortcut fails for the reason invariance always fails, and it is worth naming because it is the mistake a reader makes next.**

## The Coefficient a Normalised Basis Forces

**With a normalised basis the element form and the component form are the same number.** Let $t_a$ satisfy

$$
\operatorname{tr}(t_at_b)=\tfrac12\delta_{ab},
$$

and let $\mathbb{F}_{\imath\jmath}=\sum_a F_{a,\imath\jmath}t_a$ with real coefficients. Then

$$
\operatorname{tr}\Bigl(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath}\Bigr)
=\sum_{a,b}\Bigl(\sum_{\imath,\jmath}F_{a,\imath\jmath}F_{b,\imath\jmath}\Bigr)\operatorname{tr}(t_at_b)
=\tfrac12\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath},
$$

so

$$
-\tfrac12\operatorname{tr}\Bigl(\sum_{\imath,\jmath}\mathbb{F}_{\imath\jmath}\mathbb{F}_{\imath\jmath}\Bigr)
=-\tfrac14\sum_{a,\imath,\jmath}F_{a,\imath\jmath}F_{a,\imath\jmath}.
$$

**The $\tfrac14$ is not a choice of convention.** It is what $\operatorname{tr}(t_at_b)=\tfrac12\delta_{ab}$ forces, and it moves if the normalisation moves. **The two displays that look like two conventions are one number read in two bases**, and the basis is fixed by the requirement that the kinetic term of $A_{a,\imath}$ be canonical. **The sign in the display is the one §*Reality, and Where the Sign Comes From* fixes**: carried over from the anti-Hermitian reading it makes the density negative on Hermitian generators, and the positive density in this basis is the same expression with a plus. The coefficient and the sign are therefore two separate readings of the same table, and only the coefficient is forced by the normalisation.

**Cross terms appear the moment the basis is not orthonormal.** If $\operatorname{tr}(t_at_b)$ has off-diagonal entries, the density carries $\sum_{a\ne b}F_aF_b\operatorname{tr}(t_at_b)$ and is no longer diagonal in the fields. **The orthonormality is therefore part of the derivation and not a tidying step.**

**Two norms and one rescaling that cannot serve.** A basis built from printed arrays whose trace norms differ cannot be normalised by one constant. The primordial block's arrays are exactly of this kind: fourteen with $\operatorname{tr}(G_a^{\dagger}G_a)=2$ and one, the corner, with $12$. **One constant cannot bring both to $\tfrac12$**, so the rescaling is per array,

$$
t_a=\frac{iG_a}{\sqrt{2n_a}}, \qquad n_a=\operatorname{tr}(G_a^{\dagger}G_a),
$$

and the factor between the two families is $\sqrt{6}$. **A vertex read off $G_a$ instead of $t_a$ is wrong by that factor on the corner and right on the planes**, and no overall rescaling repairs a mismatch that is not overall.

**The sign is a second trap in the same place.** The printed arrays are anti-Hermitian, so $\operatorname{tr}(G_a^2)=-n_a<0$. **A density written on $G_a$ has the wrong sign on every one of the generators**, and the same table that fixes the norm fixes the sign. That is why the normalisation of a basis is one operation and not two: the length, the angle and the sign are all read from $\operatorname{tr}(G_a^{\dagger}G_b)$.

**Why the off-diagonal entries need a rotation and not a rescaling.** A norm fixes an array's length and says nothing about its angle, so two arrays can each be correctly normalised and still fail to be transverse. **The corpus's basis has exactly two such pairs**, and both pair the corner with a colour diagonal; the rotation that removes them is part of the normalisation. **The general statement: orthonormality is a condition on the Gram matrix, and a diagonal rescaling can only fix its diagonal.**

## When the Local Group Acts on the Left

**The trace is invariant under conjugation and not under left multiplication.** Two actions of one group element on one element,

$$
X\longmapsto \tilde QX\tilde Q^{-1} \qquad\text{and}\qquad X\longmapsto\tilde QX,
$$

are both linear and both invertible, and they behave differently under the trace.

| Property | Conjugation $\tilde QX\tilde Q^{-1}$ | Left product $\tilde QX$ |
|---|---|---|
| multiplicative in the parameter | yes, an inner automorphism | no, not an endomorphism |
| preserves the trace | yes | no |
| preserves the star | yes | no |
| preserves Hermiticity | yes | no |

**The discriminator is a proof and not a numerical accident.** The trace of a commutator vanishes, so conjugation preserves the trace for every $\tilde Q$. The left product changes it whenever $\tilde Q$ is not central, because $\operatorname{tr}(\tilde QX)=\operatorname{tr}(X\tilde Q)$ and that differs from $\operatorname{tr}(X)$ in general. **The corpus checked the first line to a residual of $2\times10^{-15}$ over random elements and random rotors, and the check agrees with the proof**; the proof is what makes it a discriminator.

**What this means for a density.** On the carrier, where the local transformation multiplies the matter field on the left, the trace of a square is *not* available as a density. **The invariant there is built from the Hermitian form instead**, $\operatorname{tr}(\tilde{Ξ}^{\dagger}\tilde{Ξ})$, which is invariant because a left multiplication by a unitary element cancels against its adjoint. **The pairing follows the transformation law of the field, and that is the criterion of the article**: the adjoint action wants the trace of a product; the module action wants the Hermitian form.

**Why this is the same criterion as the dimension argument.** In both cases the question is what the field is an element of. **A field in the algebra transforms by conjugation, so the algebra's own trace is available. A field in a module transforms by left multiplication, so only the module's inner product is available. A field in $\mathbb{C}^4$ under a transcribed group transforms by the defining representation, and the trace is again available — on $\mathbb{C}^4$.** One criterion, three answers.

## What the Density Does Not Decide

**It fixes the form of the kinetic term and nothing else.** Four statements it does not make.

- *It fixes no group.* The density exists for any compact group whose generators can be traced; whether the algebra *contains* that group is the ceiling question, and the density is silent. The biquaternion algebra carries $\mathrm{U}(2)$, and $\mathrm{SU}(3)$ is transcribed.
- *It fixes no running.* The coefficient of the classical density is one number; the beta function is a one-loop object computed from the fluctuation determinant.
- *It fixes no mass gap, and no confinement.* Both are non-perturbative statements about the quantum theory.
- *It fixes no potential.* The scalar potential is a separate functional of the scalar, restricted by invariance and dimension but not determined by them.

**It does fix one thing that is often left implicit.** The relative weight of the connection's kinetic term and the matter's kinetic term is not free once both are written on normalised bases; **the single coupling of a gauge theory is the statement that the two weights are one number.** That identity is what the words *one force* mean, and the density is where it becomes checkable.

## Summary

The density an action integrates must be a real scalar, invariant under the local transformation, and of one sign. **One functional supplies all three, the matrix trace, and cyclicity is the whole of the invariance**: the square of the curvature is invariant under $F\mapsto\tilde QF\tilde Q^{-1}$ exactly because $\operatorname{tr}(XY)=\operatorname{tr}(YX)$, and a pairing that is not cyclic has no invariant square.

Reality and positivity follow from the Hermiticity type and not from extra conditions. **With anti-Hermitian $F$ the square's trace is real and non-positive and the density carries a minus; with Hermitian generators and real coefficients the same number carries a plus.** The sign is one statement with the Hermiticity, and every display must be read with the line that fixes it. **Positivity itself is a Euclidean statement**: in Minkowski signature the contraction is indefinite and the requirement is a bounded Hamiltonian.

On $\mathbb{B}\cong M_2(\mathbb{C})$ the element pairing $2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ and the trace are the same functional, so there is no conflict at the algebra's size. **The density is a trace because the force acts on a $\mathbb{C}^4$ module, and the algebra's pairing has no argument there**; the obstruction is the module's dimension and not the pairing's symmetry.

The coefficient is forced by the basis. **$\operatorname{tr}(t_at_b)=\tfrac12\delta_{ab}$ yields $\tfrac12$ in the element form and $\tfrac14$ in the component form**, and a basis whose arrays carry two trace norms forces a rescaling per array, with a factor of six between the families. Off-diagonal Gram entries are removed by a rotation and not a rescaling.

When the local group acts on the left, the trace is not available and the Hermitian form is. **The pairing follows the transformation law of the field, and the trace discriminates the two actions exactly.**

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | The biquaternion algebra, $\cong M_2(\mathbb C)$ |
| $\mathbb{B}_\Phi,\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $F_{\imath\jmath}$ | Curvature components, $\partial_{\imath}A_{\jmath}-\partial_{\jmath}A_{\imath}+[A_{\imath},A_{\jmath}]$ |
| $\mathbb{F}_{\imath\jmath}=\sum_aF_{a,\imath\jmath}t_a$ | The same curvature expanded on the normalised basis |
| $\operatorname{tr}$ | The matrix trace on the module the field lives on |
| $\operatorname{Sc}$ | The coefficient of $e_t$ in an element; $\operatorname{tr}\tilde Q=2\operatorname{Sc}\tilde Q$ on $M_2(\mathbb C)$ |
| $2\operatorname{Sc}(\tilde Q_1\tilde Q_2)$ | The corpus's informational reduction; equal to $\operatorname{tr}(\tilde Q_1\tilde Q_2)$ at $2\times2$ |
| $t_a$ | Normalised generators, $\operatorname{tr}(t_at_b)=\tfrac12\delta_{ab}$ |
| $G_a$ | Printed arrays, anti-Hermitian, $\operatorname{tr}(G_a^{\dagger}G_a)=n_a$ |
| $n_a$ | The array's own trace norm; $2$ on the fourteen, $12$ on the corner |
| $\mathcal L$ | The density; $-\tfrac12\operatorname{tr}(\sum FF)$, equal to $-\tfrac14\sum_aF_aF_a$ |
| $d^4r$ | The measure of the frame article |
| $\varepsilon_{\imath}=(1,-1,-1,-1)$ | The Minkowski weights of a spacetime contraction |

## Further Reading

- Mikio Nakahara, *Geometry, Topology and Physics* (CRC Press, 2nd ed. 2003), for invariant bilinear forms, the Killing form and the trace as the matrix case of it.
- Sidney Coleman, *Aspects of Symmetry* (Cambridge University Press, 1985), for the trace-versus-other-invariants argument and the sign conventions of Euclidean gauge actions.
- Michael E. Peskin and Daniel V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the normalisation $\operatorname{tr}(t_at_b)=\tfrac12\delta_{ab}$ and the $\tfrac14$ that follows from it.
- Steven Weinberg, *The Quantum Theory of Fields*, vol. II (Cambridge University Press, 1996), for the construction of the Yang–Mills density from invariance and dimension alone.
- Chris J. Isham, *Modern Differential Geometry for Physicists* (World Scientific, 2nd ed. 1999), for the bundle-theoretic reading of the same one-line computation, in which the invariant form on the Lie algebra is the input and the trace is its matrix case.
- John C. Baez and Javier P. Muniain, *Gauge Fields, Knots and Gravity* (World Scientific, 1994), for the invariant pairing on a Lie algebra and its relation to the trace in a matrix representation.
- Michael F. Atiyah, *Geometry of Yang–Mills Fields* (Accademia Nazionale dei Lincei, 1979), for the invariant form as the input to the Chern–Weil construction.

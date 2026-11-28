# __The QCD Piece: Eight Generators, Three Colours, One Coupling__

## Introduction

**The claim.** The strong interaction contributes one row to the forty-seven: a single monomial with one coupling, one colour structure and a sum over six flavours and three colours folded inside it. The eight generators enter the row through the matrix $T^a$, the three colours through the trace that multiplies it, and the coupling is the same for every quark. Nothing in the row depends on which flavour carries the colour.

**The answer.**

$$
\boxed{\;\mathcal{L}_{\mathrm{QCD}}=-g_s\sum_{f}\bar q_f\gamma^\mu T^a q_f\,G^a_\mu\;\longrightarrow\;\text{one row, one constant }g_s\;}
$$

**Why one row and not eighteen.** A reader who multiplies six flavours by three colours and expects eighteen terms is counting the components of the sum. The piece is the monomial, and the sums over flavour and colour are inside it. The convention that makes the sum one piece is the first of the four in [The Census Rule](the-census-rule-dimension-four-residual-invariance-and-one-canonical-term-per-field.html), and it is what keeps the count finite.

**The standing.** The piece is standard, and the corpus's own treatment of the colour factor is in [The Gluon, an Octet Outside the Biquaternion Algebra](the-gluon-an-octet-outside-the-biquaternion-algebra.html). What this article adds is its place in the census: one row, one constant, and the reasons the row cannot be split.

## The Piece

**Written out, with the sums explicit.**

$$
\mathcal{L}_{\mathrm{QCD}}=-g_s\sum_{f=u,d,s,c,b,t}\sum_{\alpha,\beta=1}^{3}\bar q_{f\alpha}\gamma^\mu\,(T^a)_{\alpha\beta}\,q_{f\beta}\,G^a_\mu ,
$$

with $a$ summed from $1$ to $8$.

**The three ingredients.**

| Ingredient | Object | Count | Where it comes from |
|---|---|---|---|
| colour generators | $T^a=\tfrac12\lambda^a$ | $8$ | the adjoint of $\mathrm{SU}(3)_c$ |
| colours | $\alpha,\beta$ | $3$ | the fundamental of $\mathrm{SU}(3)_c$ |
| flavours | $f$ | $6$ | the quark content |

**The algebra of the generators.** $[T^a,T^b]=if^{abc}T^c$ and $\mathrm{tr}(T^aT^b)=\tfrac12\delta^{ab}$. The first is what makes the gluon self-interactions; the second is what makes the colour factor of a quark leg $C_F=\tfrac43$. Both are properties of the representation and neither is a parameter of the list.

**Why the coupling is one number.** Colour is unbroken: the vacuum carries no colour, so every colour index is treated the same way and the coefficient cannot depend on it. Flavour is a symmetry of the gauge interaction: the gluon couples to the colour current and not to the flavour index, so the coefficient cannot depend on $f$. One coefficient for the whole row is the statement that $\mathrm{SU}(3)_c$ is unbroken and flavour-blind.

## The Vertex and the Colour Factor

**The Feynman rule.** For a gluon of colour $a$, momentum $p$ and Lorentz index $\mu$ attached to a quark line,

$$
-i g_s\,\gamma^\mu\,T^a .
$$

**The colour factor of a quark leg.** Contracting two generators gives

$$
\sum_a T^a_{\alpha\beta}T^a_{\beta\gamma}=C_F\,\delta_{\alpha\gamma},\qquad C_F=\frac{N_c^2-1}{2N_c}=\frac{4}{3},
$$

which is the number that multiplies every quark-line colour trace. It is a rational number fixed by $N_c=3$ and not a measurement.

**Why the gluon does not couple to leptons.** The lepton fields are colour singlets, so $T^a q$ has no lepton analogue: the generator acts as zero on a singlet. The absence is the statement that the leptons carry no colour, and it is why the QCD row is built from quarks alone.

**Why the gluon does not couple to the photon or the $Z$.** The gluon carries colour and no electroweak charge, and the photon and $Z$ carry no colour. A coupling would need a field carrying both, and the content has none. The statement is the same one made in [The Replacement of the Derivative](the-replacement-of-the-derivative-five-blocks-and-nothing-else.html).

## What the Row Does Not Fix

**The mass basis is invisible to colour.** The rotation that diagonalises the quark masses acts on flavour indices and commutes with $T^a$, so the QCD row is the same in every flavour basis. This is why QCD has no mixing matrix: the matrix that appears in the charged current appears there because the weak ladder changes flavour, and colour does not.

**The coupling runs.** $g_s$ is one of the eighteen constants at a stated scale; its value at another scale is given by the renormalisation-group equation, and the one-loop coefficient is negative, which is asymptotic freedom. The running is a property of the coefficient and not a new row.

**The $\theta$ term is not part of the row.** $G\tilde G$ is a total derivative and contributes no vertex; it is the nineteenth parameter and none of the pieces. [What the List Omits](what-the-list-omits-ghosts-the-theta-term-neutrino-mass-and-gravity.html) states its status.

## Checks

1. The row count. One row for six flavours and three colours.
2. The generator count. Eight, the dimension of the adjoint of $\mathrm{SU}(3)_c$.
3. The colour factor. $C_F=4/3$ from $N_c=3$, not a measurement.
4. The coupling. One constant, $g_s$, and $\alpha_s=g_s^2/4\pi$.
5. The flavour blindness. The coefficient does not depend on $f$, because the gluon couples to colour and not to flavour.
6. The lepton absence. The generator acts as zero on a colour singlet.
7. The photon and $Z$ absence. No field in the content carries both colour and electroweak charge.
8. The basis independence. $T^a$ commutes with the flavour rotation, so the row has no mixing matrix.
9. The vertex. $-ig_s\gamma^\mu T^a$, with the colour factor multiplying the trace.
10. The $\theta$ term. A total derivative, a parameter and not a row.

## Summary

QCD is one row of the forty-seven: a single monomial with one coupling $g_s$, one colour matrix $T^a$ summed over eight generators, and sums over three colours and six flavours folded inside it.

The eight generators are the adjoint of $\mathrm{SU}(3)_c$ and the three colours are its fundamental; the colour factor $C_F=4/3$ follows from $N_c=3$ and is a rational number, not a measurement. The single coupling is the statement that colour is unbroken and flavour-blind.

The row has no mixing matrix, because colour commutes with the flavour rotation, and no photon or $Z$ partner, because no field carries both colour and electroweak charge. The $\theta$ term is a total derivative and belongs to the parameters, not to the rows.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G^a_\mu$ | The eight gluon fields, $a=1,\dots,8$ |
| $T^a$ | The colour generators $\tfrac12\lambda^a$ |
| $N_c$ | The number of colours, $3$ |
| $C_F$ | The quark-leg colour factor, $4/3$ |
| $g_s$ | The strong coupling, one of the eighteen constants |

## Further Reading

- [The Gluon, an Octet Outside the Biquaternion Algebra](the-gluon-an-octet-outside-the-biquaternion-algebra.html). The colour factor computed in the corpus's variables.
- [The Four Field Strengths](the-four-field-strengths-one-kinetic-piece-per-gauge-field.html). The gluon kinetic row and its self-interactions.
- [The Replacement of the Derivative](the-replacement-of-the-derivative-five-blocks-and-nothing-else.html). Where the row comes from.
- [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html). $g_s$ among the eighteen.
- [The Theta Parameter and Strong CP](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html). The term that is not a row.
